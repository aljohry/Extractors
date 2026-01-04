import os
import sys


try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    
    _HEADER = Fore.MAGENTA
    _BLUE = Fore.BLUE
    _CYAN = Fore.CYAN
    _GREEN = Fore.GREEN
    _YELLOW = Fore.YELLOW 
    _FAIL = Fore.RED
    _ENDC = Style.RESET_ALL
    _BOLD = Style.BRIGHT
except ImportError:
    _HEADER = ''
    _BLUE = ''
    _CYAN = ''
    _GREEN = ''
    _YELLOW = ''
    _FAIL = ''
    _ENDC = ''
    _BOLD = ''

class Colors:
    HEADER = _HEADER
    BLUE = _BLUE
    CYAN = _CYAN
    GREEN = _GREEN
    YELLOW = _YELLOW   
    WARNING = _YELLOW  
    FAIL = _FAIL
    ENDC = _ENDC
    BOLD = _BOLD

def print_logo():
    logo = f"""{Colors.BOLD}{Colors.FAIL}
    ████████╗██╗  ██╗██████╗     ███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗████████╗ ██████╗ ██████╗ ███████╗
    ╚══██╔══╝██║  ██║██╔══==╝    ██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
       ██║   ███████║█████╗      █████╗   ╚███╔╝    ██║   ██████╔╝███████║██║        ██║   ██║   ██║██████╔╝███████╗
       ██║   ██╔══██║██╔══╝      ██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║██║        ██║   ██║   ██║██╔══██╗╚════██║
       ██║   ██║  ██║███████╗    ███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║███████║
       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                {Colors.CYAN}Auto Vulnerability Scanner & Exploit Manager{Colors.ENDC}
    """
    print(logo)
    print(f"{Colors.HEADER}[+] Project: The Full User Journey | Team: The Extractors{Colors.ENDC}")
    print("="*100 + "\n")

def print_step(step_name):
    print(f"\n{Colors.YELLOW}➤ {step_name}...{Colors.ENDC}")

def print_success(msg):
    print(f"{Colors.GREEN}[+] {msg}{Colors.ENDC}")

def print_error(msg):
    print(f"{Colors.FAIL}[!] {msg}{Colors.ENDC}")

def print_info(msg):
    print(f"{Colors.BLUE}[*] {msg}{Colors.ENDC}")
