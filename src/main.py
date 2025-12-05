import sys
import os

# إضافة المسار الحالي للمكتبات لضمان استدعاء الملفات بشكل صحيح
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# استيراد الملفات مع معالجة الأخطاء
try:
    from src.utils.colors import Colors, print_logo, print_error, print_info
    from src.modules import waf_bypass
    from src.core import scanner, vuln_checker, exploit_manager, reporter
except ImportError as e:
    print(f"CRITICAL ERROR: Could not import modules. Reason: {e}")
    sys.exit(1)

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
                # --- القائمة الفرعية لاختيار المنافذ ---
                print(f"\n{Colors.CYAN}--- Port Selection ---{Colors.ENDC}")
                print("[1] Scan All Ports (0-65535)")
                print("[2] Scan Specific Port")
                
                port_choice = input(f"{Colors.YELLOW}Select Port Option > {Colors.ENDC}").strip()
                
                # نطلب الـ IP بعد تحديد نوع الفحص
                target_ip = input("Enter Target IP: ")

                if port_choice == '1':
                    target_port = 'all'
                    print_info("Selected: Full Range Scan (This might take time)")
                elif port_choice == '2':
                    target_port = input("Enter Target Port: ")
                else:
                    print_error("Invalid option. Defaulting to specific port scan.")
                    target_port = input("Enter Target Port: ")
                # -----------------------------------------------

                # 1. Scanning
                scan_res = scanner.run_nmap_scan(target_ip, target_port)
                if not scan_res: continue
                
                # تحديث البورت المكتشف
                detected_port = scan_res.get('port', target_port)

                # 2. Vuln Check
                exploit_info = vuln_checker.search_exploit_local(scan_res['service'], scan_res['version'])
                risk_info = vuln_checker.get_cvss_from_nvd(scan_res['service'], scan_res['version'])
                
                # 3. Exploit Manager
                if exploit_info:
                    want_dl = input(f"{Colors.CYAN}Exploit found! Download? (y/n): {Colors.ENDC}")
                    if want_dl.lower() == 'y':
                        path = exploit_manager.download_exploit(exploit_info['id'])
                        if path: exploit_manager.generate_session_guide(path, target_ip, detected_port)

                # 4. Reporting
                report_data = {
                    'ip': target_ip, 'port': detected_port,
                    'service': scan_res['service'], 'version': scan_res['version'],
                    'cve': risk_info['cve'], 'score': risk_info['score'], 'severity': risk_info['severity']
                }
                reporter.generate_xml(report_data)
                reporter.generate_html(report_data)

            elif choice == '2':
                domain = input("Enter Domain (e.g. site.com): ")
                waf_bypass.detect_waf(domain)

            elif choice == '3':
                domain = input("Enter Domain (e.g. site.com): ")
                waf_bypass.get_real_ip(domain)

            elif choice == '4':
                print("Goodbye!")
                break
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print_error(f"An unexpected error occurred: {e}")

# ========================================================
# هذا هو الجزء الأهم الذي كان مفقوداً لديك
# ========================================================
if __name__ == "__main__":
    main_menu()
