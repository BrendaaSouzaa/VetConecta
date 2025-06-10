CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS verificacao_crmv (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_veterinario INTEGER NOT NULL,
    data_verificacao DATE DEFAULT CURRENT_DATE,
    status_verificacao TEXT CHECK(status_verificacao IN ('pendente', 'verificado', 'rejeitado')),
    FOREIGN KEY (id_veterinario) REFERENCES veterinario(id_usuario)
);
"""
INSERIR = """
INSERT INTO verificacao_crmv (id_veterinario, status_verificacao)
VALUES (?, ?);
"""
ATUALIZAR = """
UPDATE verificacao_crmv SET status_verificacao = ?
WHERE id_veterinario = ?;
"""
EXCLUIR = """
DELETE FROM verificacao_crmv WHERE id_veterinario = ?;
"""
OBTER_TODOS = """
SELECT * F
ROM verificacao_crmv 
ORDER BY data_verificacao DESC;
"""
OBTER_POR_ID = """
SELECT * FROM verificacao_crmv 
WHERE id = ?;
"""