# Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número

def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

try:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é {resultado}")
except ValueError:
    print("Por favor, digite um número válido.")
    