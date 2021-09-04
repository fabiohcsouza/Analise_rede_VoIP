import subprocess
from typing import List, TextIO, Any

host_l = ''
timeout_l = '/n 300'
size_l = '/l 160'


def ping():

    timeout = '/n 4'
    size = '/l 160'

    # Abre um subprocess ping usando a sintaxe Linux
    # l = subprocess.run(['ping', timeout_l, size_l, host_l], stdout=subprocess.PIPE)
    # Abre um subprocess ping usando a sixtaxe Windows
    p = subprocess.run(['ping', timeout, size, host], stdout=subprocess.PIPE)

    # stdout = l.stdout
    stdout = p.stdout

    # Retorna o texto do terminal se houver erro retorna vazio
    # return stdout.decode('UTF-8') if w.returncode == 0 else ''
    # no windows
    return stdout.decode('ISO-8859-1') if p.returncode == 0 else ''

    def valor():

    valor = ping()
    valor.split = valor.split()
    print(valor.split)

ping(): Any = (input('Informe o IP: '))



#with open('log_ping.txt' , 'w', encoding='ISO-8859-1') as arquivo:
#    for v in valor:
#        arquivo.write(str(valor))

