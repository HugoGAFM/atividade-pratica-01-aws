notas = []  

while True:
    entrada = input("Digite as suas Notas: \n Digite ''sair'' para fazer a sua média. ")

    if entrada.lower() == 'sair':
        break

    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print("digite um número válido.")


if notas:
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")