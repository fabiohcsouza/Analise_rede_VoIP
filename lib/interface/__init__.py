from pathlib import Path
from program import *
import tempfile
import os
import getpass

usuario = getpass.getuser()

def dic_portais(entrada):
    """Dicionario de portais com proxy para uso:"""
    portal_entrada = {
        "portal1": "proxy.idtbrasilhosted.com",
        "portal2": "proxy2.idtbrasilhosted.com",
        "portal3": "proxy3.idtbrasilhosted.com",
        "portal4": "proxy4.idtbrasilhosted.com",
        "portal5": "proxy5.idtbrasilhosted.com",
        "portal6": "proxy6.idtbrasilhosted.com",
        "portal7": "proxy7.idtbrasilhosted.com",
        "portal8": "proxy8.idtbrasilhosted.com",
        "portal9": "proxy9.idtbrasilhosted.com",
        "portal10": "proxy10.idtbrasilhosted.com",
        "portal11": "proxy11.idtbrasilhosted.com",
        "portal12": "proxy12.idtbrasilhosted.com",
    }

    #entrada = input("Informe o portal: ")
    portal = portal_entrada[entrada]
 
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
        f.write (r"ping /n 5000 /l 160 {} >> ping_portal.log && tracert {} >> tracert_portal.log".format(ip_portal, ip_portal))
        f.close()
    
    #Muda o tipo de arquivo para bat
    p = Path(r"C:\Users\{}\Desktop\LOG\ping_portal.txt".format(usuario))
    p.rename(p.with_suffix('.cmd'))

    #Abre o arquivo 
    os.system("start" r"C:\Users\{}\Desktop\LOG\ping_portal.cmd".format(usuario))

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

def sip_alg():
    os.startfile("program\sip-alg-detector.exe")

