import requests
from datetime import datetime

def consultar_cotacao(moeda: str):
    
    moeda = moeda.strip().upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()

            chave = f"{moeda}BRL"
            if chave not in dados:
                print("Moeda não encontrada. Verifique o código informado.")
                return

            cotacao = dados[chave]
            nome = cotacao.get("name", "N/A")
            valor_atual = cotacao.get("bid", "N/A")
            valor_maximo = cotacao.get("high", "N/A")
            valor_minimo = cotacao.get("low", "N/A")
            timestamp = int(cotacao.get("timestamp", 0))
            data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

            print(f"\n=== Cotação de {nome} ===")
            print(f"Valor atual: R$ {valor_atual}")
            print(f"Valor máximo do dia: R$ {valor_maximo}")
            print(f"Valor mínimo do dia: R$ {valor_minimo}")
            print(f"Última atualização: {data_hora}")
        else:
            print("Erro ao acessar a API. Código de status:", resposta.status_code)
    except Exception as e:
        print("Erro durante a requisição:", e)

codigo_moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ")
consultar_cotacao(codigo_moeda)