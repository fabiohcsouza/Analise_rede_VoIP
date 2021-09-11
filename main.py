#Bibliotecas
import time
import platform
from simples2 import select_portal 

#Comandos

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def linha(tam=42):
    return '-' * tam

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m -\033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = input('\033[32mSua Opção: \033[m')

    return opc
        

#Variaveis

hora = time.ctime()
sys = platform.system()
syss = platform.release()

cabeçalho('Bem vindo!'), print(hora,'  -  ', sys, syss), print(linha(42))

while True:
    resposta = menu(['ANALISE DE REDE', 'MULTI-PING', 'SIP-ALG', 'NMAP', 'SAIR'])

    if resposta == '1':
        select_portal()
        
    elif resposta == '2':
        print('Opção 2')
    elif resposta == '3':
        print('Opção 3')
    elif resposta == '4':
        print('Opção 4')
    elif resposta == '5':
        cabeçalho('\033[34mSaindo do sistema até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m')
        time.sleep(4)