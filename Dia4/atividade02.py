def produtoDesconto(valor, percentual):
    desconto = valor * (percentual / 100)
    return valor - desconto


nomeDoProduto = input("qual o produto que você deseja comprar? ")
preco = float(input("quanto ele custa? "))
desconto = int(input("qual o desconto desse produto? "))


resultado = produtoDesconto(preco, desconto)

print("\no produto que você comprou foi: " + nomeDoProduto)
print(f"o preço original desse produto foi: R${preco:.2f}")
print("O desconto do produto foi: " + str(desconto) + "%")
print(f"esse produto com desconto fica: R${resultado:.2f}")