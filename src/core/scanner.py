import nmap
from src.utils.colors import print_success, print_error, print_step

def run_nmap_scan(ip, port):
    nm = nmap.PortScanner()
    
    # 1. Normal Scan (SYN Scan) - Default
    print_step(f"Starting NORMAL SCAN (SYN) on {ip}:{port}")
    try:
        # -sS: SYN Scan, -sV: Version Detection
        nm.scan(ip, str(port), arguments='-sS -sV --version-intensity 5')
        
        # التحقق مما إذا كان هناك نتائج للـ Host
        if ip not in nm.all_hosts():
            raise Exception("Host down or blocking Ping")

        # التحقق من حالة البورت
        if int(port) in nm[ip]['tcp']:
            state = nm[ip]['tcp'][int(port)]['state']
        else:
            state = 'filtered'

        if state == 'open':
            service = nm[ip]['tcp'][int(port)]['product']
            version = nm[ip]['tcp'][int(port)]['version']
            if not service: service = "Unknown"
            
            print_success(f"Port {port} is OPEN. Service: {service} {version}")
            return {'service': service, 'version': version, 'state': 'open'}
        
        else:
            print_error(f"Port {port} seems filtered/closed. Initiating Fallback...")
            raise Exception("Port Filtered")

    except Exception as e:
        # 2. Fallback: FIN Scan (لتجاوز الفيروول)
        print_step("!! FALLBACK TRIGGERED: Switching to FIN SCAN (Stealth Mode) !!")
        try:
            # -sF: FIN Scan
            nm.scan(ip, str(port), arguments='-sF -sV')
            
            if ip in nm.all_hosts() and int(port) in nm[ip]['tcp']:
                state = nm[ip]['tcp'][int(port)]['state']
                
                # في FIN Scan، النتيجة open|filtered تعني احتمال أنه مفتوح
                print_success(f"FIN Scan Result for {port}: {state}")
                
                service = nm[ip]['tcp'][int(port)].get('product', 'Unknown Service')
                version = nm[ip]['tcp'][int(port)].get('version', '')
                
                return {'service': service, 'version': version, 'state': state}
            else:
                print_error("FIN Scan returned no results.")
                return None
            
        except Exception as e_fin:
            print_error(f"All scans failed: {e_fin}")
            return None