# 🛡️ Extractors AutoScanner: The Full User Journey

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Kali-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Auto Vulnerability Scanner & Exploit Manager** *Graduation Project by Team: The Extractors*

---

## 🚀 Project Overview

**Extractors AutoScanner** is an advanced, automated security assessment tool designed to simulate the **"Full User Journey"** of a penetration tester. The tool automates the entire security workflow: starting from **Reconnaissance** and **WAF Evasion**, through **Scanning** and **Vulnerability Assessment**, and finally providing **Exploitation Guidance**.

This tool was built to assist security researchers and students in understanding the attack lifecycle within a controlled and educational environment.

---

## ✨ Key Features

### 1. 🔍 Intelligent Recon & WAF Bypass
- **WAF Detection:** Identifies the type of Web Application Firewall .
- **Real IP Hunting:** Attempts to bypass Cloudflare/WAFs by discovering the origin server's IP address through:
    - **DNS Reconnaissance:** Analyzing current DNS records.
    - **Common Subdomain Check:** Testing sensitive subdomains (e.g., ftp, dev, cpanel).
    - **MX Records:** Identifying Mail Server IPs.
    - **SPF Records:** Extracting authorized sender IPs from TXT data.

### 2. ⚔️ Smart Scanning Engine
- **Nmap Integration:** Fully automated and optimized port scanning.
- **Stealth Mode:** Automatically switches to **FIN Scan** if a standard scan is blocked by a firewall.
- **Port Selection:** Flexibility to scan **All Ports (0-65535)** or specific user-defined targets.
- **Input Sanitization:** Automatically cleans target URLs (removes http/https) to ensure scanning stability.

### 3. 🧠 Vulnerability Analysis (Hybrid Engine)
- **Service Enumeration:** Accurately detects service versions (e.g., `vsftpd 2.3.4`).
- **Exploit Search:** Queries the local **Exploit-DB** (SearchSploit) to find available exploits.
- **Risk Assessment:** Connects to the **NVD API (NIST)** to fetch real-time **CVSS Scores** and severity levels (Critical, High, Medium).
- **Emergency Fallback:** Includes an internal database for instant detection of known critical vulnerabilities even without an internet connection.

### 4. 💥 Exploit Management
- **Auto-Download:** Automatically fetches the actual exploit code to the `exploits/` directory.
- **Session Guide:** Generates a customized guide explaining how to execute the exploit against the specific target.

### 5. 📊 Reporting
- **Multi-Format:** Saves results in both **XML** (for data analysis) and **HTML** (for professional presentation).
- **Professional Templates:** Utilizes **Jinja2** to generate clean, readable, and structured HTML reports.

---

## 🛠️ Installation

To ensure the tool runs efficiently, **Kali Linux** or similar security distributions are recommended.  
Install the required system tools via `apt`:

```bash
# Update system and install dependencies
sudo apt update
sudo apt install nmap wafw00f exploitdb

# Clone the repository
git clone https://github.com/aljohry/Extractors
cd Extractors

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python requirements
pip install -r requirements.txt

# Run the tool
python3 src/main.py

 💻 Interface Concept | تصور الواجهة

The tool runs via a CLI with an interactive, colored interface. Below is the concept of the main menu including the Port Selection feature:



```text

    THE EXTRACTORS

    Auto Vulnerability Scanner & Exploit Manager



[+] Project: The Full User Journey | Team: The Extractors

================================================================================



Choose an action:

[1] Scan Target (Nmap & Vuln Check & Exploit)

[2] Detect WAF Type

[3] Find Real IP (Bypass WAF)

[4] Exit



Extractor-Shell > 1



--- Port Selection ---

[1] Scan All Ports (0-65535)

[2] Scan Specific Port

Select Port Option > _


