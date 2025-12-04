import requests
import subprocess
import json
from src.utils.colors import print_info, print_success, print_error

# مفتاح API الخاص بك
NVD_API_KEY = "c750683b-e975-4039-9d85-77018c81058d"

def search_exploit_local(service, version):
    """البحث باستخدام SearchSploit محلياً"""
    if not service or service == "Unknown":
        return None

    query = f"{service} {version}"
    print_info(f"Searching SearchSploit for: {query}")
    
    try:
        # تنفيذ الأمر searchsploit --json للبحث
        cmd = ['searchsploit', query, '--json']
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError:
            # أحياناً المخرجات لا تكون JSON صالح إذا لم توجد نتائج
            print_error("No results found in SearchSploit.")
            return None

        if data.get('RESULTS_EXPLOIT'):
            # نأخذ أول نتيجة كعينة
            exploit = data['RESULTS_EXPLOIT'][0] 
            title = exploit['Title']
            path = exploit['Path'] # مسار الـ EDB-ID
            print_success(f"Exploit Found: {title}")
            return {'title': title, 'path': path, 'id': exploit['EDB-ID']}
        else:
            print_error("No exploits found in local DB.")
            return None
    except FileNotFoundError:
        print_error("searchsploit is not installed.")
        return None
    except Exception as e:
        print_error(f"SearchSploit Error: {e}")
        return None

def get_cvss_from_nvd(service, version):
    """جلب الخطورة من NVD API"""
    if not service or service == "Unknown":
        return {'cve': 'N/A', 'score': 'N/A', 'severity': 'Unknown'}

    print_info(f"Querying NVD API for Risk Score ({service})...")
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    headers = {"apiKey": NVD_API_KEY}
    params = {"keywordSearch": f"{service} {version}", "resultsPerPage": 1}
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        if response.status_code == 200:
            data = response.json()
            if data['vulnerabilities']:
                cve_item = data['vulnerabilities'][0]['cve']
                cve_id = cve_item['id']
                
                # محاولة استخراج Score v3.1
                metrics = cve_item.get('metrics', {})
                cvss_data = {}
                if 'cvssMetricV31' in metrics:
                    cvss_data = metrics['cvssMetricV31'][0]['cvssData']
                elif 'cvssMetricV2' in metrics:
                    cvss_data = metrics['cvssMetricV2'][0]['cvssData']
                
                score = cvss_data.get('baseScore', 'N/A')
                severity = cvss_data.get('baseSeverity', 'Unknown')
                
                print_success(f"NVD Data Found: {cve_id} | Score: {score} ({severity})")
                return {'cve': cve_id, 'score': score, 'severity': severity}
        
        print_info("No specific CVE matched in NVD.")
        return {'cve': 'N/A', 'score': '0.0', 'severity': 'Low'}
        
    except Exception as e:
        print_error(f"API Connection Error: {e}")
        return {'cve': 'Error', 'score': '0.0', 'severity': 'Unknown'}