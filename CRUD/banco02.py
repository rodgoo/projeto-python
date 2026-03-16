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
    for linha in dados:
        id,nomeUsuario,documento,telefone = linha
        print(f"""
            ID: {id}
            Nome: {nomeUsuario}
            CPF: {documento}
            Contato: {telefone}
            """)

def atualizarDadoNome(nomeUsuario, id):
    cursor.execute("""
                   UPDATE cadastroCliente SET nomeUsuario = ?
                   WHERE id = ?
                   """,(nomeUsuario, id))
    conexao_banco.commit()
    return cursor.rowcount > 0


def atualizarDadoDocumento(documento, id):
    cursor.execute("""
                   UPDATE cadastroCliente SET documento = ?
                   WHERE id = ?
                   """,(documento, id))
    conexao_banco.commit()
    return cursor.rowcount > 0

def atualizarDadoTelefone(telefone, id):
    cursor.execute("""
                   UPDATE cadastroCliente SET telefone = ?
                   WHERE id = ?
                   """,(telefone, id))
    conexao_banco.commit()
    return cursor.rowcount > 0

def atualizarTodosDados(nomeUsuario,documento,telefone, id):
    cursor.execute("""
                    UPDATE cadastroCliente SET nomeUsuario = ?,
                    documento = ?,
                    telefone = ? 
                    WHERE id = ?
                   """,(nomeUsuario,documento,telefone, id))
    conexao_banco.commit()
    return cursor.rowcount > 0

