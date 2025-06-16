CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS postagem_feed (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    texto TEXT NOT NULL,
    data_postagem DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
"""

INSERIR = """
INSERT INTO postagem_feed (id_usuario, texto)
VALUES (?, ?);
"""

ATUALIZAR = """
UPDATE postagem_feed
SET texto = ?
WHERE id = ?;
"""

EXCLUIR = """
DELETE FROM postagem_feed
WHERE id = ?;
"""

OBTER_TODOS = """
SELECT * 
FROM postagem_feed 
ORDER BY data_postagem DESC;
"""

OBTER_POR_ID = """
SELECT * 
FROM postagem_feed 
WHERE id = ?;
"""
