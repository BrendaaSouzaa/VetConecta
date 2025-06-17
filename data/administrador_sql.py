CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS administrador (
    id_usua INTEGER PRIMARY KEY,
    nivel_acesso INTEGER DEFAULT 1,
);
"""

INSERIR = """
INSERT INTO administrador (id_usuario, nivel_acesso)
VALUES (?, ?);
"""

ATUALIZAR = """
UPDATE administrador SET nivel_acesso = ?
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
