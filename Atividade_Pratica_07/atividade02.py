import csv

def escrever_dados_csv(nome_arquivo: str):
    

    pessoas = [
        {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
        {"Nome": "Carlos", "Idade": 34, "Cidade": "Belo Horizonte"},
        {"Nome": "Marina", "Idade": 22, "Cidade": "Curitiba"},
        {"Nome": "João", "Idade": 41, "Cidade": "Recife"}
    ]


    campos = ["Nome", "Idade", "Cidade"]

    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=campos)
            writer.writeheader() 
            writer.writerows(pessoas)

        print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
    except Exception as e:
        print("Erro ao escrever o arquivo CSV:", e)


escrever_dados_csv("dados_pessoas.csv")
