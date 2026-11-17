import random

print("=" * 35)
print("PEDRA, PAPEL OU TESOURA")
print("=" * 35)

opcoes = ["pedra", "papel", "tesoura"]
computador = random.choice(opcoes)


jogador = input("\nEscolhas (pedra/papel/tesoura):") .lower ()

print(f"\nVocê: {jogador}")
print(f"Computador: {computador}")

if jogador == computador:
    print("\nEmpate!")
elif jogador == "pedra" and computador == "tesoura" :
    print("Você ganhou!")
elif jogador == "papel" and computador == "pedra" :
    print("Voce ganhau!")
elif jogador == "tesoura" and computador == "papel" :
    print("Você ganhou!")

else:
    print("\nVocê perdeu!")


