CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS veterinario (
    id_usuario INTEGER PRIMARY KEY,
    crmv TEXT NOT NULL,
    verificado BOOLEAN DEFAULT 0,
    bio TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id) 
)
"""
#LEMBRAR DE COMENTAR SOBRE ID USUARIO PRO MAROQUIO

INSERIR = """
INSERT INTO veterinario (id_usuario, crmv, verificado, bio)
VALUES (?, ?, ?, ?)
"""
ATUALIZAR = """
UPDATE veterinario SET crmv = ?, verificado = ?, bio = ?
WHERE id_usuario = ?
"""
EXCLUIR = """
DELETE FROM veterinario 
WHERE id_usuario = ?
"""
OBTER_TODOS = """
SELECT * 
FROM veterinario 
ORDER BY id_usuario
"""
OBTER_POR_ID = """
SELECT * 
FROM veterinario 
WHERE id_usuario = ?
"""