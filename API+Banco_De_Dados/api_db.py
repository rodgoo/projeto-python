import requests
import sqlite3
import time
from datetime import datetime

# --- CONFIGURAÇÕES ---
monitorMoedas = "monitorCriptomoedas.db"
moeda = "bitcoin"

# --- FUNÇÕES DE BANCO DE DADOS ---
def comecarFuncao():
    conn = sqlite3.connect(monitorMoedas)
    cursor = conn.cursor()
    # Criamos a tabela com TIMESTAMP para análise temporal depois
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS historico_precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moeda TEXT NOT NULL,
            tipomoeda TEXTO NOT NULL,
            preco_real REAL NOT NULL DEFAULT 0,
            preco_dolar REAL NOT NULL DEFAULT 0,
            data_hora TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def salvar_precoReal(moeda, preco_real):
    conn = sqlite3.connect(monitorMoedas)
    cursor = conn.cursor()
    horaAgora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        INSERT INTO historico_precos (moeda, tipomoeda, preco_real, data_hora)
        VALUES (?, 'Real', ?, ?)
    ''', (moeda, preco_real, horaAgora))
    
    conn.commit()
    conn.close()

def salvar_precoDolar(moeda, preco_dolar):
    conn = sqlite3.connect(monitorMoedas)
    cursor = conn.cursor()
    horaAgora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        INSERT INTO historico_precos (moeda, tipomoeda, preco_dolar, data_hora)
        VALUES (?, 'Dolar', ?, ?)
    ''', (moeda, preco_dolar, horaAgora))
    
    conn.commit()
    conn.close()

def menu():

    while True: 
        print('-'*30)
        print('Sistema de Monitoramento')
        print('-'*30)
        escolha = input('Qual o tipo de moeda? [BRL] ou [USD]: ').upper()
        comecarFuncao()

        if escolha not in ['BRL', 'USD']:
            print('Opção não reconhecida. Escolha BRL ou USD para começar!')
            time.sleep(1.5)
            continue

        if escolha == 'BRL':
            # --- FUNÇÃO DA API ---
            def pegar_preco_atual(coin_id):
                try:
                    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=brl"
                    response = requests.get(url)
                    dados = response.json()
                    return dados[coin_id]['brl']
                except Exception as e:
                    print(f"Erro na API: {e}")
                    return None
                
                
            print('-'*30)
            print("🚀 Monitor iniciado em [BRL]: Real! Pressione Ctrl+C para parar.")
            
            try:
                while True:
                    preco_real = pegar_preco_atual(moeda)
                    if preco_real:
                        salvar_precoReal(moeda, preco_real)
                        agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(f'{agora} | {moeda.upper()} com o valor: R$: {preco_real} | Valor registrado no banco de dados!')
                    
                    # Espera 60 segundos para a próxima consulta (evita bloqueio da API)
                        time.sleep(60) 

            except KeyboardInterrupt:
                print("\nMonitoramento encerrado pelo usuário.")
                print('-'*30)

            except Exception as erro:
                print(f'Um erro foi encontrado! ERRO: {erro}')
                
        elif escolha == 'USD':
            # --- FUNÇÃO DA API ---
            def pegar_preco_atual(coin_id):
                try:
                    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
                    response = requests.get(url)
                    dados = response.json()
                    return dados[coin_id]['usd']
                except Exception as e:
                    print(f"Erro na API: {e}")
                    return None

            # --- LOOP DE EXECUÇÃO ---
            print('-'*30)
            print("🚀 Monitor iniciado em [USD]: Dólar! Pressione Ctrl+C para parar.")
            
            try:
                while True:
                    preco_dolar = pegar_preco_atual(moeda)
                    if preco_dolar:
                        salvar_precoDolar(moeda, preco_dolar)
                        agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(f'{agora} | {moeda.upper()} com o valor: U$: {preco_dolar} | Valor registrado no banco de dados!')
                    # Espera 60 segundos para a próxima consulta (evita bloqueio da API)
                    time.sleep(60) 

            except KeyboardInterrupt:
                print("\nMonitoramento encerrado pelo usuário.")
                print('-'*30)  

            except Exception as erro:
                print(f'Um erro foi encontrado! ERRO: {erro}')
print()    

if __name__ == '__main__':
    menu()