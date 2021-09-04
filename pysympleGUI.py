from PySimpleGUI import PySimpleGUI as sg

# Layyout
sg.theme('reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar'), sg.Button('Cancelar')]
]
# Janela
janela = sg.Window('Tela de login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'fabio' and valores['senha'] == '123456':
            sg.popup('Bem vindo!')
        else:
            sg.popup('Login incorreto, tente novamente!')

    if eventos in (sg.WIN_CLOSED, 'Cancelar'):
        break