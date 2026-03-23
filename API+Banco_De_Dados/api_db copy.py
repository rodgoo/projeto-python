import requests


# --- USANDO E PEGANDO A API ---
def pegar_preco_atual():
    url = f"https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    dados = response.json()
    return dados
    