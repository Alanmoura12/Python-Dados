import sqlite3

# 1. Conectar ao banco (cria se não existir)
conexao = sqlite3.connect('Exemplo.db')

#2. criar cursor
cursor = conexao.cursor()

# 3. Executar comandos SQL
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT)")

# 4. Inserir um registro
cursor.execute("INSERT INTO clientes (nome) VALUES ('João')")

# 5. Salvar alterações
conexao.commit()



