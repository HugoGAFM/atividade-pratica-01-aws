import requests

def consultar_endereco_por_cep(cep: str):
    
    cep = cep.strip().replace("-", "")
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Certifique-se de digitar 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" in dados:
                print("CEP não encontrado.")
            else:
                print("\n=== Endereço Encontrado ===")
                print(f"Logradouro: {dados.get('logradouro', '-')}")
                print(f"Bairro: {dados.get('bairro', '-')}")
                print(f"Cidade: {dados.get('localidade', '-')}")
                print(f"Estado: {dados.get('uf', '-')}")
        else:
            print("Erro na consulta. Código:", resposta.status_code)
    except Exception as e:
        print("Erro durante a requisição:", e)

cep_usuario = input("Digite o CEP (somente números): ")
consultar_endereco_por_cep(cep_usuario)