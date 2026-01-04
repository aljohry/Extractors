import subprocess
import socket
import dns.resolver
from urllib.parse import urlparse
from src.utils.colors import print_info, print_success, print_error, print_step, Colors

def get_clean_domain(user_input):
   
    user_input = user_input.strip()
    if not user_input.startswith(('http://', 'https://')):
        user_input = 'http://' + user_input
    parsed = urlparse(user_input)
    return parsed.netloc if parsed.netloc else user_input

def detect_waf(raw_domain):
    target = get_clean_domain(raw_domain)
    print_info(f"Analyzing WAF signatures for: {target}")
    try:
        subprocess.run(['wafw00f', target], check=False)
    except FileNotFoundError:
        print_error("wafw00f tool is not installed.")
    except Exception as e:
        print_error(f"WAF Detection failed: {e}")

def resolve_dns_record(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [rdata.to_text() for rdata in answers]
    except:
        return []

def get_real_ip(raw_domain):
    target = get_clean_domain(raw_domain)
    print_info(f"Hunting for Real IP of [{target}]...")
    
    try:
        current_ip = socket.gethostbyname(target)
        print(f"{Colors.BLUE}[*] Current Public IP (Likely WAF/Firewall): {current_ip}{Colors.ENDC}")
    except:
        print_error(f"Could not resolve domain: {target}")
        return None

    found_candidates = []

    print_step("Checking MX Records (Mail Servers)...")
    mx_records = resolve_dns_record(target, 'MX')
    
    if mx_records:
        for mx in mx_records:
            try:
                mx_host = mx.split(' ')[1].strip('.')
                mx_ip = socket.gethostbyname(mx_host)
                
                if mx_ip != current_ip:
                    print(f"{Colors.GREEN}[+] Found Mail Server (MX): {mx_host} -> {mx_ip}{Colors.ENDC}")
                    print(f"    {Colors.YELLOW}↳ Hint: Mail servers are often on the same network as the web server.{Colors.ENDC}")
                    found_candidates.append(mx_ip)
            except:
                continue
    else:
        print(f"    {Colors.FAIL}[-] No MX records found.{Colors.ENDC}")

    print_step("Checking SPF Records (TXT Data)...")
    txt_records = resolve_dns_record(target, 'TXT')
    found_spf = False
    for txt in txt_records:
        if "v=spf1" in txt:
            parts = txt.replace('"', '').split(' ')
            for part in parts:
                if part.startswith('ip4:'):
                    spf_ip = part.split(':')[1]
                    if spf_ip != current_ip:
                        print(f"{Colors.GREEN}[+] Found IP in SPF Record: {spf_ip}{Colors.ENDC}")
                        found_candidates.append(spf_ip)
                        found_spf = True
    if not found_spf:
         print(f"    {Colors.FAIL}[-] No leaked IP in SPF records.{Colors.ENDC}")

    print_step("Scanning common subdomains...")
    subdomains = ['ftp', 'cpanel', 'webmail', 'direct', 'mail', 'dev', 'test', 'admin']
    found_sub = False
    for sub in subdomains:
        try:
            sub_target = f"{sub}.{target}"
            ip = socket.gethostbyname(sub_target)
            if ip != current_ip and ip not in found_candidates:
                print(f"{Colors.GREEN}[+] Found Subdomain IP ({sub_target}): {ip}{Colors.ENDC}")
                found_candidates.append(ip)
                found_sub = True
        except:
            continue
    if not found_sub:
        print(f"    {Colors.FAIL}[-] No unique IPs found in subdomains.{Colors.ENDC}")

    print("\n" + "="*50)
    if found_candidates:
        best_guess = found_candidates[0]
        print(f"{Colors.CYAN}Analysis Complete. Candidates found:{Colors.ENDC}")
        for ip in found_candidates:
            print(f" - {ip}")
        print(f"\n{Colors.YELLOW}[i] Recommendation: Try scanning {best_guess} manually.{Colors.ENDC}")
        return best_guess
    else:
        print_error("No bypass found. The WAF is configured correctly.")
        return current_ip
