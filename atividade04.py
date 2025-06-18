def produtoComprado (value1, value2):
    return value1 * value2


nomeDoProduto = input("qual o produto que você deseja comprar? ")
preco = float(input("quanto ele custa? "))
quantidade = int(input("quantos deles irá querer comprar? "))
resultado = produtoComprado(preco, quantidade)

print("o seu produto é: " + nomeDoProduto)
print("o preço do produto é: " + str(preco))
print("a quantidade que você comprou desse produto é: " + str(quantidade))
print("esse produto custará para você: R$" + str(resultado)) 

