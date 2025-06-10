CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS comentario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_artigo INTEGER NOT NULL,
    texto TEXT NOT NULL,
    data_comentario DATE DEFAULT CURRENT_DATE,
    data_moderacao DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_artigo) REFERENCES postagem_artigo(id)
);
"""
INSERIR = """
INSERT INTO comentario (id_usuario, id_artigo, texto)
VALUES (?, ?, ?);
"""
ATUALIZAR = """
UPDATE comentario SET texto = ?, data_moderacao = ?
WHERE id = ?;
"""
EXCLUIR = """
DELETE FROM comentario 
WHERE id = ?;
"""
OBTER_TODOS = """
SELECT * 
FROM comentario 
ORDER BY data_comentario DESC;
"""
OBTER_POR_ID ="""
SELECT * FROM comentario 
WHERE id = ?;
"""