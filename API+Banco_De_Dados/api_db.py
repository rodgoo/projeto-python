import requests
import sqlite3
import time
from datetime import datetime

# --- CONFIGURAÇÕES ---
monitorMoedas = "./databases/monitorMoedas.db"
moeda = "bitcoin"

# --- FUNÇÕES DO BANCO DE DADOS ---
def comecarFuncao():
    conn = sqlite3.connect('./databases/monitorMoedas.db')
    cursor = conn.cursor()
    
    # Tabela criada com timestamp 
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS historico_precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moeda TEXT NOT NULL,
            tipomoeda TEXTO NOT NULL,
            preco REAL NOT NULL DEFAULT 0,
            data_hora TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def salvar_Preco(moeda, tipomoeda, preco):
    conn = sqlite3.connect(monitorMoedas)
    cursor = conn.cursor()
    horaAgora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        INSERT INTO historico_precos (moeda, tipomoeda, preco, data_hora)
        VALUES (?, ?, ?, ?)
    ''', (moeda, tipomoeda, preco, horaAgora))
    
    conn.commit()
    conn.close()

def menu():

    while True: 
        print('-'*30)
        print('Sistema de Monitoramento')
        print('-'*30)
        escolha = input('Qual o tipo de moeda? [BRL] ou [USD]: ').lower()
        comecarFuncao()

        if escolha not in ['brl', 'usd']:
            print('Opção não reconhecida. Escolha BRL ou USD para começar!')
            time.sleep(1.5)
            continue


        # --- USANDO E PEGANDO A API ---
        def pegar_preco_atual(coin_id):
            try:
                url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={escolha}"
                response = requests.get(url)
                dados = response.json()
                return dados[coin_id][f'{escolha}']
            except Exception as e:
                print(f"Erro na API: {e}")
                return None
            
            
        print('-'*30)

        moedaNomeExtended = 'Real' if escolha == 'brl' else 'Dolar'
        moedaExtensao = 'R$' if escolha == 'brl' else 'US$'

        print(f"🚀 Monitor iniciado em [{escolha.upper()}]: {moedaNomeExtended} | Pressione Ctrl+C para parar.")
        

        try:
            while True:
                preco = pegar_preco_atual(moeda)
                if preco:
                    salvar_Preco(moeda, moedaNomeExtended, preco)
                    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(f'{agora} | {moeda.upper()} com o valor: {moedaExtensao}: {preco} | Valor registrado no banco de dados!')
                
                # Espera 60 segundos para a próxima consulta (evitando bloqueio da API)
                    time.sleep(60) 

        except KeyboardInterrupt:
            print("\nMonitoramento encerrado pelo usuário.")

        except Exception as erro:
            print(f'Um erro foi encontrado! ERRO: {erro}')
                
print()    

if __name__ == '__main__':
    menu()  