from pathlib import Path
import tempfile
import os


def select_portal():

    while True:

        portalv = input('Informe o Portal: ')

        if portalv == 'portal1':
            portal1 = portalv.replace("portal1", "proxy.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 1: {portal1} ')
            write_ping(portal1)

        elif portalv == 'portal2':
            portal2 = portalv.replace("portal2", "proxy2.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 2: {portal2} ')
            

        elif portalv == 'portal3':
            portal3 = portalv.replace("portal3", "proxy3.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 3: {portal3} ')
            

        elif portalv == 'portal4':
            portal4 = portalv.replace("portal4", "proxy4.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 5: {portal4} ')
            

        elif portalv == 'portal5':
            portal5 = portalv.replace("portal5", "proxy5.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 5: {portal5} ')
            
        
        elif portalv == 'portal6':
            portal6 = portalv.replace("portal6", "proxy6.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 6: {portal6} ')
            
        
        elif portalv == 'portal7':
            portal7 = portalv.replace("portal7", "proxy7.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 7: {portal7} ')
            
        
        elif portalv == 'portal8':
            portal8 = portalv.replace("portal8", "proxy8.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 8: {portal8} ')
            
        
        elif portalv == 'portal9':
            portal9 = portalv.replace("portal9", "proxy8.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 9: {portal9} ')
            

        elif portalv == 'portal10':
            portal10 = portalv.replace("portal10", "proxy10.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 10: {portal10} ')
            
        
        elif portalv == 'portal11':
            portal11 = portalv.replace("portal11", "proxy11.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 11: {portal11} ')
            
        
        elif portalv == 'portal12':
            portal12 = portalv.replace("portal12", "proxy12.idtbrasilhosted.com")
            print(f'Portal selecionado Portal 12: {portal12} ')
            
        
        else:
            ('Digite um portal valido, exemplo: " portal12 " ')
            return portalv
    
        

def write_ping(portal):

    with open('ping_portal.txt', 'w') as f:
        #Escreve o resultado em um txt
        f.write('ping /n 30 /l 160 {} > ping_portal.txt'.format(portal))
        f.close()

    #Muda o tipo de arquivo para bat
    p = Path('ping_portal.txt')
    p.rename(p.with_suffix('.bat'))

    #Abre o arquivo 
    os.system('start ping_portal.bat')
    #Sai do sistema e apaga os dados
    sair = input('Digite qualquer tecla para sair: ')
    if sair == '0':
        os.remove('ping_portal.bat')
        exit
    else:
        os.remove('ping_portal.bat')
        exit

