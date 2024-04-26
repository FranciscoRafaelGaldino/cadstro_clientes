import sqlite3
import re

# Função para criar a tabela de clientes
def criar_tabela():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        email TEXT,
                        telefone TEXT
                    )''')
    
    conexao.commit()
    conexao.close()

# Função para inserir um cliente no banco de dados
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    if not validar_email(email):
        print("Formato de email inválido.")
        return
    
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    
    cursor.execute('''INSERT INTO clientes (nome, email, telefone) 
                      VALUES (?, ?, ?)''', (nome, email, telefone))
    
    conexao.commit()
    conexao.close()
    
    print("Cliente cadastrado com sucesso!")

# Função para listar todos os clientes cadastrados
def listar_clientes():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()
    
    if not resultados:
        print("Não há clientes cadastrados.")
    else:
        print("Lista de clientes:")
        for cliente in resultados:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}, Telefone: {cliente[3]}")
    
    conexao.close()

# Função para deletar um cliente do banco de dados
def deletar_cliente():
    listar_clientes()
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    id_cliente = input("Digite o ID do cliente que deseja deletar: ")
    cursor.execute("DELETE FROM clientes WHERE id=?", (id_cliente,))
    conexao.commit()
    conexao.close()
    print("Cliente deletado com sucesso!")

# Função para validar o formato de e-mail
def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)

def menu():
    print("\n--- Menu ---")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Deletar cliente")
    print("4. Sair")

def main():
    criar_tabela()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            deletar_cliente()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
