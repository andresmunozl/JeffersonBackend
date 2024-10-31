
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))


imc = calcular_imc(peso, altura)


print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")


if imc < 18.5:
    print("Estás por debajo del peso normal.")
elif 18.5 <= imc < 24.9:
    print("Tienes un peso normal.")
elif 25 <= imc < 29.9:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")
