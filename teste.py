from pathlib import Path
import tempfile
import os

entrada = str(input('Informe o Portal: '))

with open('ping_portal1.txt', 'w') as f:
    #Escreve o resultado em um txt

    f.write('ping /n 30 /l 160 {} > D: /log/ping_portal.txt'.format(entrada))
    f.close()
    #Muda o tipo de arquivo para bat
    p = Path('ping_portal1.txt')
    p.rename(p.with_suffix('.bat'))
    #Abre o arquivo 
    os.system('start ping_portal1.bat')
    #Sai do sistema e apaga os dados
    sair = input('Digite 0 para sair: ')
    if sair == '0':
        os.remove('ping_portal1.bat')


