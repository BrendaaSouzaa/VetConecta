CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS chamado (
    id_chamado INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    status TEXT CHECK(status IN ('aberto', 'em andamento', 'resolvido')) DEFAULT 'aberto',
    data DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
)
"""
CRIAR_TABELA_RESPOSTA = """
CREATE TABLE IF NOT EXISTS resposta_chamado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_chamado INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    data DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_chamado) REFERENCES chamado(id)
)
"""
INSERIR = """
INSERT INTO chamado (id_usuario, titulo, descricao)
VALUES (?, ?, ?) 
"""

INSERIR_RESPOSTA_CHAMADO = """ 
INSERT INTO resposta_chamado (id_chamado, titulo, descricao)
VALUES (?, ?, ?)
"""

ATUALIZAR = """
UPDATE chamado SET status = ? WHERE id = ?
"""
EXCLUIR = """
DELETE FROM chamado WHERE id = ?
"""
OBTER_TODOS = """
SELECT * 
FROM chamado 
ORDER BY data DESC
"""

OBTER_RESPOSTA_POR_ORDEM ="""
SELECT * 
FROM resposta_chamado 
ORDER BY data DESC
"""
OBTER_POR_ID = """
SELECT * 
FROM chamado 
WHERE id = ?
"""