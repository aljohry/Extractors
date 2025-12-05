# 🛡️ Extractors AutoScanner: The Full User Journey

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Kali-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-for-the-badge)

**Auto Vulnerability Scanner & Exploit Manager** *Graduation Project by Team: The Extractors*

---

## 🚀 Overview | نبذة عن المشروع

**Extractors AutoScanner** هي أداة متقدمة ومؤتمتة لتقييم الأمن، مصممة لمحاكاة "رحلة المستخدم الكاملة" لمختبر الاختراق. تقوم الأداة بأتمتة العملية برمتها: بدءًا من **الاستطلاع (Reconnaissance)** و **تجاوز جدران حماية تطبيقات الويب (WAF Evasion)**، مروراً **بالفحص (Scanning)** و **تقييم الثغرات (Vulnerability Assessment)**، وصولاً إلى **إرشادات الاستغلال (Exploitation)**.

تم بناء هذه الأداة لمساعدة الباحثين الأمنيين والطلاب على فهم دورة حياة الهجوم في بيئة تعليمية ومضبوطة.

---

## ✨ Key Features | المميزات الرئيسية

### 1. 🔍 Intelligent Recon & WAF Bypass
- **WAF Detection:** تحديد نوع جدار حماية تطبيقات الويب (باستخدام `wafw00f`).
- **Real IP Hunting (البحث عن الـ IP الحقيقي):** محاولة تجاوز Cloudflare/WAFs بالبحث عن عنوان IP للخادم الأصلي عبر:
    - DNS History (سجل DNS).
    - Subdomain Enumeration (تعداد النطاقات الفرعية).
    - **MX Records** (سجلات خوادم البريد).
    - **SPF Records** (بيانات TXT).

### 2. ⚔️ Smart Scanning Engine
- **Nmap Integration:** فحص المنافذ مؤتمت بالكامل.
- **Stealth Mode (الوضع الخفي):** التبديل تلقائيًا إلى **FIN Scan** إذا تم حظر الفحص القياسي بواسطة جدار حماية.
- **Port Selection:** خيار لفحص **جميع المنافذ (0-65535)** أو منافذ محددة.

### 3. 🧠 Vulnerability Analysis
- **Service Enumeration:** اكتشاف إصدارات الخدمات (مثل `vsftpd 2.3.4`).
- **Exploit Search:** التحقق من قاعدة بيانات **Exploit-DB** المحلية (SearchSploit) للعثور على استغلالات متاحة.
- **Risk Assessment (تقييم المخاطر):** الاتصال بواجهة NVD API (NIST) لجلب درجات CVSS ومستويات الخطورة في الوقت الفعلي (Critical, High, Medium).

### 4. 💥 Exploit Management
- **Auto-Download:** تنزيل شفرة الاستغلال الفعلية إلى مجلد `exploits/` على جهازك.
- **Session Guide:** إنشاء دليل مخصص يشرح كيفية تشغيل الاستغلال ضد الهدف المحدد.

### 5. 📊 Reporting
- **Multi-Format:** حفظ النتائج بصيغتي **XML** (للبيانات) و **HTML** (للعرض التقديمي).
- **Professional Templates:** استخدام Jinja2 لإنشاء تقارير HTML نظيفة وسهلة القراءة.

---

## 🛠️ Installation | التثبيت

لضمان عمل الأداة بكفاءة، يوصى باستخدام **Kali Linux** أو توزيعات أمنية مماثلة.

### 1. Install System Tools (تثبيت أدوات النظام)
تأكد من تثبيت أدوات النظام التالية عبر `apt`:
```bash
sudo apt update
sudo apt install nmap wafw00f exploitdb
✨ Key Features | المميزات الرئيسية
1. 🔍 Intelligent Recon & WAF Bypass
WAF Detection: Identifies the type of Web Application Firewall (using wafw00f).

Real IP Hunting: Attempts to bypass Cloudflare/WAFs by searching for the origin server IP via:

MX Records (Mail Servers).

SPF Records (TXT Data).

Subdomain Enumeration.

DNS History.

2. ⚔️ Smart Scanning Engine
Nmap Integration: Fully automated port scanning.

Stealth Mode (Fallback): Automatically switches to FIN Scan if a standard scan is blocked by a firewall.

Port Selection: Option to scan All Ports (0-65535) or specific targets.

3. 🧠 Vulnerability Analysis
Service Enumeration: Detects service versions (e.g., vsftpd 2.3.4).

Exploit Search: Checks local Exploit-DB (SearchSploit) for available exploits.

Risk Assessment: Connects to NVD API (NIST) to fetch real-time CVSS Scores and Severity levels (Critical, High, Medium).

4. 💥 Exploit Management
Auto-Download: Downloads the actual exploit code to your machine in exploits/ folder.

Session Guide: Generates a custom guide on how to run the exploit against the specific target.

5. 📊 Reporting
Multi-Format: Saves results in both XML (for data) and HTML (for presentation).

Professional Templates: Uses Jinja2 for clean, readable HTML reports.

🛠️ Installation | التثبيت
To run this tool efficiently, Kali Linux is recommended. Follow these steps:

1. Install System Tools (تثبيت أدوات النظام)
Ensure you have the following system tools installed via apt:

Bash

sudo apt update
sudo apt install nmap wafw00f exploitdb
2. Clone Repository (تنزيل المشروع)
Bash

git clone [https://github.com/aljohry/Extractors.git](https://github.com/aljohry/Extractors.git)
cd Extractors
3. Setup Virtual Environment (إعداد البيئة)
Recommended to isolate project libraries:

Bash

python3 -m venv venv
source venv/bin/activate
4. Install Python Dependencies (تثبيت المكتبات)
This step installs all required libraries from requirements.txt:

Bash

pip install -r requirements.txt
🚀 Usage | طريقة الاستخدام
Run the main script from the terminal:

Bash

python3 src/main.py
Module Guide:
[1] Scan Target: The core module. Choose between All Ports or Specific Port, enter the IP, and let the tool do the rest.

[2] Detect WAF Type: Identifies if the site is protected.

[3] Find Real IP: Hunts for the origin IP using DNS/MX/SPF records.

⚠️ Disclaimer | إخلاء مسؤولية
This tool is for EDUCATIONAL and AUTHORIZED TESTING purposes only. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Always obtain proper permission before scanning any target.

Developed with ❤️ by The Extractors Team
