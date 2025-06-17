CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS administrador (
    id_ INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha INTEGER DEFAULT 1,
    FOREIGN KEY (id_admin) REFERENCES usuario(id),
);
"""

INSERIR = """
INSERT INTO administrador (id_usuario, senha )
VALUES (?, ?);
"""

ATUALIZAR = """
UPDATE administrador SET senha = ?
WHERE id_usuario = ?;
"""

EXCLUIR = """
DELETE FROM administrador 
WHERE id_usuario = ?;
"""

OBTER_TODOS = """
SELECT * 
FROM administrador 
ORDER BY id_usuario;
"""

OBTER_POR_ID = """
SELECT * 
FROM administrador 
WHERE id_usuario = ?;
"""
