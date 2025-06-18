
def calcularVolume (value1, value2, value3):
    return value1 * value2 * value3


comprimento = int(input("digite o valor do comprimento: "))
altura = int(input("digite o valor da altura: "))
largura = int(input("digite o valor da largura: "))

resultado = calcularVolume(comprimento, altura, largura)

print("o Volume é: " + str(resultado) + " cm³" )
