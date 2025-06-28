def classificar_numeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print("\n--- Resultado final ---")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

classificar_numeros()