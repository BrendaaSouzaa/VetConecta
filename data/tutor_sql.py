CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS tutor (
    id_tutor INTEGER PRIMARY KEY,
    FOREIGN KEY (id_tutor) REFERENCES usuario(id_usuario)
);
"""
INSERIR = """
INSERT INTO tutor (id_tutor, telefone, endereco)
VALUES (?, ?, ?);
"""
ATUALIZAR = """
UPDATE tutor
SET telefone = ?, endereco = ?
WHERE id_tutor = ?;
"""

EXCLUIR = """
DELETE FROM tutor 
WHERE id_tutor = ?;
"""
OBTER_TODOS = """
SELECT * 
FROM tutor 
ORDER BY id_tutor;
"""
OBTER_POR_ID = """
SELECT * 
FROM tutor 
WHERE id_tutor = ?;
"""
OBTER_DADOS_TUTOR = """
SELECT u.nome, u.email, u.telefone
FROM tutor t
JOIN usuario u ON t.id_tutor = u.id_usuario
WHERE t.id_tutor = ?;
"""