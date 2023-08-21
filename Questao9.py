# Escreva um programa que leia uma lista de nomes e retorne apenas os nomes que começam com a letra 'A'.

def main():
    lista_nomes = input("Digite a lista de nomes separados por vírgula: ").split(',')
    
    nomes_filtrados = [nome for nome in lista_nomes if nome.strip().startswith('A')]
    
    print("Nomes que começam com a letra 'A':")
    for nome in nomes_filtrados:
        print(nome)

if __name__ == "__main__":
    main()



