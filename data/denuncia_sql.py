CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS denuncia (
    id_denuncia INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_admin INTEGER,
    motivo TEXT NOT NULL,
    data_denuncia DATETIME DEFAULT CURRENT_DATE,
    status TEXT DEFAULT 'pendente',
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_admin) REFERENCES administrador(id)
);
"""
INSERIR = """
INSERT INTO denuncia (id_usuario, id_admin, motivo, status)
VALUES (?, ?, ?, ?);
"""
ATUALIZAR = """
UPDATE denuncia SET id_usuario = ?, motivo = ?, status = ?
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
