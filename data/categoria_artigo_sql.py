CRIAR_TABELA_CATEGORIA = """
CREATE TABLE IF NOT EXISTS categoria_artigo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255) NOT NULL
)
"""

INSERIR_CATEGORIA = """
INSERT INTO categoria_artigo (titulo)
VALUES (?)
"""

EXCLUIR_CATEGORIA = """
DELETE FROM categoria_artigo
WHERE id = ?
"""

OBTER_TODAS_CATEGORIAS = """
SELECT *
FROM categoria_artigo
ORDER BY titulo ASC
"""

OBTER_CATEGORIA_POR_ID = """
SELECT *
FROM categoria_artigo
WHERE id = ?
"""
