# -- imports -- #
import sys
import pyqrcode
from colorama import Fore
from pyqrcode import QRCode
import subprocess
import os
# -- banner -- #
os.system("clear")
pwd = subprocess.getoutput("pwd")
x = Fore.LIGHTBLUE_EX+f"[{Fore.WHITE}*{Fore.LIGHTBLUE_EX}]"
banner = f"""
                ▄▄▄▄▄▄▄   ▄ ▄▄▄▄  ▄▄▄ ▄▄▄▄▄▄▄  
                █ ▄▄▄ █ ▀ ▀ ▄█▀█▀▀▀▄▄ █ ▄▄▄ █  
                █ ███ █ ▀█▀ ▀ ▀█▄█▄█  █ ███ █  
                █▄▄▄▄▄█ █▀▄▀█ ▄ ▄▀▄ █ █▄▄▄▄▄█  
                ▄▄▄▄▄ ▄▄▄█▀█  ▀ █▄ ▄▀▄ ▄ ▄ ▄   
                ▄ ▄█ ▀▄██ █ ▀███▄▀▀▀███▀▀   ▀  
                █▄ █▀█▄▀▀▄▄ █▀▄█ ▄▄    ▀ █▄▀   
                ▀▀█ ▄█▄ ▀▀▄▄▄  ▀▀█▀▀▀▀█▄▀▄▄ ▀  
                ▀▄▄█▀▄▄▀ ▀██  ▀ ▀▄ ▀▄▀▀█▀▄▄▀  
                █  ▄▀█▄▀█▀  ▀███▄  ▀█▄▀█▀ █ ▀  
                █ ▄ █▀▄▀█▄▄ █▀▄ ▀▄█▀█▄███ ▄█▄  
                ▄▄▄▄▄▄▄ █ ▀▄▄  ▄▄▀▄▄█ ▄ ███▀▀  
                █ ▄▄▄ █ ▄▄ █  ▀ █▄▀▀█▄▄▄█ ▄█   
                █ ███ █ █ ▀ ▀████ ▄▀  ▄█▄███▀  
                █▄▄▄▄▄█ █▄  █▀▄██▄ ▄▀▄ █▄█▄▀   
         -----------------------------------------------
        {x} Developer : {Fore.WHITE}Ethereal
        {x} discord : {Fore.WHITE}eth2comp   
        {x} Coded By : {Fore.WHITE}ethan - 0xBBD                    
        {Fore.GREEN}------------------------------------------------
        {Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] The Programmer of this tool is irresponsible about any damage Or leak induced by the user 
"""
print(banner)
# -- url to qr code -- #
try:
    url = sys.argv[1]
    file_name = sys.argv[2]
    print(f"{x} URL :{Fore.WHITE} {url}")
    print(f"{x} Convert URL To QR Code ")
    myQR = QRCode(url)
    path = pwd+"/"+file_name
    print(f"{x} QR Code Saved :{Fore.WHITE} {path}")
    myQR.svg(file_name, scale= 8)
    print(f"{x} Open in Browser ")
    myQR.show()
# -- Argv Error -- #
except IndexError:
    print("         Usege : python3 CodeX.py <PHISHING_URL> <file_name.svg> ")
    exit()
# -- End -- #
