dolar = 5.20
euro = 6.15

resultado = 0

def converterRealParaDolar(value1):
    return value1 / dolar

def converterRealParaEuro(value1):
    return value1 / euro

print("Conversor de Real para Dolar e Euro\n")
real = float(input("digite quantos reais você tem: "))

while True:
    value = input("Escolha para qual valor você quer converter\nDigite 1 Para Dolar | Digite 2 para Euro\n")
    
    if value == "1":
        resultado = converterRealParaDolar(real)
        print(f"A conversão de Real para Dólar deu: ${resultado:.2f}")
        break
    elif value == "2":
        resultado = converterRealParaEuro(real)
        print(f"A conversão de Real para Euro deu: €{resultado:.2f}")
        break
    else:
        print("Número ou caractere inválido! Digite apenas 1 ou 2.\n")

