# Faça um programa que determine se um número é primo ou não.
num = int(input("Digite um número inteiro: "))

if num <= 1:
    primo = False
else:
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break

if primo:
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
