print ("---Calculadora---")
n1 = float(input("Primeiro numero"))
n2 = float(input("Segundo numero"))
op = input("Operação (+, -, *,/):")

if op == "+":
    print(f"Resultado: {n1 + n2}")

elif op == "-":
    print(f"Resultado: {n1 - n2}")

elif op == "*":
    print(f"Resultado: {n1 * n2}")

elif op == "/":
    if n2 != 0:
    print(f"Resultado: {n1 / n2:.2f}")

else:
    print("erro! Não pode dividir por zero!")

else:
    print("Operação invalida!")
   

