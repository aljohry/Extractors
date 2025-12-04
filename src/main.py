import sys
import os

# إضافة المجلد الحالي للمسار ليتمكن من رؤية الـ modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.colors import Colors, print_logo, print_error, print_info
from src.modules import waf_bypass
from src.core import scanner, vuln_checker, exploit_manager, reporter

def main_menu():
    print_logo()
    print(f"{Colors.BOLD}Choose an action:{Colors.ENDC}")
    print("[1] Scan Target (Nmap & Vuln Check & Exploit)")
    print("[2] Detect WAF Type")
    print("[3] Find Real IP (Bypass WAF)")
    print("[4] Exit")

    while True:
        try:
            choice = input(f"\n{Colors.YELLOW}Extractor-Shell > {Colors.ENDC}").strip()
            
            if choice == '1':
                target_ip = input("Enter Target IP: ")
                target_port = input("Enter Target Port: ")
                
                # 1. Scanning
                scan_res = scanner.run_nmap_scan(target_ip, target_port)
                if not scan_res: continue
                
                # 2. Vuln Check
                exploit_info = vuln_checker.search_exploit_local(scan_res['service'], scan_res['version'])
                risk_info = vuln_checker.get_cvss_from_nvd(scan_res['service'], scan_res['version'])
                
                # 3. Exploit Manager
                if exploit_info:
                    want_dl = input(f"{Colors.CYAN}Exploit found! Download it? (y/n): {Colors.ENDC}")
                    if want_dl.lower() == 'y':
                        saved_path = exploit_manager.download_exploit(exploit_info['id'])
                        if saved_path:
                            exploit_manager.generate_session_guide(saved_path, target_ip, target_port)

                # 4. Reporting
                report_data = {
                    'ip': target_ip, 'port': target_port,
                    'service': scan_res['service'], 'version': scan_res['version'],
                    'cve': risk_info['cve'], 'score': risk_info['score'], 'severity': risk_info['severity']
                }
                reporter.generate_xml(report_data)
                reporter.generate_html(report_data)

            elif choice == '2':
                domain = input("Enter Domain: ")
                waf_bypass.detect_waf(domain)

            elif choice == '3':
                domain = input("Enter Domain: ")
                ip = waf_bypass.get_real_ip(domain)
                if ip: 
                    print_info(f"Use this IP for scanning: {ip}")

            elif choice == '4':
                print("Goodbye!")
                break
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print_error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main_menu()