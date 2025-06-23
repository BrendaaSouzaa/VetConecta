CRIAR_TABELA_RESPOSTA = """
CREATE TABLE IF NOT EXISTS resposta_chamado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_chamado INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    data DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_chamado) REFERENCES chamado(id)
);
"""