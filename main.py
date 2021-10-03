from simples2 import *
from tkinter import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Analise de rede - Net2Phone")
root.geometry("800x600+500+100")
"""Define reajuste de janela"""
root.resizable(False, False)


"""Variaveis"""

"""Lista de portais para box"""
portais = (["Portal 1", "Portal 2", "Portal 3", "Portal 4", "Portal 5", "Portal 6", 
                "Portal 7", "Portal 8", "Portal 9", "Portal 10", "Portal 11", "Portal 12"])

"""Dicionario de portais com proxy para uso:"""
portal_entrada = {
        "Portal 1": "proxy.idtbrasilhosted.com",
        "Portal 2": "proxy2.idtbrasilhosted.com",
        "Portal 3": "proxy3.idtbrasilhosted.com",
        "Portal 4": "proxy4.idtbrasilhosted.com",
        "Portal 5": "proxy5.idtbrasilhosted.com",
        "Portal 6": "proxy6.idtbrasilhosted.com",
        "Portal 7": "proxy7.idtbrasilhosted.com",
        "Portal 8": "proxy8.idtbrasilhosted.com",
        "Portal 9": "proxy9.idtbrasilhosted.com",
        "Portal 10": "proxy10.idtbrasilhosted.com",
        "Portal 11": "proxy11.idtbrasilhosted.com",
        "Portal 12": "proxy12.idtbrasilhosted.com",
    }

"""Modulos"""


def error_tk():
    """Modulo ERRO"""
    
    print("Opção invalida, selecione um Portal!")

def op_check(event):

    """Modulo para validação"""

    comman, resp, resp2, resp3, portal_in, portal_out = events()
    print(comman)

    if portal_in == str :

        respos(comman, resp, resp2, resp3, portal_out)
    else:
        error_tk()

def events():
    comman = botao
    resp = valor_check.get()
    resp2 = valor_check2.get()
    resp3 = valor_check3.get()
    portal_in = combobox1.get()
    portal_out = portal_entrada[portal_in]
    return comman,resp,resp2,resp3,portal_in,portal_out

def respos(comman, resp, resp2, resp3, portal_out):
    if resp == 1 and comman == None:
        file_TRACERT(portal_out)

    if resp2 == 1 and  comman == None:
        file_DNS()

    if resp3 == 1 and comman == None:
        sip_alg()

"""Icone"""
root.iconbitmap("images/icon/net2phone.ico")


"""Label"""
t1 = ttk.Label(root, 
    relief="solid").place(
        x = 10, y = 5, width=780, height=200)

t1 = ttk.Label(root, 
    relief="solid").place(
        x = 650, y = 30, width=120, height=160)

t2 = ttk.Label(root, 
    text="ANALISE DE REDE VOIP - github.com/fabiohcsouza/Analise_rede_VoIP",
    background="#00008B",
    foreground="white",
    anchor=CENTER).place(
        x = 200, y = 10, width=400, height=20)

"""Label"""
t3 = ttk.Label(root, 
    text="Escolha o Portal",
    background="#C0C0C0",
    foreground="black",
    font="verdana 10",
    anchor=CENTER).place(
        x = 20, y = 45, width=114, height=20)

t4 = ttk.Label(root, 
    text="-",
    font="verdana 10",
    anchor=CENTER).place(
        x = 138, y = 45, width=10, height=20)


"""ComboBox"""

combobox_var = tk.StringVar()
combobox_var.trace('w',op_check)
combobox1 = ttk.Combobox(root, 
    textvariable=combobox_var)
combobox1['values'] = portais
combobox1.place(x = 151, y = 45, width=100, height=20)

t4 = ttk.Label(root, 
    text="-",
    font="verdana 10",
    anchor=CENTER).place(
        x = 260, y = 45, width=10, height=20)

"""Check Button"""
valor_check = IntVar()
check = ttk.Checkbutton(root,
    text="TRACERT",
    variable=valor_check,
    command = op_check,).place(
        x = 20, y = 80, width=100, height=20)

valor_check2 = IntVar()
check1 = ttk.Checkbutton(root,
    text="DNS Google",
    variable=valor_check2,
    command = op_check,).place(
        x = 98, y = 80 , width=100, height=20)

valor_check3 = IntVar()
check2 = ttk.Checkbutton(root,
    text="SIP ALG",
    variable=valor_check3,
    command = op_check,).place(
        x = 190, y = 80 , width=100, height=20)

"""Label"""

t3 = ttk.Label(root, 
    text="Ping Gateway",
    background="#C0C0C0",
    foreground="black",
    font="verdana 10",
    anchor=CENTER).place(
        x = 20, y = 110, width=98, height=20)

"""Entrada"""
ip_gat = StringVar()
entrada = ttk.Entry(root,
    textvariable=ip_gat).place(
        x = 135, y = 110, width=100, height=20)

"""Label"""
t4 = ttk.Label(root, 
    text="-",
    font="verdana 10",
    anchor=CENTER).place(
        x = 122, y = 110, width=10, height=20)

"""Label"""
t3 = ttk.Label(root, 
    text="IP Host",
    background="#C0C0C0",
    foreground="black",
    font="verdana 10",
    anchor=CENTER).place(
        x = 250, y = 110, width=80, height=20)

"""Label"""
t4 = ttk.Label(root, 
    text="-",
    font="verdana 10",
    anchor=CENTER).place(
        x = 335, y = 110, width=10, height=20)

"""Entrada"""
ip_gat = StringVar()
entrada = ttk.Entry(root,
    textvariable=ip_gat).place(
        x = 350, y = 110, width=100, height=20)

"""Botao"""
botao = ttk.Button(
    root, 
    text="Executar",
    command=op_check)

botao.place(
        x = 20, y = 170, width=100, height=20)

"""Botao"""
botao = ttk.Button(
    root, 
    text="Parar",
    command = lambda: op_check("n"),).place(
        x = 140, y = 170, width=100, height=20)

root.mainloop()

