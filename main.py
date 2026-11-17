nome = input("Digite seu Nome:")
peso = float(input("Digite seu peso:"))
altura =  float(input("Digite sua altura:"))


imc = peso / (altura * altura)

if imc <= 18.5:
    print(f"{nome} está abaixo do peso")

elif imc <= 25:
    print(f"{nome} está no peso Normal")

elif imc <= 30:
    print(f"{nome} está sobrePeso")

elif imc >= 30:
    print(f"{nome} está obeso")