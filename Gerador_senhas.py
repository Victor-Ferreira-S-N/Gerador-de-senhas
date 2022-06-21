""" Gerador de senhas """
from random import choice

letras = 'abcdefghijklmnopqrstuvwxyz'
LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
especiais = """`~!@#$%^&*()-_=+/*[{]}|\:;"'<,>.?"""
numeros = '0123456789'

possibilidades = [letras, LETRAS]
senha_lista = []

print('-='*20)
print(f'{"Gerador de senhas":^40}')
print('-='*20)

while True:
    try:
        qtd = int(input('Digite a quantidade de caracteres que você quer para a senha: \n'))
        if qtd > 0:
            break
        else:
            print('Resposta inválida. Digite números maiores que zero.')
    except:
        print('Resposta inválida. Digite apenas números.')

while True:
    spc = input('Deseja caracteres especiais na senha? [1-Sim] [2-Não]\n')
    if spc.lower() in ['sim', '1']:
        possibilidades.append(especiais)
        break
    elif spc.lower() in ['não', 'nao', '2']:
        spc = None
        break
    else:
        print('Resposta inválida.')

while True:
    num = input('Deseja números na senha? [1-Sim] [2-Não]\n')
    if num.lower() in ['sim', '1']:
        possibilidades.append(numeros)
        break
    elif num.lower() in ['não', 'nao', '2']:
        num = None
        break
    else:
        print('Resposta inválida.')

for q in range(qtd):
    tipo = choice(possibilidades)
    caracter = choice(tipo)
    senha_lista.append(caracter)

senha_final = ''.join(senha_lista)

print(f'Sua senha é: \n{senha_final}')