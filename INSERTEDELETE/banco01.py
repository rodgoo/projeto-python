import sqlite3
from time import sleep

# Conectando banco de dados no código
conexao_banco = sqlite3.connect('meuBanco.db')
cursor = conexao_banco.cursor()

# Criando a tabela
cursor.execute("""CREATE TABLE IF NOT EXISTS cadastroCliente
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nomeUsuario TEXT NOT NULL,               
documento INTEGER NOT NULL,
telefone INTEGER NOT NULL)""")

while True:
    print('='*30)
    print('Olá! Seja bem vind@!')
    sleep(1)
    print('Ações possíveis com os dados: [adicionar] [excluir] [sair]')
    sleep(1.5)
    pergunta = input('O que deseja fazer? ')

    if pergunta == 'sair':
        print('[sair] O programa está sendo finalizado, até mais!')
        sleep(1)
        break
    
    # INSERT - Adicionando/Injetando/Alimentando dados no banco 
    elif pergunta == 'adicionar':
        print('='*30)
        nomeUsuario = input('Digite o seu primeiro nome:').strip().capitalize()
        
        if not nomeUsuario.isalpha() or not nomeUsuario:
            print('Este campo deve ser um texto, sem números ou caracteres especiais!')
            continue

        print('='*30)
        documento = input('Digite o número do seu documento (fictício)').strip()

        print('='*30)
        telefone = input('Digite o número de seu telefone (fictício):')
        print('='*30)

        try:
            # Injetando os dados no SQL
            dados_para_SQL = 'INSERT INTO cadastroCliente (nomeUsuario, documento, telefone) VALUES (?, ?, ?)'
            inserindoSQL = (nomeUsuario, documento, telefone)

            cursor.execute(dados_para_SQL,inserindoSQL)
            conexao_banco.commit()  
            print('Sucesso! Dados adicionados no banco de dados')
            sleep(1.5)
        
        except Exception as erro:
            print('='*30)
            print(f'Erro ao adicionar os dados no banco, dá uma olhada: {erro}')


    # DELETE - Excluindo registros do banco de dados
    elif pergunta == 'excluir':
        print('='*30)
        perguntaDelete = input('Digite o nome ou ID do usuário que deseja excluir:').capitalize()
        print('='*30)

        try:
            # Deletando dados do SQL
            deletando_do_SQL = 'DELETE FROM cadastroCliente WHERE nomeUsuario = ? OR id = ?'
            cursor.execute(deletando_do_SQL,(perguntaDelete, perguntaDelete))
            conexao_banco.commit()

            if cursor.rowcount > 0:
                print('Sucesso! dado excluído do banco de dados')
                print(f'[{nomeUsuario} saiu do chat] | não existe mais!')
                sleep(1.5)
            else:
                print(f'Opa! Esse dado: [{perguntaDelete}] não existe em sistema :/')
                sleep(1)
        
        except Exception as erro:
            print('='*30)
            print(f'Erro ao excluir dados do banco, vê aí: {erro}')
    else:
        print('Comando incorreto ou não reconhecido, tente novamente!')

# Fecha a conexão com o banco de dados, encerrando o circuito
conexao_banco.close()