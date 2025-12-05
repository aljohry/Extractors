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
