import os
import subprocess
import platform
import time

host = input('Informe o IP: ')

def ping(portal):
    if platform.system().lower() == 'windows':
        timeout_l = '/t'
        size_l = '/l 160'
    else:
        timeout_c = '-c'

    completedPing = subprocess.run(['ping', size_l ,timeout_l, host],
                                   stdout=subprocess.PIPE,    # Capture standard out
                                   stderr=subprocess.STDOUT)  # Capture standard error
    resposta_replace = str(completedPing.stdout.replace('\\r\\n', ' ')
    stdout = resposta_replace.stdout
    
    #resposta_replace.split = resposta_replace.replace(',')

    #arquivo = open('report_ping.txt', 'a')

    #arquivo.write(str(resposta.split(','))

    return stdout.decode('ISO-8859-1') if p.returncode == 0 else ''

print(ping(host))







