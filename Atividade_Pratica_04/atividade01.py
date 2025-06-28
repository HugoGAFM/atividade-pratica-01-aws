def calculadora():
    while True:
        try:
            
            num1 = float(input("Digite o primeiro número: "))
            
            
            num2 = float(input("Digite o segundo número: "))
            
            
            operacao = input("Digite a operação (+, -, *, /): ")

        
            if operacao not in ['+', '-', '*', '/']:
                print("Operação inválida. Tente novamente.")
                continue

            
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Não é possível dividir por zero.")
                resultado = num1 / num2

            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            break

        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")


calculadora()