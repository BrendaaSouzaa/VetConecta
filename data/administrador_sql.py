CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS administrador (
    id_admin INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha CHAR(8),
    FOREIGN KEY (id_admin) REFERENCES usuario(id_usuario)
);
"""

INSERIR = """
INSERT INTO administrador (nome, email, senha )
VALUES (?, ?, ?);
"""

ATUALIZAR = """
UPDATE administrador 
SET nome = ?, email = ?, senha = ?
WHERE id_admin = ?;
"""

EXCLUIR = """
DELETE FROM administrador 
WHERE id_admin = ?;
"""

OBTER_TODOS = """
SELECT * 
FROM administrador 
ORDER BY id_admin;
"""

OBTER_POR_ID = """
SELECT * 
FROM administrador 
WHERE id_admin = ?;
"""
