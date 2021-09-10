import os
import subprocess
import platform
import time

def ping(host):
    if platform.system().lower() == 'windows':
        timeout = '/n 30'
        size = '/l 160'
    else:
        #Colocar class erro
        print('error')

    completedPing = subprocess.run(['ping', timeout, size, host],
                                   stdout=subprocess.PIPE,    # Capture standard out
                                   stderr=subprocess.STDOUT)  # Capture standard error

    #resposta_replace = str(completedPing.stdout.replace('\\r\\n', ' ')
    stdout = completedPing.stdout
    
    #resposta_replace.split = resposta_replace.replace(',')

    #arquivo = open('report_ping.txt', 'a')

    #arquivo.write(str(resposta.split(','))

    return stdout.decode('ISO-8859-1') if resposta_replace.returncode == 0 else ''

host = input('Informe o IP: ')

print(ping(host))



P1 = 'proxy.idtbrasilhosted.com'
P2 = 'proxy2.idtbrasilhosted.com'
P3 = 'proxy3.idtbrasilhosted.com'
P4 = 'proxy4.idtbrasilhosted.com'
P5 = 'proxy5.idtbrasilhosted.com'
P6 = 'proxy6.idtbrasilhosted.com'
P7 = 'proxy7.idtbrasilhosted.com'
P8 = 'proxy8.idtbrasilhosted.com'
P9 = 'proxy9.idtbrasilhosted.com'
P10 = 'proxy10.idtbrasilhosted.com'
P11 = 'proxy11.idtbrasilhosted.com'
P12 = 'proxy12.idtbrasilhosted.com'
google = '8.8.8.8'
tracert = ''







