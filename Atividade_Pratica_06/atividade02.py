import requests

def gerar_usuario_aleatorio():
    try:
        resposta = requests.get("https://randomuser.me/api/")
        if resposta.status_code == 200:
            dados = resposta.json()
            usuario = dados['results'][0]

            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']

            print("=== Perfil Gerado ===")
            print(f"Nome: {nome}")
            print(f"E-mail: {email}")
            print(f"País: {pais}")
        else:
            print("Erro ao acessar a API. Código de status:", resposta.status_code)
    except Exception as e:
        print("Erro durante a requisição:", e)

gerar_usuario_aleatorio()