# Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O programa
# deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do computador
# e determinar o vencedor.

import random

def usuario_escolhe():
    while True:
        user_choice = input("Escolha Pedra, Papel ou Tesoura: ").strip().lower()
        if user_choice in ["pedra", "papel", "tesoura"]:
            return user_choice
        else:
            print("Escolha inválida. Por favor, escolha entre Pedra, Papel ou Tesoura.")

def pc_escolhe():
    choices = ["pedra", "papel", "tesoura"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"
    elif (
        (user_choice == "pedra" and computer_choice == "tesoura")
        or (user_choice == "papel" and computer_choice == "pedra")
        or (user_choice == "tesoura" and computer_choice == "papel")
    ):
        return "Você venceu!"
    else:
        return "Computador venceu!"

def main():
    print("Bem-vindo ao Pedra, Papel e Tesoura!")

    user_choice = usuario_escolhe()
    computer_choice = pc_escolhe()

    print(f"Você escolheu: {user_choice}")
    print(f"Computador escolheu: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    print(winner)

if __name__ == "__main__":
    main()