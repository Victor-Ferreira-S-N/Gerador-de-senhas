"""
Gerador de senhas em janela gráfica

"""
from random import choice
import PySimpleGUI as sg
from pyperclip import copy

sg.theme('Darkblue3')

layout = [
    [sg.Text('Quantidade de caracteres: '), sg.Push(),
     sg.Combo([i for i in range(4, 21)], readonly=True, default_value=8, key='-QUANTIDADE-')],
    [sg.Text('Deseja caracteres especiais: '), sg.Push(), sg.Radio('Sim', '1', default=False, key='-SIM1-'),
     sg.Radio('Não', '1', default=True, key='-NAO1-')],
    [sg.Text('Deseja números na senha: '), sg.Push(), sg.Radio('Sim', '2', default=False, key='-SIM2-'),
     sg.Radio('Não', '2', default=True, key='-NAO2-')],
    [sg.Push(), sg.Button('Gerar Senha', key='-GERAR-'), sg.Push()],
    [sg.Text('Sua senha é: '), sg.Text('', key='-OUTPUT-'), sg.Push(), sg.Button('Copiar senha', key='-COPIAR-')]
]

window = sg.Window('Gerador de senhas', layout, font=('Arial, 12'), size=(500,200))

letras = 'abcdefghijklmnopqrstuvwxyz'
LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
especiais = """`~!@#$%^&*()-_=+/*[{]}|\:;"'<,>.?"""
numeros = '0123456789'

possibilidades = [letras, LETRAS]
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    possibilidades = [letras, LETRAS]
    senha_lista = []

    if event == '-GERAR-':

        if values['-QUANTIDADE-'] is not None:
            qtd = values['-QUANTIDADE-']

        if values['-SIM1-']:
            possibilidades.append(especiais)


        if values['-SIM2-']:
            possibilidades.append(numeros)

        for q in range(qtd):
            tipo = choice(possibilidades)
            caracter = choice(tipo)
            senha_lista.append(caracter)

        senha_final = ''.join(senha_lista)
        window['-OUTPUT-'].update(senha_final)

    if event == '-COPIAR-':
        try:
            copy(senha_final)
            sg.popup('Senha copiada!', background_color='Green', font='Arial, 12', text_color='White',
                     button_type=5, title='')
        except:
            sg.popup('Não há senha gerada!', background_color='Orange', font='Arial, 12', text_color='Black',
                     button_type=5, title='')


window.close()

