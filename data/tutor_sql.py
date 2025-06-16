CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS tutor (
    id_usuario INTEGER PRIMARY KEY,
    telefone TEXT,
    endereco TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
"""
INSERIR = """
INSERT INTO tutor (id_usuario, telefone, endereco)
VALUES (?, ?, ?);
"""
ATUALIZAR = """
UPDATE tutor SET telefone = ?, endereco = ?
WHERE id_usuario = ?;
"""
EXCLUIR = """
DELETE FROM tutor 
WHERE id_usuario = ?;
"""
OBTER_TODOS = """
SELECT * 
FROM tutor 
ORDER BY id_usuario;
"""
OBTER_POR_ID = """
SELECT * 
FROM tutor 
WHERE id_usuario = ?;
"""
