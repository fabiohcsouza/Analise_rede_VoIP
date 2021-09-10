
#Bibliotecas

import time
import platform
#from Analise_rede_VoIP import simples


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

def portal():
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

    while True:

        entrada = input('Informe o Portal, Ex: "portal4" ou Digite 0 para voltar: ')

        if 'portal1, Portal 1, portal 1' in entrada:
            print('Portal 1')
            break
        elif 'portal2' in entrada:
            print('p')
        elif 'portal3' in entrada:
            print('p')
        elif 'portal4' in entrada:
            print('p')
        elif 'portal5' in entrada:
            print('p')
        elif 'portal6' in entrada:
            print('p')
        elif 'portal7' in entrada:
            print('p')
        elif 'portal8' in entrada:
            print('p')
        elif 'portal9' in entrada:
            print('p')
        elif 'portal10' in entrada:
            print('p')
        elif 'portal11' in entrada:
            print('p')
        elif 'portal12' in entrada:
            print('p')
        elif '0' in entrada:
            print(isso())
        else:
            print('\033[31mERRO! Digite uma opção valida\033[m')
            time.sleep(4)
        


#Variaveis

hora = time.ctime()
sys = platform.system()
syss = platform.release()

cabeçalho('Bem vindo!'), print(hora,'  -  ', sys, syss), print(linha(42))

def isso():
    while True:
        resposta = menu(['ANALISE DE REDE', 'MULTI-PING', 'SIP-ALG', 'NMAP', 'SAIR'])

        if resposta == '1':
            print(portal())
        elif resposta == 2:
            print('Opção 2')
        elif resposta == 3:
            print('Opção 3')
        elif resposta == 4:
            print('Opção 4')
        elif resposta == 5:
            cabeçalho('\033[34mSaindo do sistema até logo!\033[m')
            break
        else:
            print('\033[31mERRO! Digite uma opção valida\033[m')
            time.sleep(4)

print(isso())