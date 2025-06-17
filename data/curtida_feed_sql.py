CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS curtida_feed (
    id_usuario INTEGER NOT NULL,
    id_feed INTEGER NOT NULL,
    data_curtida DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (id_usuario, id_feed),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_feed) REFERENCES postagem_feed(id_postagem_feed)
);
"""

INSERIR = """
INSERT INTO curtida_feed (id_usuario, id_feed)
VALUES (?, ?);
"""

EXCLUIR = """
DELETE FROM curtida_feed 
WHERE id_usuario = ? AND id_feed = ?;
"""

OBTER_TODOS = """
SELECT * 
FROM curtida_feed 
ORDER BY data_curtida DESC;
"""

OBTER_POR_ID = """
SELECT * 
FROM curtida_feed 
WHERE id_usuario = ? AND id_feed = ?;
"""
