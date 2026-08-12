import sqlite3


DATABASE = "workguard.db"


def conectar():
    return sqlite3.connect(DATABASE)


def criar_tabela():

    conexao = conectar()
    cursor = conexao.cursor()

    # Tabela de pessoas cadastradas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento TEXT,
            cargo TEXT,
            foto TEXT
        )
    """)

    # Tabela de ocorrências
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ocorrencias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL,
            tipo TEXT NOT NULL,
            foto TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()

    print("🗄️ Banco de dados pronto!")


def salvar_pessoa(nome, data_nascimento, cargo, foto):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO pessoas
        (nome, data_nascimento, cargo, foto)
        VALUES (?, ?, ?, ?)
    """, (nome, data_nascimento, cargo, foto))

    conexao.commit()
    conexao.close()

    print("👤 Pessoa cadastrada com sucesso!")


def salvar_ocorrencia(data_hora, tipo, foto):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO ocorrencias
        (data_hora, tipo, foto)
        VALUES (?, ?, ?)
    """, (data_hora, tipo, foto))

    conexao.commit()
    conexao.close()

    print("💾 Ocorrência salva no banco!")


def listar_pessoas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, data_nascimento, cargo, foto
        FROM pessoas
    """)

    pessoas = cursor.fetchall()

    conexao.close()

    return pessoas