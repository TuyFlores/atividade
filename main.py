idade = int(input("Digite sua idade:"))


if idade <= 0:
    print("Idade Invalida")

if idade <= 12:
    print("Criança")

if idade <= 13:
    print("Adolecente")

if idade <= 18:
    print("Adulto")

if idade >= 60:
    print("Idoso")