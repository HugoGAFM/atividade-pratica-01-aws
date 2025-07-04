import json

def escrever_dados_json(nome_arquivo: str):
    
    pessoa = {
        "nome": "Lucas",
        "idade": 30,
        "cidade": "Porto Alegre"
    }

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados gravados em '{nome_arquivo}'.")
    except Exception as e:
        print("Erro ao escrever o arquivo JSON:", e)

def ler_dados_json(nome_arquivo: str):

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
        
        print("\n=== Dados da Pessoa ===")
        print(f"Nome: {dados.get('nome')}")
        print(f"Idade: {dados.get('idade')}")
        print(f"Cidade: {dados.get('cidade')}")

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print("Erro ao ler o arquivo JSON:", e)


nome_arquivo = "pessoa.json"
escrever_dados_json(nome_arquivo)
ler_dados_json(nome_arquivo)