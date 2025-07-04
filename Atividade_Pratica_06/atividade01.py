import random
import string

def gerar_senha(tamanho: int) -> str:
    
    if tamanho < 1:
        return "Tamanho inválido!"


    caracteres = string.ascii_letters + string.digits + string.punctuation


    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


try:
    qtd = int(input("Informe o número de caracteres da senha: "))
    senha_gerada = gerar_senha(qtd)
    print("Senha gerada:", senha_gerada)
except ValueError:
    print("Por favor, digite um número inteiro válido.")