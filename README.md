# 🛡️ Extractors AutoScanner: The Full User Journey

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Kali-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Auto Vulnerability Scanner & Exploit Manager** *Graduation Project by Team: The Extractors*

---

## 🚀 Overview | نبذة عن المشروع
**Extractors AutoScanner** is an advanced, automated security assessment tool designed to simulate the "Full User Journey" of a penetration tester. Unlike simple scanners, this tool automates the entire process: from **Reconnaissance** and **WAF Evasion**, to **Scanning**, **Vulnerability Assessment**, and finally **Exploitation** guidance.

It is built to help security researchers and students understand the attack lifecycle in a controlled, educational environment.

## ✨ Key Features | المميزات الرئيسية

### 1. 🔍 Intelligent Recon & WAF Bypass
- **WAF Detection:** Identifies the type of Web Application Firewall (using `wafw00f`).
- **Real IP Hunting:** Attempts to bypass Cloudflare/WAFs by searching for the origin server IP via:
  - DNS History.
  - Subdomain Enumeration.
  - **MX Records** (Mail Servers).
  - **SPF Records** (TXT Data).

### 2. ⚔️ Smart Scanning Engine
- **Nmap Integration:** Fully automated port scanning.
- **Stealth Mode (Fallback):** Automatically switches to **FIN Scan** if a standard scan is blocked by a firewall.
- **Port Selection:** Option to scan **All Ports (0-65535)** or specific targets.

### 3. 🧠 Vulnerability Analysis
- **Service Enumeration:** Detects service versions (e.g., `vsftpd 2.3.4`).
- **Exploit Search:** Checks local **Exploit-DB** (SearchSploit) for available exploits.
- **Risk Assessment:** Connects to **NVD API (NIST)** to fetch real-time **CVSS Scores** and Severity levels (Critical, High, Medium).

### 4. 💥 Exploit Management
- **Auto-Download:** Downloads the actual exploit code to your machine.
- **Session Guide:** Generates a custom guide on how to run the exploit against the specific target.

### 5. 📊 Reporting
- **Multi-Format:** Saves results in both **XML** (for data) and **HTML** (for presentation).
- **Professional Templates:** Uses Jinja2 for clean, readable HTML reports.

### 6. 💻 Interface Concept | تصور الواجهة
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

---

## 🛠️ Installation | التثبيت

### Prerequisites
This tool is designed for **Kali Linux** or similar security distributions. Ensure you have the following system tools installed:
```bash
sudo apt update
sudo apt install nmap wafw00f exploitdb

