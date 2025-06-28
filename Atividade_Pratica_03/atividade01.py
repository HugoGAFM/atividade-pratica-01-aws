def compararIdade(value1):
    
    if value1 >= 12:
        resultado = "O(a) usuário(a) é um(a) criança."
    elif value1 >= 17:
        resultado = "O(a) usuário(a) é um(a) adolescente"
    elif value1 >= 59:
        resultado = "O(a) usuário(a) é um(a) adulto(a)"
    elif value1 > 60:
        resultado = "O(a) usuário(a) é um(a) idoso(a)"
    else:
        resultado = "Valor incorreto para a aplicação."

    return resultado



idade = int(input("Digite a sua Idade."))

print(compararIdade(idade))

