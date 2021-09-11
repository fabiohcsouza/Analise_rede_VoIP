from pathlib import Path
import tempfile
import os


def ping_portal(portal):

    portal = str(input('Informe o Portal: '))
    
    portal1 = 'proxy.idtbrasilhosted.com'
    portal2 = 'proxy2.idtbrasilhosted.com'
    portal3 = 'proxy3.idtbrasilhosted.com'
    portal4 = 'proxy4.idtbrasilhosted.com'
    portal5 = 'proxy5.idtbrasilhosted.com'
    portal6 = 'proxy6.idtbrasilhosted.com'
    portal7 = 'proxy7.idtbrasilhosted.com'
    portal8 = 'proxy8.idtbrasilhosted.com'
    portal9 = 'proxy9.idtbrasilhosted.com'
    portal10 = 'proxy10.idtbrasilhosted.com'
    portal11 = 'proxy11.idtbrasilhosted.com'
    portal12 = 'proxy12.idtbrasilhosted.com'

    portal = portal1
    portal = portal2

    with open('ping_portal1.txt', 'w') as f:
        #Escreve o resultado em um txt

        f.write('ping /n 30 /l 160 {} > ping_portal.txt'.format(portal))
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
        exit
    else:
        os.remove('ping_portal1.bat')
        exit


