import math

numero_1 = float(input("Escreva o primeiro numero:"))
operacao = input('Escolha o número da operação: \n 1 - Soma \n 2 - Subtracao, \n 3 - Multiplicacao \n 4 - Divisão \n 5 - Potenciacao \n 6 - Raiz quadrada \n 7 - Logaritmo \n')

if operacao == '1':
    numero_2 = float(input('Escreva o segundo numero: '))
    resultado = numero_1 + numero_2
    print(f'{numero_1} + {numero_2} = {resultado}.')
    #print(f'Seu resultado é: {resultado}.')
elif operacao == '2':
    numero_2 = float(input('Escreva o segundo numero: '))
    resultado = numero_1 - numero_2
    print(f'{numero_1} - {numero_2} = {resultado}.')
    #print(f'Seu resultado é: {resultado}.')
elif operacao == '3':
    numero_2 = float(input('Escreva o segundo numero: '))
    resultado = numero_1 * numero_2
    print(f'{numero_1} * {numero_2} = {resultado}.')
    #print(f'Seu resultado é: {resultado}.')
elif operacao == '4':
    numero_2 = float(input('Escreva o segundo numero: '))
    resultado = numero_1 / numero_2
    print(f'{numero_1} / {numero_2} = {resultado}.')
    #print(f'Seu resultado é: {resultado}.')
elif operacao == '5':
    numero_2 = float(input('Escreva o segundo numero: '))
    resultado = numero_1 ** numero_2
    print(f'{numero_1} elevado a {numero_2} = {resultado}.')
    #print(f'Seu resultado é: {resultado}.')
elif operacao == '6':
    #resultado = numero_1 ** (1/2)
    resultado = math.sqrt(numero_1)
    print(f'({numero_1})² = {resultado}.')
    #print(f'Seu resultado é: {resultado}.')
elif operacao == '7':
    resultado = math.log10(numero_1)
    print(f'Log de {numero_1} = {resultado}.')
    #print(f'Seu resultado é: {resultado}.')
else:
    print('Operação inválida. Selecione um número de 1 a 7.')