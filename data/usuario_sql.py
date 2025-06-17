CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha CHAR(8) NOT NULL,
    telefone CHAR(11) NOT NULL,
);
"""
INSERIR = """
INSERT INTO usuario (nome, email, senha, telefone)
VALUES (?, ?, ?, ?, ?);
"""
ATUALIZAR = """
UPDATE usuario 
SET nome = ?, email = ?, senha = ?, telefone = ?
WHERE id = ?;
"""
EXCLUIR = """
DELETE FROM usuario 
WHERE id = ?;
"""
OBTER_TODOS = """
SELECT 
id, nome, email, telefone
FROM usuario 
ORDER BY nome;
"""
OBTER_POR_ID = """
SELECT 
id, nome, email, telefone
FROM usuario 
WHERE id = ?;
"""