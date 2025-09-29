import random
import os

def gerar_cpf(quantidade, formatado):

    cpfs_numericos = []
    cpfs_formatados = []

    for i in range(quantidade):
        nine_digits = ''
        soma = 0
        countdown = 10

        for i in range(9):
            nine_digits += str(random.randint(0,9))

        for num in nine_digits: # Multiplica os 9 primeiros dígitos do CPF por uma contagem regressiva de 10 a 2
            soma += int(num)*countdown # soma todos eles
            countdown -= 1  

        rest_division = soma % 11 

        if rest_division < 2:
            first_digit = 0

        else:
            first_digit = 11 - rest_division

        soma = 0
        ten_digits = nine_digits + str(first_digit)
        countdown = 11

        for num in ten_digits: # # Multiplica os 10 primeiros dígitos do CPF por uma contagem regressiva de 11 a 2
            soma += int(num)*countdown # soma todos eles
            countdown -= 1

        rest_division = soma % 11

        if rest_division < 2:
            second_digit = 0

        else:
            second_digit = 11 - rest_division

        cpf = f'{nine_digits}{first_digit}{second_digit}'
        cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

        cpfs_formatados.append(cpf_formatado)
        cpfs_numericos.append(cpf)

    if formatado:
        return cpfs_formatados
    else:
        return cpfs_numericos



escolheu_quantidade = False

while escolheu_quantidade is False:
    try:
        quantidade = int(input('Quantos CPFs irá querer? '))
        if quantidade <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Você escolheu um número menor que um(1). Tente novamente.')
            continue
            
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Você não Digitou um número. Tente novamente.')
        continue
    escolheu_quantidade = True

escolheu_sera_formatado = False

while escolheu_sera_formatado is False:
    sera_formatado = input('Você vai querer que o(s) cpf(s) seja(m) formatado(s)? [S]im ou [N]ão : ')

    if sera_formatado.upper() == 'S':
        formatado = True
        escolheu_sera_formatado = True
    elif sera_formatado.upper() == 'N':
        formatado = False
        escolheu_sera_formatado = True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Você não escolheu uma das opções. Tente novamente')

print(f'{quantidade} CPF(s) abaixo:')
print(gerar_cpf(quantidade,formatado))














