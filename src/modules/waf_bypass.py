import subprocess
import socket
import requests
import re
from src.utils.colors import print_info, print_success, print_error

def detect_waf(domain):
    print_info(f"Analyzing WAF signatures for: {domain}")
    try:
        # استدعاء wafw00f
        # ملاحظة: تأكد من تثبيت الأداة على النظام أو وجودها في المسار
        result = subprocess.run(['wafw00f', domain], capture_output=True, text=True, timeout=45)
        
        # البحث في المخرجات عن الجملة التي تحدد الـ WAF
        match = re.search(r'is behind (.*?)(?: \[|$)', result.stdout, re.IGNORECASE)
        
        if match:
            waf_name = match.group(1).strip()
            print_error(f"WAF DETECTED: {waf_name}")
            return waf_name
        else:
            if "No WAF detected" in result.stdout:
                print_success("No WAF detected.")
            else:
                print_info("WAF scan finished (Unclear result).")
            return None
    except FileNotFoundError:
        print_error("wafw00f tool is not installed or not in PATH.")
        return None
    except Exception as e:
        print_error(f"WAF Detection failed: {e}")
        return None

def get_real_ip(domain):
    print_info(f"Hunting for Real IP of {domain} (Bypassing Firewall)...")
    
    # 1. DNS العادي
    try:
        current_ip = socket.gethostbyname(domain)
        print_info(f"Current DNS IP: {current_ip}")
    except:
        print_error("Could not resolve domain.")
        return None

    # 2. محاكاة البحث عن IP مختلف عبر Subdomains (منطق مبسط لـ CloakQuest3r)
    potential_ips = []
    subdomains = ['ftp', 'direct', 'mail', 'dev', 'cpanel', 'webmail']
    
    for sub in subdomains:
        try:
            target = f"{sub}.{domain}"
            ip = socket.gethostbyname(target)
            if ip != current_ip:
                print_success(f"Found different IP on {target}: {ip}")
                potential_ips.append(ip)
        except:
            pass

    if potential_ips:
        return potential_ips[0] # إعادة أول IP وجدناه مختلف
    
    print_error("Could not find Real IP using basic methods.")
    return current_ip