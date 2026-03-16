import sqlite3
from time import sleep

# Conectando banco de dados no código
conexao_banco = sqlite3.connect('meuBanco.db')
cursor = conexao_banco.cursor()

# Criando a tabela
cursor.execute("""CREATE TABLE IF NOT EXISTS cadastroCliente
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nomeUsuario TEXT NOT NULL,               
documento INTEGER NOT NULL UNIQUE,
telefone INTEGER NOT NULL UNIQUE)""")

#Definindo a regra de negócio
def adicionarDado(nomeUsuario,documento,telefone):
    cursor.execute('INSERT INTO cadastroCliente (nomeUsuario, documento, telefone) VALUES (?, ?, ?)',(nomeUsuario,documento,telefone))
    conexao_banco.commit()

def listarDados():
    cursor.execute('SELECT * FROM cadastroCliente')
    dados = cursor.fetchall()
    for dados in dados:
        id,nomeUsuario,documento,telefone
        print(f"""
            ID: {id}
            Nome: {nomeUsuario}
            CPF: {documento}
            Contato: {telefone}
            """)
        print('\n')

def atualizarDadoNome(nomeUsuario):
    cursor.execute("""
                   UPDATE cadastroCliente SET nomeUsuario = ?
                   WHERE id = ?
                   """,(nomeUsuario))
    conexao_banco.commit()

def atualizarDadoDocumento(documento):
    cursor.execute("""
                   UPDATE cadastroCliente SET telefone = ?
                   WHERE id = ?
                   """,(documento))
    conexao_banco.commit()

def atualizarDadoTelefone(telefone):
    cursor.execute("""
                   UPDATE cadastroCliente SET telefone = ?
                   WHERE id = ?
                   """,(telefone))
    conexao_banco.commit()

def deletarDado(nomeUsuario, id):
    cursor.execute('DELETE FROM cadastroCliente WHERE nomeUsuario = ? OR id = ?',(nomeUsuario,id,))
    conexao_banco.commit()


while True:
    print('='*30)
    print('Olá! Seja bem vind@!')
    sleep(1)
    print('Ações possíveis com os dados: [adicionar] [excluir] [listar] [atualizar] [sair]')
    sleep(1.5)
    pergunta = input('O que deseja fazer? ')

    if pergunta == 'sair':
        print('[sair] O programa está sendo finalizado, até mais!')
        sleep(1)
        break
    
    # INSERT - Adicionando/Injetando/Alimentando dados no banco 
    elif pergunta == 'adicionar':
        print('='*30)
        nomeUsuario = input('Digite o seu primeiro nome: ').strip().capitalize()
        
        if not nomeUsuario.isalpha() or not nomeUsuario:
            print('Este campo deve ser um texto, sem números ou caracteres especiais!')
            continue

        print('='*30)
        documento = input('Digite o número do seu documento (fictício)(único): ').strip()

        print('='*30)
        telefone = input('Digite o número de seu telefone (fictício)(único): ')
        print('='*30)

        try:
            # Injetando os dados no SQL
            adicionarDado(nomeUsuario,documento,telefone)
            print('Sucesso! Dado adicionado!')
        
        except Exception as erro:
            print('='*30)
            print(f'Erro ao adicionar os dados no banco, dá uma olhada: {erro}')

        except sqlite3.IntegrityError:
            print('Opa! Identificado campos já existentes sendo cadastrados novamente')
            print('Lembrando... Campos: documento, telefone precisam ser únicos!')


    # DELETE - Excluindo registros do banco de dados
    elif pergunta == 'excluir':
        print('='*30)
        perguntaDelete = input('Digite o nome ou ID do usuário que deseja excluir:').capitalize()
        print('='*30)

        try:
            # Deletando dados do SQL
            deletarDado(nomeUsuario,id)
            print('Dado excluído com sucesso!')


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

    elif pergunta == 'listar':
        print('='*30)
        print('Listando todos os usuários da tabela')
    
        try:
            listarDados(id,nomeUsuario,documento,telefone)
            conexao_banco.commit()
        except Exception as erro:
            print('='*30)
            print(f'Erro ao listar dados do banco, vê aí: {erro}')


    elif pergunta == 'atualizar':
        print('='*30)
        perguntaPorId = input('Antes de prosseguirmos, me informe o ID da pessoa no qual alterarmos o(s) dado(s): ')


        perguntaAtualizar = input('Digite o dado que deseja atualizar: [nome] [documento] [telefone] [todos]').capitalize()
        
        if perguntaAtualizar == 'Nome':
            nomeAtualizado = input('Digite aqui o novo valor para nome: ')
            atualizarDadoNome(nomeUsuario)

        try:
            # Deletando dados do SQL
            deletarDado(nomeUsuario,id)
            print('Dado excluído com sucesso!')


            if cursor.rowcount > 0:
                print('Sucesso! dado atualizado no banco de dados')
                sleep(1.5)
        
        except Exception as erro:
            print('='*30)
            print(f'Erro ao excluir dados do banco, vê aí: {erro}')
            

        print('='*30)

    else:
        print('Comando incorreto ou não reconhecido, tente novamente!')

# Fecha a conexão com o banco de dados, encerrando o circuito
conexao_banco.close()