from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Não considera anos bissextos

    return idade_dias

print(calcular_idade_em_dias(20))