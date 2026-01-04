import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
import os
from src.utils.colors import print_success, print_error

def generate_xml(data):
    try:
        root = ET.Element("ScanReport")
        
        ET.SubElement(root, "TargetIP").text = str(data.get('ip'))
        ET.SubElement(root, "Port").text = str(data.get('port'))
        ET.SubElement(root, "Service").text = str(data.get('service'))
        ET.SubElement(root, "Version").text = str(data.get('version'))
        
        vuln = ET.SubElement(root, "Vulnerability")
        ET.SubElement(vuln, "CVE").text = str(data.get('cve'))
        ET.SubElement(vuln, "Score").text = str(data.get('score'))
        ET.SubElement(vuln, "Severity").text = str(data.get('severity'))
        
        tree = ET.ElementTree(root)
        
       
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        reports_dir = os.path.join(base_dir, 'reports')
        
        filename = os.path.join(reports_dir, f"scan_{data['ip']}_{data['port']}.xml")
        tree.write(filename)
        print_success(f"XML Report saved: {filename}")
    except Exception as e:
        print_error(f"Failed to save XML: {e}")

def generate_html(data):
    try:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        templates_dir = os.path.join(base_dir, 'reports', 'templates')
        reports_dir = os.path.join(base_dir, 'reports')

        env = Environment(loader=FileSystemLoader(templates_dir))
        template = env.get_template('report_template.html')
        
        output = template.render(data=data)
        
        filename = os.path.join(reports_dir, f"report_{data['ip']}_{data['port']}.html")
        with open(filename, 'w') as f:
            f.write(output)
        print_success(f"HTML Report saved: {filename}")
    except Exception as e:
        print_error(f"Failed to save HTML: {e}")
