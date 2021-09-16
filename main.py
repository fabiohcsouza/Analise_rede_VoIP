from tkinter.font import BOLD
from simples2 import *
from tkinter import *
from tkinter import Tk, ttk



root = Tk()
root.title("Analise de rede - Net2Phone")
root.geometry("800x600+500+100")
"""Define reajuste de janela"""
root.resizable(False, False)


"""Variaveis"""

"""Modulos"""

def op_check(comman):

    resp = valor_check.get()
    resp2 = valor_check2.get()
    resp3 = valor_check3.get()

    if resp == 1 and comman == "s":
        sip_alg()
    else:
        ()


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
combobox_var = StringVar()
combobox = ttk.Combobox(root, 
    textvariable=combobox_var).place(
        x = 151, y = 45, width=100, height=20)

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
    command = lambda: op_check("s"),).place(
        x = 20, y = 170, width=100, height=20)

"""Botao"""
botao = ttk.Button(
    root, 
    text="Parar",
    command = lambda: op_check("n"),).place(
        x = 140, y = 170, width=100, height=20)



root.mainloop()

