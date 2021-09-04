import os
import subprocess
import platform
import time


print('#'*20)
host = input('IP: ')
time.sleep(1)
print('-'*20)
timeout = input('Packages: ')
print('#'*20)


def ping(host, timeout):
    if platform.system().lower() == 'windows':
        numFlag = '-n'
    else:
        numFlag = '-c'
    completedPing = subprocess.run(['ping', numFlag, '1', '-w', timeout, host],
                                   stdout=subprocess.PIPE,    # Capture standard out
                                   stderr=subprocess.STDOUT)  # Capture standard error
    resposta_replace:  = str(completedPing.stdout.replace('\\r\\n', ' ')
    #resposta.split = resposta.replace(',')
    print(resposta_replace)

    # arquivo = open('report_ping.txt', 'a')

    #arquivo.write(str(resposta.split(','))

    return (completedPing.returncode == 0) and (b'TTL=' in completedPing.stdout)

print(ping(host, timeout))







