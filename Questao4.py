# Função para encontrar o menor valor em uma lista
def encontrar_menor(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

# Função para encontrar o maior valor em uma lista
def encontrar_maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

# Entrada dos números como uma lista de strings separadas por espaço
numeros_lista = input("Digite uma lista de números separados por espaço: ")

# Convertendo a entrada em números inteiros
numeros = [int(x) for x in numeros_lista.split()]

# Verificando se a lista está vazia
if len(numeros) == 0:
    print("Sua lista está vazia")
else:
    # Chamando as funções para encontrar o menor e o maior valor
    num_menor = encontrar_menor(numeros)
    num_maior = encontrar_maior(numeros)
    
    # Exibindo o menor e o maior valor
    print("O menor valor é {}.".format(num_menor))
    print("O maior valor é {}.".format(num_maior))