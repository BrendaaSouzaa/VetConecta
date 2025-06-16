CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS postagem_artigo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_veterinario INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    conteudo TEXT NOT NULL,
    categoria_id INTEGER NOT NULL,
    data_publicacao DATE DEFAULT CURRENT_DATE,
    visualizacoes INTEGER DEFAULT 0,
    FOREIGN KEY (id_veterinario) REFERENCES veterinario(id_usuario),
    FOREIGN KEY (categoria_id) REFERENCES categoria_artigo(id)
);
"""

INSERIR = """
INSERT INTO postagem_artigo (id_veterinario, titulo, conteudo, categoria_id)
VALUES (?, ?, ?, ?);
"""

ATUALIZAR = """
UPDATE postagem_artigo 
SET titulo = ?, conteudo = ?, categoria_id = ?
WHERE id = ?;
"""

EXCLUIR = """
DELETE FROM postagem_artigo 
WHERE id = ?;
"""

OBTER_TODOS = """
SELECT * 
FROM postagem_artigo 
ORDER BY data_publicacao DESC;
"""

OBTER_POR_ID = """
SELECT * 
FROM postagem_artigo 
WHERE id = ?;
"""