def deletarDado(nomeUsuario, id):
    cursor.execute('DELETE FROM cadastroCliente WHERE nomeUsuario = ? OR id = ?',(nomeUsuario,id,))
    conexao_banco.commit()
    return cursor.rowcount > 0



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

            sleep(1)
            print(f'A tabela será mostrada em segundos, afim de exibir os novos valores')
            sleep(3)

            try:
                listarDados()
        
            except Exception as erro:
                print('='*30)
                print(f'Erro ao listar dados do banco, vê aí: {erro}')
        
        except sqlite3.IntegrityError:
                print('Opa! Identificamos campos já existentes sendo cadastrados novamente')
                print('Lembrando... Os Campos: documento, telefone precisam ser únicos!')

        except Exception as erro:
            print('='*30)
            print(f'Erro ao adicionar os dados no banco, dá uma olhada: {erro}')


    # DELETE - Excluindo registros do banco de dados
    elif pergunta == 'excluir':
        print('='*30)
        print('Listando todos os usuários da tabela...:')
        sleep(2)
    
        try:
            listarDados()
        
        except Exception as erro:
            print('='*30)
            print(f'Erro ao listar dados do banco, vê aí: {erro}')

        print('='*30)
        apagarPessoa = input('Digite o nome ou ID do usuário que deseja excluir:').capitalize()
        print('='*30)

        try:
            # Deletando dados do SQL
            deletado = deletarDado(apagarPessoa.capitalize(),apagarPessoa)
            print('Dado excluído com sucesso!')

            sleep(1)
            print(f'A tabela será mostrada em segundos, afim de exibir os novos valores')
            sleep(3)

            try:
                listarDados()
        
            except Exception as erro:
                print('='*30)
                print(f'Erro ao listar dados do banco, vê aí: {erro}')
        
        except Exception as erro:
            print('='*30)
            print(f'Erro ao excluir dados do banco, vê aí: {erro}')

    elif pergunta == 'listar':
        print('='*30)
        print('Listando todos os usuários da tabela...:')
        sleep(2)

        cursor.execute('SELECT MAX(id) FROM cadastroCliente')
        resultado = cursor.fetchone()[0]

        if resultado is None:
            print('O banco ainda está vazio, tente adicionar algum dado.')

        try:
            listarDados()
        
        except Exception as erro:
            print('='*30)
            print(f'Erro ao listar dados do banco, vê aí: {erro}')


    elif pergunta == 'atualizar':
        print('='*30)

        try:
            listarDados()
        
        except Exception as erro:
            print('='*30)
            print(f'Erro ao listar dados do banco, vê aí: {erro}')

        def verificandoID(id_digitado):
            cursor.execute('SELECT MAX(id) FROM cadastroCliente')
            resultado = cursor.fetchone()[0]

            if resultado is None:
                return False,'O banco ainda está vazio, tente adicionar algum dado!'
            if id_digitado > resultado:
                return False, f'O id {id_digitado} não existe! Maior registro {resultado}'
            return True,''

        # Faz a validação do ID para a alteração com o usuário
        print('='*30)
        perguntaPorId = int(input('Antes de prosseguirmos, me informe o ID da pessoa no qual alteraremos o(s) dado(s): ').strip())
        existente, msg = verificandoID(perguntaPorId)

        if not existente:
            print(msg)
            continue

        print('Digite o dado que deseja atualizar: [nome] [documento] [telefone] [tudo]')
        perguntaAtualizar = input('O que deseja alterar? ').capitalize()
       
        # Alterando o nome
        if perguntaAtualizar == 'Nome':         
            nomeAtualizado = input('Digite aqui o novo valor para [nome]: ')

            try: 
                vinculandoId = atualizarDadoNome(nomeAtualizado, perguntaPorId)

                if vinculandoId:
                    print(f'Sucesso! Nome do id: {perguntaPorId} alterado!')
                    sleep(1)
                    print(f'A tabela será mostrada em segundos, afim de exibir os novos valores')
                    sleep(3)

                    try:
                        listarDados()
                
                    except Exception as erro:
                        print('='*30)
                        print(f'Erro ao listar dados do banco, vê aí: {erro}')
                else:
                    print(f'Erro no banco! id: {perguntaPorId} não encontrado')

            except Exception as erro:
                print('='*30)
                print(f'Erro ao alterar dados do banco, vê aí: {erro}')

        # Alterando o documento
        if perguntaAtualizar == 'Documento':         
            documentoAtualizado = input('Digite aqui o novo valor para [documento] [valor único]: ')

            try: 
                vinculandoId = atualizarDadoDocumento(documentoAtualizado, perguntaPorId)

                if vinculandoId:
                    print(f'Sucesso! Documento do id: {perguntaPorId} alterado!')
                    sleep(1)
                    print(f'A tabela será mostrada em segundos, afim de exibir os novos valores')
                    sleep(3)

                    try:
                        listarDados()
                
                    except Exception as erro:
                        print('='*30)
                        print(f'Erro ao listar dados do banco, vê aí: {erro}')
                else:
                    print(f'Erro no banco! id: {perguntaPorId} não encontrado')

            except Exception as erro:
                print('='*30)
                print(f'Erro ao alterar dados do banco, vê aí: {erro}')

        # Alterando o telefone
        if perguntaAtualizar == 'Telefone':         
            telefoneAtualizado = input('Digite aqui o novo valor para [telefone] [valor único]: ')

            try: 
                vinculandoId = atualizarDadoTelefone(telefoneAtualizado, perguntaPorId)

                if vinculandoId:
                    print(f'Sucesso! Telefone do id: {perguntaPorId} alterado!')
                    sleep(1)
                    print(f'A tabela será mostrada em segundos, afim de exibir os novos valores')
                    sleep(3)

                    try:
                        listarDados()
                
                    except Exception as erro:
                        print('='*30)
                        print(f'Erro ao listar dados do banco, vê aí: {erro}')
                else:
                    print(f'Erro no banco! id: {perguntaPorId} não encontrado')

            except Exception as erro:
                print('='*30)
                print(f'Erro ao alterar dados do banco, vê aí: {erro}')

        # Alterando todos os dados
        if perguntaAtualizar == 'Tudo':         
            tudoAtualizadoNome = input('Digite aqui o novo valor para [nome]: ')
            tudoAtualizadoDoc = input('Digite aqui o novo valor para [documento] [único]: ')
            tudoAtualizadoTel = input('Digite aqui o novo valor para [telefone] [único]: ')

            try: 
                vinculandoId = atualizarTodosDados(tudoAtualizadoNome, tudoAtualizadoDoc, tudoAtualizadoTel, perguntaPorId)

                if vinculandoId:
                    print(f'Sucesso! Todos os dados do id: {perguntaPorId} alterados!')
                    sleep(1)
                    print(f'A tabela será mostrada em segundos, afim de exibir os novos valores')
                    sleep(3)
                    print('='*30)

                    try:
                        listarDados()
                
                    except Exception as erro:
                        print('='*30)
                        print(f'Erro ao listar dados do banco, vê aí: {erro}')
                else:
                    print(f'Erro no banco! id: {perguntaPorId} não encontrado')

            except Exception as erro:
                print('='*30)
                print(f'Erro ao alterar dados do banco, vê aí: {erro}')

    else:
        print('Comando incorreto ou não reconhecido, tente novamente!')

# Fecha a conexão com o banco de dados, encerrando o circuito
conexao_banco.close()