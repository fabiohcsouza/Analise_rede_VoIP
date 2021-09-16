from simples2 import *
from tkinter import *
from tkinter import Tk, ttk



root = Tk()
root.title("Analise de rede - Net2Phone")

"""Variaveis"""

"""Modulos"""

def op_check(comman):

    resp = valor_check.get()

    if resp == 1 and comman == "s":
        sip_alg()
    else:
        ()

"""Define o tamanho da janela"""
root.geometry("960x720+500+100")

"""Icone"""
root.iconbitmap("images/icon/net2phone.ico")

"""Define reajuste de janela"""
root.resizable(True, True)

"""Definir limite mine max tam tela"""
#root.minsize("800x600")
#root.maxsize("960x720")

"""Label"""
label1 = Label(root,
                    text="Bem Vindo!",
                    background="#00aa00",
                    foreground="#000000",
                    font="verdana 16 bold",
                    width=70)

label2 = ttk.Label(root,
                    text="Selecione o Portal",
                    foreground="#000000",
                    font="verdana 10 bold",
                    border= 1, #tam borda
                    relief="solid", #tipo borda
                    width=50, #Largura
                    #justify=LEFT,
                    anchor=W, #Posição com base em Norte, Sul, Leste e Oeste
                    )

label3 = ttk.Label(root,
                    text="Esse é meu Label",
                    foreground="#00aa00",
                    font="verdana 10 bold",
                    border = 1, #tam borda
                    relief="solid", #tipo borda
                    width=36, #Largura
                    #padx=10, #outra forma so que em pixiel
                    #pady=10,
                    justify=LEFT, #Ajustar texto
                    anchor=W
                    )
                

"""Check Button"""
valor_check = IntVar()
check = ttk.Checkbutton(
    root,
    text="SIP ALG",
    variable=valor_check,
    command = op_check,
)

"""Botao"""

botao = ttk.Button(
    root, 
    text="Executar",
    command = lambda: op_check("s"),
)

"""ComboBox"""

combobox_var = StringVar()
combobox = ttk.Combobox(root, textvariable=combobox_var)

""".PACK(Define a orde e ativa os bang ai)"""
label1.pack()
label2.pack(), combobox.pack()
label3.pack()
check.pack()
botao.pack()


root.mainloop()