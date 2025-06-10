CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha CHAR(8) NOT NULL,
    telefone CHAR(11) NOT NULL,
    tipo_usuario TEXT CHECK(tipo_usuario IN ('tutor', 'veterinario', 'administrador')) NOT NULL
);
"""
INSERIR = """
INSERT INTO usuario (nome, email, senha, telefone, tipo_usuario)
VALUES (?, ?, ?, ?, ?);
"""
ATUALIZAR = """
UPDATE usuario 
SET nome = ?, email = ?, senha = ?, telefone = ?, tipo_usuario = ?
WHERE id = ?;
"""
EXCLUIR = """
DELETE FROM usuario 
WHERE id = ?;
"""
OBTER_TODOS = """
-- OBTER_TODOS
SELECT id, nome, email, telefone, tipo_usuario 
FROM usuario 
ORDER BY nome;
"""
OBTER_POR_ID = """
-- OBTER_POR_ID
SELECT id, nome, email, telefone, tipo_usuario 
FROM usuario 
WHERE id = ?;
"""