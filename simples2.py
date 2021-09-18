from pathlib import Path
from program import *
from main import *
import tempfile
import os
import getpass
import time
usuario = getpass.getuser()


 
def path_log():
    """Validar usuario logado"""

    usuario = getpass.getuser()

    """Validar Pastas e diretorios."""

    newpath = (r"C:\Users\{}\Desktop\LOG".format(usuario))

    if not os.path.exists(newpath):
        os.makedirs(newpath)

def file_portal(ip_portal):

    usuario = getpass.getuser()
    
    """Portal e TRACERT"""
    with  open (r"C:\Users\{}\Desktop\LOG\ping_portal.txt".format(usuario) , 'w') as  f :
        #Escreve o resultado em um txt
        f.write (r"ping /n 5000 /l 160 {} >> ping_portal.log".format(ip_portal))
        f.close()
    
    #Muda o tipo de arquivo para bat
    p = Path(r"C:\Users\{}\Desktop\LOG\ping_portal.txt".format(usuario))
    p.rename(p.with_suffix('.cmd'))

    #Abre o arquivo 
    os.system("start" r"C:\Users\{}\Desktop\LOG\ping_portal.cmd".format(usuario))

def file_TRACERT(ip_portal):

    usuario = getpass.getuser()

    with  open (r"C:\Users\{}\Desktop\LOG\ping_tracert.txt".format(usuario) , 'w') as  f :
        #Escreve o resultado em um txt
        f.write (r"tracert {} >> ping_tracert.txt".format(ip_portal))
        f.close()

    #Muda o tipo de arquivo para bat
    p = Path(r"C:\Users\{}\Desktop\LOG\ping_tracert.txt".format(usuario))
    p.rename(p.with_suffix('.cmd'))

    #Abre o arquivo 
    os.system("start" r"C:\Users\{}\Desktop\LOG\ping_TRACERT.cmd".format(usuario))

def file_DNS():

    usuario = getpass.getuser()

    with  open (r"C:\Users\{}\Desktop\LOG\ping_DNS.txt".format(usuario) , 'w') as  f :
        #Escreve o resultado em um txt
        f.write (r"ping /n 5000 8.8.8.8 >> ping_DNS.log")
        f.close()

    #Muda o tipo de arquivo para bat
    p = Path(r"C:\Users\{}\Desktop\LOG\ping_DNS.txt".format(usuario))
    p.rename(p.with_suffix('.cmd'))

    #Abre o arquivo 
    os.system("start" r"C:\Users\{}\Desktop\LOG\ping_DNS.cmd".format(usuario))

def sip_alg(s: str):
    os.startfile("program\sip-alg-detector.exe")

