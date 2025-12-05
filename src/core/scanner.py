import nmap
from src.utils.colors import print_success, print_error, print_step, print_info

def run_nmap_scan(ip, port):
    nm = nmap.PortScanner()
    
    # تحديد نوع الفحص بناءً على المدخل
    if port.lower() == 'all':
        print_step(f"Starting FULL PORT SCAN (0-65535) on {ip} ... This may take time!")
        # -p- يعني فحص كل البورتات
        # -T4 لزيادة السرعة
        scan_args = '-p- -sS -sV -T4 --version-intensity 3'
        target_port_str = "All Ports"
    else:
        print_step(f"Starting NORMAL SCAN on {ip}:{port}")
        scan_args = f'-p {port} -sS -sV --version-intensity 5'
        target_port_str = str(port)

    try:
        # تنفيذ الفحص
        nm.scan(ip, arguments=scan_args)
        
        # التأكد من عمل السيرفر
        if ip not in nm.all_hosts():
            raise Exception("Host down or blocking Ping")

        # معالجة النتائج
        found_open_ports = []
        
        if port.lower() == 'all':
            # جلب كل البورتات المفتوحة
            if 'tcp' in nm[ip]:
                for p in nm[ip]['tcp']:
                    state = nm[ip]['tcp'][p]['state']
                    if state == 'open':
                        svc = nm[ip]['tcp'][p]['product']
                        ver = nm[ip]['tcp'][p]['version']
                        print_success(f"Found Open Port: {p}/tcp | Service: {svc} {ver}")
                        found_open_ports.append({'port': p, 'service': svc, 'version': ver})
            
            # نرجع أول بورت مفتوح وجدناه لنكمل عليه باقي العملية (للتبسيط)
            if found_open_ports:
                return {'service': found_open_ports[0]['service'], 
                        'version': found_open_ports[0]['version'], 
                        'state': 'open',
                        'port': found_open_ports[0]['port']} # نحفظ البورت الذي وجدناه
            else:
                print_error("No open ports found.")
                return None

        else:
            # الفحص العادي لبورت واحد
            p = int(port)
            if p in nm[ip]['tcp']:
                state = nm[ip]['tcp'][p]['state']
                if state == 'open':
                    service = nm[ip]['tcp'][p]['product']
                    version = nm[ip]['tcp'][p]['version']
                    print_success(f"Port {p} is OPEN. Service: {service} {version}")
                    return {'service': service, 'version': version, 'state': 'open', 'port': p}
            
            print_error(f"Port {port} seems closed/filtered.")
            return None

    except Exception as e:
        print_error(f"Scan failed: {e}")
        return None
