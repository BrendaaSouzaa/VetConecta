CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS veterinario (
    id_veterinario INTEGER PRIMARY KEY,
    crmv TEXT NOT NULL,
    verificado BOOLEAN DEFAULT 0,
    bio TEXT,
    FOREIGN KEY (id_veterinario) REFERENCES usuario(id)
);
"""

INSERIR = """
INSERT INTO veterinario (id_veterinario, crmv, verificado, bio)
VALUES (?, ?, ?, ?);
"""

ATUALIZAR = """
UPDATE veterinario SET crmv = ?, verificado = ?, bio = ?
WHERE id_veterinario = ?;
"""

EXCLUIR = """
DELETE FROM veterinario 
WHERE id_veterinario = ?;
"""

OBTER_TODOS = """
SELECT * 
FROM veterinario 
ORDER BY id_veterinario;
"""

OBTER_POR_ID = """
SELECT * 
FROM veterinario 
WHERE id_veterinario = ?;
"""