CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS denuncia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_comentario INTEGER,
    motivo TEXT NOT NULL,
    data_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'pendente',
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_comentario) REFERENCES comentario(id)
);
"""
INSERIR = """
INSERT INTO denuncia (id_usuario, id_comentario, motivo, status)
VALUES (?, ?, ?, ?);
"""
ATUALIZAR = """
UPDATE denuncia SET id_usuario = ?, id_comentario = ?, motivo = ?, status = ?
WHERE id = ?;
"""
EXCLUIR = """
DELETE FROM denuncia 
WHERE id = ?;
"""
OBTER_TODOS = """
SELECT * 
FROM denuncia 
ORDER BY data_envio DESC;
"""
OBTER_POR_ID = """
SELECT * 
FROM denuncia 
WHERE id = ?;
"""
