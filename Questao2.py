# Crie um programa que determine se um número inserido pelo usuário é par ou ímpar

numero = int(input("Digite um numero:"))

if numero % 2 == 0:
    print("O numero {} é par.".format(numero))
else:
    print("O numero {} é ímpar." .format(numero))
