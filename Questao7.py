# Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

def fibonacci_sequence(n):
    sequence = [0, 1]
    
    while sequence[-1] + sequence[-2] <= n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence

def main():
    try:
        limit = int(input("Insira um valor limite para a sequência de Fibonacci: "))
        if limit < 0:
            print("Por favor, insira um valor não negativo.")
        else:
            fib_sequence = fibonacci_sequence(limit)
            print("Sequência de Fibonacci até", limit, ":", fib_sequence)
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    main()