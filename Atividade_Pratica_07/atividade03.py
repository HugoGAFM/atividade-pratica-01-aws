import csv

def ler_e_exibir_csv(nome_arquivo: str):
    
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            
            print("=== Dados das Pessoas ===")
            for linha in leitor:
                nome = linha['Nome']
                idade = linha['Idade']
                cidade = linha['Cidade']
                print(f"Nome: {nome} | Idade: {idade} | Cidade: {cidade}")

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print("Erro ao ler o arquivo CSV:", e)

# Executa a função
ler_e_exibir_csv("dados_pessoas.csv")