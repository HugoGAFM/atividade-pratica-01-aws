def calcular_imc():
    peso = float(input("Informe seu peso (kg): "))
    altura = float(input("Informe sua altura (m): "))
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")


print(calcular_imc())