import os
import sys

# التأكد من دعم الألوان في Windows
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HEADER = Fore.MAGENTA
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    WARNING = Fore.YELLOW
    FAIL = Fore.RED
    ENDC = Style.RESET_ALL
    BOLD = Style.BRIGHT
except ImportError:
    # ألوان بديلة في حال لم يتم تثبيت colorama بعد
    HEADER = ''
    BLUE = ''
    CYAN = ''
    GREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    BOLD = ''

def print_logo():
    logo = f"""{BOLD}{FAIL}
    ████████╗██╗  ██╗██████╗     ███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗████████╗ ██████╗ ██████╗ ███████╗
    ╚══██╔══╝██║  ██║██╔══==╝    ██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
       ██║   ███████║█████╗      █████╗   ╚███╔╝    ██║   ██████╔╝███████║██║        ██║   ██║   ██║██████╔╝███████╗
       ██║   ██╔══██║██╔══╝      ██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║██║        ██║   ██║   ██║██╔══██╗╚════██║
       ██║   ██║  ██║███████╗    ███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║███████║
       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                {CYAN}Auto Vulnerability Scanner & Exploit Manager{ENDC}
    """
    print(logo)
    print(f"{HEADER}[+] Project: The Full User Journey | Team: The Extractors{ENDC}")
    print("="*100 + "\n")

def print_step(step_name):
    print(f"\n{WARNING}➤ {step_name}...{ENDC}")

def print_success(msg):
    print(f"{GREEN}[+] {msg}{ENDC}")

def print_error(msg):
    print(f"{FAIL}[!] {msg}{ENDC}")

def print_info(msg):
    print(f"{BLUE}[*] {msg}{ENDC}")