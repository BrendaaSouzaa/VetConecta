CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS curtida_artigo (
    id_usuario INTEGER NOT NULL,
    id_postagem_artigo INTEGER PRIMARY KEY AUTOINCREMENT,
    data_curtida DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (id_usuario, id_postagem_artigo),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_postagem_artigo) REFERENCES postagem_artigo(id)
);
"""
INSERIR = """
INSERT INTO curtida_artigo (id_usuario, id_postagem_artigo)
VALUES (?, ?);
"""
ATUALIZAR = """
DELETE FROM curtida_artigo
WHERE id_usuario = ? 
AND id_postagem_artigo = ?;
"""
OBTER_TODOS = """
SELECT *
FROM curtida_artigo 
ORDER BY data_curtida DESC;
"""
OBTER_POR_ID = """ #(com base no par usuário + artigo)
SELECT * FROM curtida_artigo 
WHERE id_usuario = ? AND id_postagem_artigo = ?;
"""

