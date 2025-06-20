
distancia = float(input("digite quantos KM's foram andados:"))

litragem = float(input("Digite quantos litros de gasolina foram gastos:"))

def calculoConsumo(value1, value2):
    return value1 / value2


resultado = calculoConsumo(distancia, litragem)

print("você andou " + str(distancia)+ "KM, gastou " + str(litragem) + f"L e o consumo médio nesse periodo foi de {resultado:.2f}KM/L")