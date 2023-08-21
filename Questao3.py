# Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.

numero = int(input("Digite um número: "))

print("Aqui estão os números pares de 0 até {}:" .format(numero))

for i in range(0, numero+1, 2):
    print(i)
    