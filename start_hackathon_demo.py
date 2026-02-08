
import os
import sys
import subprocess
import time
import platform
import shutil

# ANSI Colors (Graceful degradation)
try:
    import colorama
    colorama.init()
    class Colors:
        HEADER = colorama.Fore.MAGENTA
        BLUE = colorama.Fore.BLUE
        CYAN = colorama.Fore.CYAN
        GREEN = colorama.Fore.GREEN
        WARNING = colorama.Fore.YELLOW
        FAIL = colorama.Fore.RED
        ENDC = colorama.Style.RESET_ALL
        BOLD = colorama.Style.BRIGHT
        UNDERLINE = "" 
except ImportError:
    class Colors:
        HEADER = ""
        BLUE = ""
        CYAN = ""
        GREEN = ""
        WARNING = ""
        FAIL = ""
        ENDC = ""
        BOLD = ""
        UNDERLINE = ""

def print_header():
    print(Colors.HEADER + Colors.BOLD + """
    ████████████████████████████████████████████████
    █      EVOPYRAMID - TRINITY HACKATHON DEMO     █
    █      GOOGLE AI STUDIO / GEMINI 3 INTEGRATION █
    ████████████████████████████████████████████████
    """ + Colors.ENDC)
    print(Colors.CYAN + "    [SYSTEM] Initializing One-Click Launch Protocol..." + Colors.ENDC)
    print(Colors.CYAN + f"    [SYSTEM] OS: {platform.system()} {platform.release()}" + Colors.ENDC)
    print(Colors.CYAN + f"    [SYSTEM] Python: {sys.version.split()[0]}" + Colors.ENDC)
    time.sleep(1)

def check_dependencies():
    print(Colors.BLUE + "\n    [1/4] Checking Dependencies..." + Colors.ENDC)
    
    # Try to verify pip, but don't die if it's missing
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pip_available = True
        print(Colors.GREEN + "    [INFO] pip is available." + Colors.ENDC)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pip_available = False
        print(Colors.WARNING + "    [WARNING] pip not found. Skipping package installation." + Colors.ENDC)

    # Only attempt install if pip is alive
    if pip_available:
        req_file = "requirements.txt"
        if os.path.exists(req_file):
            print(Colors.GREEN + f"    [INFO] Found {req_file}. Attempting install..." + Colors.ENDC)
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', req_file], stdout=subprocess.DEVNULL)
                print(Colors.GREEN + "    [SUCCESS] Requirements installed." + Colors.ENDC)
            except subprocess.CalledProcessError:
                 print(Colors.WARNING + "    [WARNING] Failed to install requirements. Proceeding anyway..." + Colors.ENDC)

    print(Colors.GREEN + "    [SUCCESS] Dependency check complete (Soft Mode)." + Colors.ENDC)

def verify_environment():
    print(Colors.BLUE + "\n    [2/4] Verifying Environment Integrity..." + Colors.ENDC)
    
    # Check essential files
    critical_files = [
        os.path.join("core", "trinity_core.py"),
        os.path.join("core", "evolution_protocol.py"),
        os.path.join("src", "main.py"),
        os.path.join("src", "vision_monitor.py")
    ]
    
    missing_files = []
    for f in critical_files:
        if not os.path.exists(f):
            missing_files.append(f)
    
    if missing_files:
        print(Colors.FAIL + "    [CRITICAL] Missing core files:" + Colors.ENDC)
        for f in missing_files:
            print(Colors.FAIL + f"      - {f}" + Colors.ENDC)
        print(Colors.FAIL + "    [ABORT] Cannot proceed with demo." + Colors.ENDC)
        sys.exit(1)
        
    print(Colors.GREEN + "    [SUCCESS] Core architecture intact." + Colors.ENDC)

def run_demo():
    print(Colors.BLUE + "\n    [3/4] Launching Trinity Core..." + Colors.ENDC)
    time.sleep(1)
    
    main_script = os.path.join("src", "main.py")
    
    print(Colors.HEADER + "\n    --------------------------------------------------" + Colors.ENDC)
    print(Colors.HEADER + "    >>> STARTING DEMO SEQUENCE <<<" + Colors.ENDC)
    print(Colors.HEADER + "    --------------------------------------------------\n" + Colors.ENDC)
    
    try:
        # Run the main script and stream output
        result = subprocess.run([sys.executable, main_script], check=True)
        if result.returncode == 0:
            print(Colors.GREEN + "\n    [SUCCESS] Demo sequence completed successfully." + Colors.ENDC)
        else:
             print(Colors.FAIL + f"\n    [FAILURE] Demo exited with code {result.returncode}." + Colors.ENDC)
    except subprocess.CalledProcessError as e:
        print(Colors.FAIL + f"\n    [CRITICAL ERROR] Execution failed: {e}" + Colors.ENDC)
    except KeyboardInterrupt:
        print(Colors.WARNING + "\n    [ABORT] User interrupted execution." + Colors.ENDC)

def generate_report():
    print(Colors.BLUE + "\n    [4/4] Generating Hackathon Artifacts..." + Colors.ENDC)
    
    # Simulate saving artifacts if they weren't saved by the script itself
    # (The python scripts already save JSONs, here we just confirm)
    
    reports = [f for f in os.listdir('.') if f.startswith('trinity_') and f.endswith('.json')]
    if reports:
        print(Colors.GREEN + f"    [ARTIFACT] Found {len(reports)} generated reports." + Colors.ENDC)
        print(Colors.GREEN + f"    [ARTIFACT] Latest: {reports[-1]}" + Colors.ENDC)
    else:
        print(Colors.WARNING + "    [INFO] No new reports generated in root." + Colors.ENDC)

    print(Colors.HEADER + Colors.BOLD + "\n    [SYSTEM] HACKATHON SUBMISSION READY." + Colors.ENDC)

if __name__ == "__main__":
    # Windows ANSI support hack
    if platform.system() == 'Windows':
        os.system('color')
        
    print_header()
    check_dependencies()
    verify_environment()
    run_demo()
    generate_report()
    
    input(Colors.CYAN + "\n    Press Enter to exit..." + Colors.ENDC)
