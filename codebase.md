# .gitignore

```
.venv
*.pyc
__pycache__
*.pyo
*.pkl

# Distribution / packaging
.Python
build/
dist/

```

# .pytest_cache\.gitignore

```
# Created by pytest automatically.
*

```

# .pytest_cache\CACHEDIR.TAG

```TAG
Signature: 8a477f597d28d172789f06886806bc55
# This file is a cache directory tag created by pytest.
# For information about cache directory tags, see:
#	https://bford.info/cachedir/spec.html

```

# .pytest_cache\README.md

```md
# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

```

# .pytest_cache\v\cache\lastfailed

```
{
  "tests/test_denuncia_repo.py": true,
  "tests/test_categoria_artigo_repo.py::TestCategoriaArtigoRepo::test_criar_tabela": true,
  "tests/test_comentario_repo.py::TestComentarioRepo::test_criar_tabela": true,
  "tests/test_comentario_repo.py::TestComentarioRepo::test_inserir": true,
  "tests/test_comentario_repo.py::TestComentarioRepo::test_atualizar": true,
  "tests/test_categoria_artigo_repo.py::TestCategoriaArtigoRepo::test_inserir_categoria": true,
  "tests/test_categoria_artigo_repo.py::TestCategoriaArtigoRepo::test_excluir_categoria": true,
  "tests/test_comentario_repo.py::TestComentarioRepo::test_inserir_comentario": true,
  "tests/test_comentario_repo.py::TestComentarioRepo::test_atualizar_comentario": true,
  "tests/test_comentario_repo.py::TestComentarioRepo::test_excluir_comentario": true,
  "tests/test_comentario_repo.py::TestComentarioRepo::test_obter_comentarios_paginado": true,
  "tests/test_comentario_repo.py::TestComentarioRepo::test_excluir": true,
  "tests/test_comentario_repo.py::TestComentarioRepo::test_obter_por_id": true,
  "tests/test_curtida_artigo_repo.py::TestAdministradorRepo::test_criar_tabela_administrador": true,
  "tests/test_administrador_repo.py::TestAdministradorRepo::test_criar_tabela_administrador": true,
  "tests/test_curtida_artigo_repo.py::TestCurtidaArtigoRepo::test_criar_tabela_curtida_artigo": true
}
```

# .pytest_cache\v\cache\nodeids

```
[
  "tests/test_administrador_repo.py::TestAdministradorRepo::test_criar_tabela_administrador",
  "tests/test_categoria_artigo_repo.py::TestCategoriaArtigoRepo::test_criar_tabela",
  "tests/test_categoria_artigo_repo.py::TestCategoriaArtigoRepo::test_excluir_categoria",
  "tests/test_categoria_artigo_repo.py::TestCategoriaArtigoRepo::test_inserir_categoria",
  "tests/test_comentario_repo.py::TestComentarioRepo::test_atualizar",
  "tests/test_comentario_repo.py::TestComentarioRepo::test_atualizar_comentario",
  "tests/test_comentario_repo.py::TestComentarioRepo::test_criar_tabela",
  "tests/test_comentario_repo.py::TestComentarioRepo::test_excluir",
  "tests/test_comentario_repo.py::TestComentarioRepo::test_excluir_comentario",
  "tests/test_comentario_repo.py::TestComentarioRepo::test_inserir",
  "tests/test_comentario_repo.py::TestComentarioRepo::test_inserir_comentario",
  "tests/test_comentario_repo.py::TestComentarioRepo::test_obter_comentarios_paginado",
  "tests/test_comentario_repo.py::TestComentarioRepo::test_obter_por_id",
  "tests/test_curtida_artigo_repo.py::TestCurtidaArtigoRepo::test_criar_tabela_curtida_artigo"
]
```

# .vscode\settings.json

```json
{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

# dados.db

This is a binary file of the type: Binary

# data\administrador_model.py

```py
from dataclasses import dataclass

@dataclass
class Administrador:
    id_admin: int
    nome: str
    email: str
    senha: str
    
```

# data\administrador_repo.py

```py
from typing import Any, Optional, List
from data.administrador_model import Administrador
from data.administrador_sql import *
from util import get_connection


def criar_tabela_administrador() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de administrador: {e}")
        return False

def inserir_administrador(admin: Administrador) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (admin.nome, admin.email, admin.senha))
        return cursor.lastrowid


def atualizar_administrador(admin: Administrador) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (admin.nome, admin.email, admin.senha, admin.id_admin))
        return cursor.rowcount > 0
    
def atualizar_senha(id_admin: int, nova_senha: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_SENHA, (nova_senha, id_admin))
        return cursor.rowcount > 0

def excluir_administrador(id_admin: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_admin,))
        return cursor.rowcount > 0


def obter_administradores_paginado(offset: int, limite: int) -> List[Administrador]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [Administrador(**row) for row in rows]


def obter_administrador_por_id(id_admin: int) -> Optional[Administrador]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_admin,))
        row = cursor.fetchone()
        return Administrador(**row) if row else None
```

# data\administrador_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS administrador (
    id_admin INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha CHAR(8) NOT NULL
);
"""

INSERIR = """
INSERT INTO administrador (nome, email, senha )
VALUES (?, ?, ?);
"""

ATUALIZAR = """
UPDATE administrador 
SET nome = ?, email = ?, senha = ?
WHERE id_admin = ?;
"""

ATUALIZAR_SENHA = """
UPDATE administrador
SET senha = ?
WHERE id_admin = ?;
"""

EXCLUIR = """
DELETE FROM administrador 
WHERE id_admin = ?;
"""

OBTER_TODOS_PAGINADO = """
SELECT * 
FROM administrador 
ORDER BY id_admin
LIMIT ? OFFSET ?;
"""

OBTER_POR_ID = """
SELECT * 
FROM administrador 
WHERE id_admin = ?;
"""

```

# data\categoria_artigo_model.py

```py
from dataclasses import dataclass

@dataclass
class CategoriaArtigo:
    id: int
    nome: str
    descricao: str | None  # campo opcional

```

# data\categoria_artigo_repo.py

```py
from typing import Optional, List
from data.categoria_artigo_model import CategoriaArtigo
from data.categoria_artigo_sql import *
from util import get_connection


def criar_tabela_categoria_artigo() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False


def inserir_categoria(categoria: CategoriaArtigo) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (categoria.nome, categoria.descricao))
        return cursor.lastrowid


def atualizar_categoria(categoria: CategoriaArtigo) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (categoria.nome, categoria.descricao, categoria.id))
        return cursor.rowcount > 0


def excluir_categoria(id_categoria: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_categoria,))
        return cursor.rowcount > 0


def obter_categorias_paginado(offset: int, limite: int) -> List[CategoriaArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [CategoriaArtigo(**row) for row in rows]
    

def obter_categoria_por_id(id_categoria: int) -> Optional[CategoriaArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_categoria,))
        row = cursor.fetchone()
        return CategoriaArtigo(**row) if row else None

```

# data\categoria_artigo_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS categoria_artigo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
);
"""
INSERIR = """
INSERT INTO categoria_artigo (nome, descricao)
VALUES (?, ?);
"""
ATUALIZAR = """
UPDATE categoria_artigo SET nome = ?, descricao = ?
WHERE id = ?;
"""
EXCLUIR = """
DELETE FROM categoria_artigo 
WHERE id = ?;
"""
OBTER_TODOS_PAGINADO = """
SELECT * 
FROM categoria_artigo 
ORDER BY nome
LIMIT ? OFFSET ?;
"""

OBTER_POR_ID = """
SELECT * 
FROM categoria_artigo 
WHERE id = ?;
"""


```

# data\chamado_model.py

```py
from dataclasses import dataclass

@dataclass
class Chamado:
    id: int
    id_usuario: int
    id_admin: int
    titulo: str
    descricao: str
    status: str  # valores possíveis: 'aberto', 'em andamento', 'resolvido'
    data: str  # formato DATE

```

# data\chamado_repo.py

```py
from typing import Optional, List
from data.chamado_model import Chamado
from data.chamado_sql import *
from util import get_connection


def criar_tabelas() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False


def inserir_chamado(chamado: Chamado) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            chamado.id_usuario,
            chamado.id_admin,
            chamado.titulo,
            chamado.descricao,
            chamado.status,
            chamado.data
        ))
        return cursor.lastrowid


def atualizar_status_chamado(id_chamado: int, novo_status: str) -> bool:
    if novo_status not in ['aberto', 'em andamento', 'resolvido']:
        raise ValueError("Status inválido. Use: 'aberto', 'em andamento' ou 'resolvido'.")

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (novo_status, id_chamado))
        return cursor.rowcount > 0


def excluir_chamado(id_chamado: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_chamado,))
        return cursor.rowcount > 0


def obter_todos_chamados_paginado(limite: int, offset: int) -> List[Chamado]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [
            Chamado(
                id=row["id"],
                id_usuario=row["id_usuario"],
                id_admin=row["id_admin"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                status=row["status"],
                data=row["data"]
            )
            for row in rows]


def obter_chamado_por_id(id_chamado: int) -> Optional[Chamado]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_chamado,))
        row = cursor.fetchone()
        if row:
            return Chamado(
                id=row["id"],
                id_usuario=row["id_usuario"],
                id_admin=row["id_admin"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                status=row["status"],
                data=row["data"]
            )
        return None




```

# data\chamado_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS chamado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_admin INTEGER,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    status TEXT CHECK(status IN ('aberto', 'em andamento', 'resolvido')) DEFAULT 'aberto',
    data DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
    FOREIGN KEY (id_admin) REFERENCES administrador(id_admin)
);
"""

INSERIR = """
INSERT INTO chamado (id_usuario, id_admin, titulo, descricao, status, data) 
VALUES (?, ?, ?, ?, ?, ?);
"""

ATUALIZAR = """
UPDATE chamado 
SET id_usuario = ?, id_admin = ?, titulo = ?, descricao = ?, status = ?, data = ?
WHERE id = ?
"""

EXCLUIR = """
DELETE FROM chamado
WHERE id = ?;
"""

OBTER_TODOS_PAGINADO = """
SELECT * 
FROM chamado 
ORDER BY data DESC
LIMIT ? OFFSET ?;
"""

OBTER_POR_ID = """
SELECT * 
FROM chamado
WHERE id = ?;

"""
```

# data\comentario_model.py

```py
from dataclasses import dataclass

from data.postagem_artigo_model import PostagemArtigo
from data.usuario_model import Usuario

@dataclass
class Comentario:
    id: int
    usuario: Usuario
    artigo: PostagemArtigo
    texto: str
    data_comentario: str
    data_moderacao: str | None
```

# data\comentario_repo.py

```py
from typing import Optional, List
from data.comentario_model import Comentario
from data.comentario_sql import *
from data.postagem_artigo_model import PostagemArtigo
from data.usuario_model import Usuario
from util import get_connection


def criar_tabela() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False


def inserir(comentario: Comentario) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            comentario.usuario,
            comentario.artigo,
            comentario.texto
        ))
        return cursor.lastrowid


def atualizar(comentario: Comentario) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            comentario.texto,
            comentario.data_moderacao,
            comentario.id
        ))
        return cursor.rowcount > 0


def excluir(id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id,))
        return cursor.rowcount > 0


def obter_todos_paginado(limite: int, offset: int) -> List[Comentario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [
            Comentario(
                id=row["id"],
                id_usuario=Usuario(id_usuario=row["id_usuario"], nome=row["nome_usuario"]),
                id_artigo=PostagemArtigo(id=row["id_artigo"], titulo=row["titulo_artigo"]),
                texto=row["texto"],
                data_comentario=row["data_comentario"],
                data_moderacao=row["data_moderacao"]
            )
            for row in rows]



def obter_por_id(id: int) -> Optional[Comentario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id,))
        row = cursor.fetchone()
        if row:
            return Comentario(
                id=row["id"],
                id_usuario=Usuario(id_usuario=row["id_usuario"], nome=row["nome_usuario"]),
                id_artigo=PostagemArtigo(id=row["id_artigo"], titulo=row["titulo_artigo"]),
                texto=row["texto"],
                data_comentario=row["data_comentario"],
                data_moderacao=row["data_moderacao"])
        return None
```

# data\comentario_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS comentario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_artigo INTEGER NOT NULL,
    texto TEXT NOT NULL,
    data_comentario DATE DEFAULT CURRENT_DATE,
    data_moderacao DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_artigo) REFERENCES postagem_artigo(id)
);
"""
INSERIR = """
INSERT INTO comentario (id_usuario, id_artigo, texto)
VALUES (?, ?, ?);
"""
ATUALIZAR = """
UPDATE comentario SET texto = ?, data_moderacao = ?
WHERE id = ?;
"""
EXCLUIR = """
DELETE FROM comentario 
WHERE id = ?;
"""
OBTER_TODOS_PAGINADO = """
SELECT 
    c.id,
    c.texto,
    c.data_comentario,
    c.data_moderacao,
    u.id_usuario,
    u.nome AS nome_usuario,
    a.id AS id_artigo,
    a.titulo AS titulo_artigo
FROM comentario c
JOIN usuario u ON c.id_usuario = u.id_usuario
JOIN postagem_artigo a ON c.id_artigo = a.id
ORDER BY c.data_comentario DESC
LIMIT ? OFFSET ?;
"""


OBTER_POR_ID = """
SELECT 
    c.id,
    c.texto,
    c.data_comentario,
    c.data_moderacao,
    u.id_usuario,
    u.nome AS nome_usuario,
    a.id AS id_artigo,
    a.titulo AS titulo_artigo
FROM comentario c
JOIN usuario u ON c.id_usuario = u.id_usuario
JOIN postagem_artigo a ON c.id_artigo = a.id
WHERE c.id = ?;
"""
```

# data\curtida_artigo_model.py

```py
from dataclasses import dataclass
from data.postagem_artigo_model import PostagemArtigo
from data.usuario_model import Usuario

@dataclass
class CurtidaArtigo:
    usuario: Usuario
    artigo: PostagemArtigo
    data_curtida: str
```

# data\curtida_artigo_repo.py

```py
from typing import Optional, List
from data.curtida_artigo_model import CurtidaArtigo
from data.curtida_artigo_sql import *
from data.postagem_artigo_model import PostagemArtigo
from data.usuario_model import Usuario
from util import get_connection


def criar_tabela() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False


def inserir(curtida: CurtidaArtigo) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (curtida.id_usuario, curtida.id_artigo))
        return cursor.rowcount > 0

def excluir_curtida(id_usuario: int, id_postagem_artigo: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_usuario, id_postagem_artigo))
        return cursor.rowcount > 0


def obter_todos_paginado(limite: int, offset: int) -> List[CurtidaArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [
            CurtidaArtigo(
                usuario=Usuario(id=row["id_usuario"], nome=row["nome_usuario"]),
                artigo=PostagemArtigo(id=row["id_postagem_artigo"], titulo=row["titulo_artigo"]),
                data_curtida=row["data_curtida"]
            )
            for row in rows]


def obter_por_id(id_usuario: int, id_postagem_artigo: int) -> Optional[CurtidaArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_usuario, id_postagem_artigo))
        row = cursor.fetchone()
        if row:
            return CurtidaArtigo(
                usuario=Usuario(id=row["id_usuario"],nome=row["nome_usuario"]),
                artigo=PostagemArtigo(id=row["id_artigo"], nome=row["titulo_artigo"]), #verificar o nome do campo titulo na tabela postagem art.
                data_curtida=row["data_curtida"]
            )
        return None
```

# data\curtida_artigo_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS curtida_artigo (
    id_usuario INTEGER NOT NULL,
    id_postagem_artigo INTEGER NOT NULL,
    data_curtida DATE DEFAULT CURRENT_DATE
    PRIMARY KEY (id_usuario, id_postagem_artigo),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_postagem_artigo) REFERENCES postagem_artigo(id_artigo)
);  
"""

INSERIR = """
INSERT INTO curtida_artigo (id_usuario, id_postagem_artigo)
VALUES (?, ?);
"""

ATUALIZAR = """
UPDATE curtida_artigo
SET data_curtida = ?
WHERE id_usuario = ? AND id_postagem_artigo = ?;
"""

EXCLUIR = """
DELETE FROM curtida_artigo
WHERE id_usuario = ? 
AND id_postagem_artigo = ?;
"""

OBTER_TODOS_PAGINADO = """
SELECT
    ca.id_usuario,
    u.nome AS nome_usuario,
    ca.id_postagem_artigo,
    pa.titulo AS titulo_artigo,
    ca.data_curtida
FROM curtida_artigo ca
INNER JOIN usuario u ON ca.id_usuario = u.id_usuario
INNER JOIN postagem_artigo pa ON ca.id_postagem_artigo = pa.id
ORDER BY ca.data_curtida DESC
LIMIT ? OFFSET ?;
"""

OBTER_POR_ID = """
SELECT
    ca.id_usuario,
    u.nome AS nome_usuario,
    ca.id_postagem_artigo,
    pa.titulo AS titulo_artigo,
    ca.data_curtida
FROM curtida_artigo ca
INNER JOIN usuario u ON ca.id_usuario = u.id_usuario
INNER JOIN postagem_artigo pa ON ca.id_postagem_artigo = pa.id
WHERE ca.id_usuario = ? AND ca.id_postagem_artigo = ?;
"""
```

# data\curtida_feed_model.py

```py
from dataclasses import dataclass
from typing import Optional

@dataclass
class CurtidaFeed:
    id_usuario: int
    id_postagem_feed: int
    data_curtida: Optional[str] = None

```

# data\curtida_feed_repo.py

```py
from typing import Optional, List
from data.curtida_feed_model import CurtidaFeed
from data.curtida_feed_sql import *
from util import get_connection


def criar_tabela() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False


def inserir(curtida: CurtidaFeed) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            curtida.id_usuario,
            curtida.id_postagem_feed
        ))
        return cursor.rowcount > 0


def excluir(id_usuario: int, id_postagem_feed: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_usuario, id_postagem_feed))
        return cursor.rowcount > 0


def obter_todos_paginado(limite: int, offset: int) -> List[CurtidaFeed]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [
            CurtidaFeed(
                id_usuario=row["id_usuario"],
                id_postagem_feed=row["id_postagem_feed"],
                data_curtida=row["data_curtida"]
            )
            for row in rows]


def obter_por_id(id_usuario: int, id_postagem_feed: int) -> Optional[CurtidaFeed]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_usuario, id_postagem_feed))
        row = cursor.fetchone()
        if row:
            return CurtidaFeed(
                id_usuario=id_usuario,
                id_postagem_feed=id_postagem_feed,
                data_curtida=row["data_curtida"]
            )
        return None

```

# data\curtida_feed_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS curtida_feed (
    id_usuario INTEGER NOT NULL,
    id_postagem_feed INTEGER NOT NULL,
    data_curtida DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (id_usuario, id_postagem_feed),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_postagem_feed) REFERENCES postagem_feed(id_postagem_feed)
);
"""

INSERIR = """
INSERT INTO curtida_feed (id_usuario, id_postagem_feed)
VALUES (?, ?);
"""

EXCLUIR = """
DELETE FROM curtida_feed 
WHERE id_usuario = ? AND id_postagem_feed = ?;
"""


OBTER_TODOS_PAGINADO = """
SELECT 
    cf.id_usuario,
    u.nome AS nome_usuario,
    cf.id_postagem_feed,
    pf.descricao AS descricao_postagem,
    pf.imagem,
    cf.data_curtida
FROM curtida_feed cf
JOIN usuario u ON cf.id_usuario = u.id_usuario
JOIN postagem_feed pf ON cf.id_postagem_feed = pf.id_postagem_feed
ORDER BY cf.data_curtida DESC
LIMIT ? OFFSET ?;
"""

OBTER_POR_ID = """
SELECT 
    u.nome AS nome_usuario,
    pf.descricao AS descricao_postagem,
    pf.imagem,
    cf.data_curtida
FROM curtida_feed cf
JOIN usuario u ON cf.id_usuario = u.id_usuario
JOIN postagem_feed pf ON cf.id_postagem_feed = pf.id_postagem_feed
WHERE cf.id_usuario = ? AND cf.id_postagem_feed = ?;
"""

```

# data\denuncia_model.py

```py
from dataclasses import dataclass
from typing import Optional
from data.administrador_model import Administrador
from data.usuario_model import Usuario

@dataclass
class Denuncia:
    id_denuncia: Optional[int] 
    usuario: Usuario
    admin: Administrador
    motivo: str
    data_denuncia: str
    status: str

```

# data\denuncia_repo.py

```py
from typing import Optional, List
from data.denuncia_model import Denuncia
from data.denuncia_sql import *
from util import get_connection


def criar_tabela_denuncia() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False


def inserir_denuncia(denuncia: Denuncia) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            denuncia.id_usuario,
            denuncia.id_admin,
            denuncia.motivo,
            denuncia.status
        ))
        return cursor.lastrowid


def atualizar_denuncia(denuncia: Denuncia) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            denuncia.id_usuario,
            denuncia.id_admin,
            denuncia.motivo,
            denuncia.status,
            denuncia.id_denuncia
        ))
        return cursor.rowcount > 0


def excluir_denuncia(id_denuncia: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_denuncia,))
        return cursor.rowcount > 0

def obter_todas_denuncias_paginadas(limite: int, offset: int) -> List[Denuncia]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODAS_DENUNCIAS_PAGINADAS, (limite, offset))
        rows = cursor.fetchall()
        return [Denuncia(**row) for row in rows]



def obter_denuncia_por_id(id_denuncia: int) -> Optional[Denuncia]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_denuncia,))
        row = cursor.fetchone()
        return Denuncia(**row) if row else None

```

# data\denuncia_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS denuncia (
    id_denuncia INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_admin INTEGER,
    motivo TEXT NOT NULL,
    data_denuncia DATETIME DEFAULT CURRENT_DATE,
    status TEXT NOT NULL CHECK (status IN ('pendente', 'aprovada', 'rejeitada')),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_admin) REFERENCES administrador(id)
);
"""

INSERIR = """
INSERT INTO denuncia (id_usuario, id_admin, motivo, status)
VALUES (?, ?, ?, ?);
"""

ATUALIZAR = """
UPDATE denuncia 
SET id_usuario = ?, id_admin = ?, motivo = ?, status = ?
WHERE id_denuncia = ?;
"""

EXCLUIR = """
DELETE FROM denuncia 
WHERE id_denuncia = ?;
"""

OBTER_TODAS_DENUNCIAS_PAGINADAS = """
SELECT
    d.id_denuncia,
    d.id_usuario,
    u.nome AS nome_usuario,
    d.id_admin,
    a.nome AS nome_admin,
    d.motivo,
    d.data_denuncia,
    d.status
FROM denuncia d
INNER JOIN usuario u ON d.id_usuario = u.id_usuario
INNER JOIN administrador a ON d.id_admin = a.id_admin
ORDER BY d.data_denuncia DESC
LIMIT ? OFFSET ?;
"""


OBTER_POR_ID = """
SELECT
    d.id_denuncia,
    d.id_usuario,
    u.nome AS nome_usuario,
    d.id_admin,
    a.nome AS nome_admin,
    d.motivo,
    d.data_denuncia,
    d.status
FROM denuncia d
INNER JOIN usuario u ON d.id_usuario = u.id_usuario
INNER JOIN administrador a ON d.id_admin = a.id_admin
WHERE d.id_denuncia = ?;
"""
```

# data\postagem_artigo_model.py

```py
from dataclasses import dataclass
from data.categoria_artigo_model import CategoriaArtigo
from data.veterinario_model import Veterinario

@dataclass
class PostagemArtigo:
    id: int
    veterinario: Veterinario
    titulo: str
    conteudo: str
    categoria_artigo: CategoriaArtigo
    data_publicacao: str
    visualizacoes: int
```

# data\postagem_artigo_repo.py

```py
from typing import Optional, List
from data.categoria_artigo_model import CategoriaArtigo
from data.postagem_artigo_model import PostagemArtigo
from data.postagem_artigo_sql import *
from util import get_connection
from data.veterinario_model import Veterinario


def criar_tabela() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False


def inserir(postagem: PostagemArtigo) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            postagem.id_veterinario,
            postagem.titulo,
            postagem.conteudo,
            postagem.categoria_artigo .id
        ))
        return cursor.lastrowid


def atualizar(postagem: PostagemArtigo) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            postagem.titulo,
            postagem.conteudo,
            postagem.categoria_artigo .id,
            postagem.visualizacoes,
            postagem.id
        ))
        return cursor.rowcount > 0


def excluir(id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id,))
        return cursor.rowcount > 0


def obter_todos_paginado(limite: int, offset: int) -> List[PostagemArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [
            PostagemArtigo(
                id=row["id"],
                veterinario=Veterinario(id=row["id_veterinario"], nome=row["nome_veterinario"]),
                titulo=row["titulo"],
                conteudo=row["conteudo"],
                categoria=CategoriaArtigo(id=row["id_categoria_artigo"], nome_categoria=row["nome_categoria"]),
                data_publicacao=row["data_publicacao"],
                visualizacoes=row["visualizacoes"]
            )
            for row in rows]



def obter_por_id(id: int) -> Optional[PostagemArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id,))
        row = cursor.fetchone()
        if row:
            return PostagemArtigo(
                id=row["id"],
                veterinario=Veterinario(id=row["id_veterinario"], nome=row["nome_veterinario"]),
                titulo=row["titulo"],
                conteudo=row["conteudo"],
                categoria=CategoriaArtigo(id=row["categoria_id"], nome_categoria=row["nome_categoria"]),
                data_publicacao=row["data_publicacao"],
                visualizacoes=row["visualizacoes"]
            )
        return None
```

# data\postagem_artigo_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS postagem_artigo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_veterinario INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    conteudo TEXT NOT NULL,
    id_categoria_artigo INTEGER NOT NULL,
    data_publicacao DATE DEFAULT CURRENT_DATE,
    visualizacoes INTEGER DEFAULT 0,
    FOREIGN KEY (id_veterinario) REFERENCES veterinario(id_usuario),
    FOREIGN KEY (id_categoria_artigo) REFERENCES categoria_artigo(id)
);
"""

INSERIR = """
INSERT INTO postagem_artigo (id_veterinario, titulo, conteudo, id_categoria_artigo)
VALUES (?, ?, ?, ?);
"""

ATUALIZAR = """
UPDATE postagem_artigo 
SET titulo = ?, conteudo = ?, id_categoria_artigo = ?
WHERE id = ?;
"""

EXCLUIR = """
DELETE FROM postagem_artigo 
WHERE id = ?;
"""

OBTER_TODOS_PAGINADO = """
SELECT 
    p.id,
    p.id_veterinario,
    v.nome AS nome_veterinario,
    p.titulo,
    p.conteudo,
    p.id_categoria_artigo,
    c.nome AS nome_categoria,
    p.data_publicacao,
    p.visualizacoes
FROM postagem_artigo p
JOIN categoria_artigo c ON p.id_categoria_artigo = c.id
JOIN veterinario v ON p.id_veterinario = v.id
ORDER BY p.data_publicacao DESC
LIMIT ? OFFSET ?;
"""


OBTER_POR_ID = """
SELECT 
    p.id,
    p.id_veterinario,
    v.nome AS nome_veterinario,
    p.titulo,
    p.conteudo,
    p.id_categoria_artigo,
    c.nome AS nome_categoria,
    p.data_publicacao,
    p.visualizacoes
FROM postagem_artigo p
JOIN categoria_artigo c ON p.id_categoria_artigo = c.id
JOIN veterinario v ON p.id_veterinario = v.id
WHERE p.id = ?;
"""
```

# data\postagem_feed_model.py

```py
from dataclasses import dataclass
from typing import Optional
from data.tutor_model import Tutor

@dataclass
class PostagemFeed:
    id_postagem_feed: int
    tutor: Tutor
    imagem: Optional[str]
    descricao: str
    data_postagem: str

```

# data\postagem_feed_repo.py

```py
from typing import Optional, List
from data.postagem_feed_model import PostagemFeed
from data.postagem_feed_sql import *
from data.tutor_model import Tutor
from util import get_connection


def criar_tabela() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False


def inserir(postagem: PostagemFeed) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            postagem.id_tutor,
            postagem.imagem,
            postagem.descricao
        ))
        return cursor.lastrowid


    
def atualizar(postagem: PostagemFeed) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            postagem.descricao,
            postagem.id_postagem_feed
        ))
        return cursor.rowcount > 0


def excluir(id_postagem_feed: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_postagem_feed,))
        return cursor.rowcount > 0

def obter_todos_paginado(limite: int, offset: int) -> List[PostagemFeed]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [
            PostagemFeed(
                id_postagem_feed=row["id_postagem_feed"],
                tutor=Tutor(id=row["id_tutor"], nome=row["nome_tutor"]),
                imagem=row["imagem"],
                descricao=row["descricao"],
                data_postagem=row["data_postagem"]
            )
            for row in rows
        ]



def obter_por_id(id_postagem_feed: int) -> Optional[PostagemFeed]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_postagem_feed,))
        row = cursor.fetchone()
        if row:
            return PostagemFeed(
                id_postagem_feed=row["id_postagem_feed"],
                tutor=Tutor(id=row["id_tutor"], nome=row["nome_tutor"]),
                imagem=row["imagem"],
                descricao=row["descricao"],
                data_postagem=row["data_postagem"]
            )
        return None
```

# data\postagem_feed_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS postagem_feed (
    id_postagem_feed INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tutor INTEGER NOT NULL,
    imagem TEXT,
    descricao TEXT,
    data_postagem DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_tutor) REFERENCES tutor(id_usuario)
);
"""

INSERIR = """
INSERT INTO postagem_feed (id_tutor, imagem, descricao)
VALUES (?, ?, ?);
"""

ATUALIZAR = """
UPDATE postagem_feed
SET descricao = ?
WHERE id_postagem_feed = ?;
"""

EXCLUIR = """
DELETE FROM postagem_feed
WHERE id_postagem_feed = ?;
"""

OBTER_TODOS_PAGINADO = """
SELECT 
    pf.id_postagem_feed,
    pf.id_tutor,
    u.nome AS nome_tutor,
    pf.imagem,
    pf.descricao,
    pf.data_postagem
FROM postagem_feed pf
JOIN tutor t ON pf.id_tutor = t.id_usuario
JOIN usuario u ON t.id_usuario = u.id_usuario
ORDER BY pf.data_postagem DESC
LIMIT ? OFFSET ?;
"""


OBTER_POR_ID = """
SELECT 
    pf.id_postagem_feed,
    pf.id_tutor,
    u.nome AS nome_tutor,
    pf.imagem,
    pf.descricao,
    pf.data_postagem
FROM postagem_feed pf
JOIN tutor t ON pf.id_tutor = t.id_usuario
JOIN usuario u ON t.id_usuario = u.id_usuario
WHERE pf.id_postagem_feed = ?;
"""

```

# data\resposta_chamado_model.py

```py
from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class RespostaChamado:
    id: Optional[int] = None     
    id_chamado: int = 0
    titulo: str = ""
    descricao: str = ""
    data: Optional[date] = None  
```

# data\resposta_chamado_repo.py

```py
from typing import Optional, List
from data.resposta_chamado_model import RespostaChamado
from data.resposta_chamado_sql import *
from util import get_connection

def criar_tabelas() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False
    
def inserir_resposta(resposta: RespostaChamado) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            resposta.id_chamado,
            resposta.titulo,
            resposta.descricao,
            resposta.data
        ))
        return cursor.lastrowid
    
def obter_todas_respostas_paginado(limite: int, offset: int) -> List[RespostaChamado]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [
            RespostaChamado(
                id=row["id"],
                id_chamado=row["id_chamado"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                data=row["data"]
            )
            for row in rows
        ]


def obter_resposta_por_id(id_resposta: int) -> Optional[RespostaChamado]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_resposta,))
        row = cursor.fetchone()
        if row:
            return RespostaChamado(
                id=row["id"],
                id_chamado=row["id_chamado"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                data=row["data"]
            )
        return None
```

# data\resposta_chamado_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS resposta_chamado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_chamado INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    data DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_chamado) REFERENCES chamado(id)
);
"""

INSERIR = """
INSERT INTO resposta_chamado (id_chamado, titulo, descricao, data) 
VALUES (?, ?, ?, ?);
"""

ATUALIZAR = """
UPDATE resposta_chamado 
SET id_chamado, titulo = ?, descricao = ?, data = ?
WHERE id = ?
"""

EXCLUIR = """
DELETE FROM resposta_chamado
WHERE id = ?;
"""

OBTER_TODOS_PAGINADO = """
SELECT * 
FROM resposta_chamado 
ORDER BY data DESC
LIMIT ? OFFSET ?;
"""


OBTER_POR_ID = """
SELECT * 
FROM resposta_chamado
WHERE id = ?;

"""
```

# data\seguida_model.py

```py
from dataclasses import dataclass
from datetime import date

from data.tutor_model import Tutor
from data.veterinario_model import Veterinario

@dataclass
class Seguida:
    id_veterinario: Veterinario
    id_tutor: Tutor
    data_inicio: date
# verificar se data_inicio est´CORRETO, verificar se os ints estao corretos
```

# data\seguida_repo.py

```py
from typing import Optional, List
from data.seguida_model import Seguida
from data.seguida_sql import *
from data.tutor_model import Tutor
from util import get_connection
from data.veterinario_model import Veterinario


def criar_tabela() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False


def inserir(seguida: Seguida) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            seguida.id_veterinario,
            seguida.id_tutor))
        return cursor.rowcount > 0


def excluir(id_veterinario: int, id_tutor: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_veterinario, id_tutor))
        return cursor.rowcount > 0


def obter_todos_paginado(limite: int, offset: int) -> List[Seguida]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [
            Seguida(
                id_veterinario=Veterinario(id_usuario=row["id_veterinario"], nome=row["nome_veterinario"]),
                id_tutor=Tutor(id_usuario=row["id_tutor"], nome=row["nome_tutor"]),
                data_inicio=row["data_inicio"]
            )
            for row in rows]



def obter_por_id(id_veterinario: int, id_tutor: int) -> Optional[Seguida]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_veterinario, id_tutor))
        row = cursor.fetchone()
        if row:
            return Seguida(
                id_veterinario=Veterinario(id_usuario=row["id_veterinario"], nome=row["nome_veterinario"]),
                id_tutor=Tutor(id_usuario=row["id_tutor"], nome=row["nome_tutor"]),
                data_inicio=row["data_inicio"]
            )
        return None

```

# data\seguida_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS seguida (
  id_veterinario INTEGER NOT NULL,
  id_tutor INTEGER NOT NULL,
  data_inicio DATE DEFAULT CURRENT_DATE,
  PRIMARY KEY (id_veterinario, id_tutor),
  FOREIGN KEY (id_veterinario) REFERENCES veterinario(id_usuario),
  FOREIGN KEY (id_tutor) REFERENCES tutor(id_usuario)
);
"""

INSERIR = """
INSERT INTO seguida (id_veterinario, id_tutor)
VALUES (?, ?);
"""

EXCLUIR = """
DELETE FROM seguida 
WHERE id_veterinario = ? AND id_tutor = ?;
"""

OBTER_TODOS_PAGINADO = """
SELECT 
  s.id_veterinario,
  v.nome AS nome_veterinario,
  s.id_tutor,
  t.nome AS nome_tutor,
  s.data_inicio
FROM seguida s
JOIN veterinario v ON s.id_veterinario = v.id_usuario
JOIN tutor t ON s.id_tutor = t.id_usuario
ORDER BY s.data_inicio DESC
LIMIT ? OFFSET ?;
"""


OBTER_POR_ID = """
SELECT 
  s.id_veterinario,
  v.nome AS nome_veterinario,
  s.id_tutor,
  t.nome AS nome_tutor,
  s.data_inicio
FROM seguida s
JOIN veterinario v ON s.id_veterinario = v.id_usuario
JOIN tutor t ON s.id_tutor = t.id_usuario
WHERE s.id_veterinario = ? AND s.id_tutor = ?;
"""

```

# data\tutor_model.py

```py
from dataclasses import dataclass

from data.usuario_model import Usuario

@dataclass
class Tutor(Usuario):
    pass
```

# data\tutor_repo.py

```py
from typing import Any, Optional
from data import usuario_repo
from data.tutor_model import Tutor
import data.tutor_sql as tutor_sql
from data.usuario_model import Usuario
import data.usuario_sql as usuario_sql
from util import get_connection

  
def criar_tabela_tutor() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(tutor_sql.CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False

    
def inserir_tutor(tutor: Tutor) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        id_tutor = usuario_repo.inserir_usuario(tutor, cursor)
        cursor.execute(tutor_sql.INSERIR, (tutor.id_usuario, tutor.nome, tutor.email, tutor.senha))
        return cursor.lastrowid



def atualizar_tutor(tutor: Tutor) -> bool:
    return usuario_repo.atualizar_usuario(tutor)
    
def excluir_tutor(id_tutor: int) -> bool:
     with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(tutor_sql.EXCLUIR, (id_tutor,))
        return (cursor.rowcount > 0)

def obter_todos_tutores_paginado(limite: int, offset: int) -> list[Tutor]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(tutor_sql.OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        tutores = [
            Tutor(
                id_tutor=row["id_tutor"],
                nome=row["nome"],
                email=row["email"],
                telefone=row["telefone"]
            )
            for row in rows]
        return tutores

    
def obter_tutor_por_id(id_tutor: int) -> Optional[Tutor]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(tutor_sql.OBTER_POR_ID, (id_tutor,))
        row = cursor.fetchone()
        tutor = Tutor(
                id_tutor=row["id_tutor"], 
                telefone=row["telefone"])
        return tutor
```

# data\tutor_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS tutor (
    id_tutor INTEGER PRIMARY KEY,
    FOREIGN KEY (id_tutor) REFERENCES usuario(id_usuario)
);
"""

INSERIR = """
INSERT INTO tutor (id_tutor)
VALUES (?);
"""

EXCLUIR = """
DELETE FROM tutor 
WHERE id_tutor = ?;
"""

OBTER_TODOS_PAGINADO = """
SELECT 
    t.id_tutor,
    u.nome, 
    u.email, 
    u.telefone
FROM tutor t
INNER JOIN usuario u ON t.id_tutor = u.id_usuario
ORDER BY u.nome
LIMIT ? OFFSET ?;
"""


OBTER_POR_ID = """
SELECT 
t.id_tutor,
u.nome,
u.email,
u.telefone
FROM tutor t
INNER JOIN usuario u ON t.id_usuario = u.id_usuario
WHERE t.id_tutor = ?;
"""
```

# data\usuario_model.py

```py
from dataclasses import dataclass

@dataclass
class Usuario:
    id_usuario: int
    nome: str
    email: str
    senha: str
    telefone: str
```

# data\usuario_repo.py

```py
from typing import Any, Optional
from data.usuario_model import Usuario
from data.usuario_sql import *
from util import get_connection


def criar_tabela_usuario() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False

def inserir_usuario(usuario: Usuario, cursor: Any) -> Optional[int]:
    cursor.execute(INSERIR, (
        usuario.nome,
        usuario.email,
        usuario.senha,
        usuario.telefone))
    return cursor.lastrowid


def atualizar_usuario(usuario: Usuario, cursor: Any) -> bool:
    cursor.execute(ATUALIZAR, (
        usuario.nome,
        usuario.email,
        usuario.telefone,
        usuario.id_usuario))
    return (cursor.rowcount > 0)
    
def atualizar_senha_usuario(id_usuario: int, senha: str, cursor: Any) -> bool:
    cursor.execute(ATUALIZAR_SENHA, (senha, id_usuario))
    return (cursor.rowcount > 0)


def excluir_usuario(id_usuario: int, cursor: Any) -> bool:
    cursor.execute(EXCLUIR, (id_usuario,))
    return (cursor.rowcount > 0)

def obter_todos_usuarios_paginado(limite: int, offset: int) -> list[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        usuarios = [
            Usuario(
                id_usuario=row["id_usuario"], 
                nome=row["nome"], 
                email=row["email"], 
                senha=row["senha"], 
                telefone=row["telefone"]
            ) 
            for row in rows]
        return usuarios

def obter_usuario_por_id(id_usuario: int) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_usuario,))
        row = cursor.fetchone()
        usuario = Usuario(
            id=row["id_usuario"], 
            nome=row["nome"], 
            email=row["email"], 
            senha=row["senha"], 
            telefone=row["telefone"])
        return usuario

```

# data\usuario_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha CHAR(8) NOT NULL,
    telefone CHAR(11) NOT NULL
);
"""

INSERIR = """
INSERT INTO usuario (nome, email, senha, telefone)
VALUES (?, ?, ?, ?);
"""
ATUALIZAR = """
UPDATE usuario 
SET nome = ?, email = ?, telefone = ?
WHERE id_usuario = ?;
"""

ATUALIZAR_SENHA = """
UPDATE usuario 
SET senha = ?
WHERE id_usuario = ?;
"""

EXCLUIR = """
DELETE FROM usuario 
WHERE id_usuario = ?;
"""
OBTER_TODOS_PAGINADO = """
SELECT 
    id_usuario, 
    nome, 
    email, 
    senha, 
    telefone
FROM usuario 
ORDER BY nome
LIMIT ? OFFSET ?;
"""


OBTER_POR_ID = """
SELECT 
id_usuario, 
nome, 
email, 
telefone
FROM usuario 
WHERE id_usuario = ?;
"""
```

# data\verificacao_crmv_model.py

```py
from dataclasses import dataclass
from data.veterinario_model import Veterinario
from data.administrador_model import Administrador

@dataclass
class VerificacaoCRMV:
    id: int
    veterinario: Veterinario
    administrador: Administrador
    data_verificacao: str
    status_verificacao: str

```

# data\verificacao_crmv_repo.py

```py
from typing import Optional, List
from data.verificacao_crmv_model import VerificacaoCRMV
from data.verificacao_crmv_sql import *
from util import get_connection
from data.veterinario_model import Veterinario
from data.administrador_model import Administrador


def criar_tabela() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False

def inserir(verificacao: VerificacaoCRMV) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            verificacao.veterinario.id_veterinario,
            verificacao.administrador.id_admin,
            verificacao.status_verificacao
        ))
        return cursor.lastrowid


def atualizar(id_veterinario: int, novo_status: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (novo_status, id_veterinario))
        return cursor.rowcount > 0


def excluir(id_veterinario: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_veterinario,))
        return cursor.rowcount > 0


def obter_todos_paginado(limite: int, offset: int) -> List[VerificacaoCRMV]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_PAGINADO, (limite, offset))
        rows = cursor.fetchall()
        return [
            VerificacaoCRMV(
                id=row["id"],
                veterinario=Veterinario(id_veterinario=row["id_veterinario"], nome=row["nome_veterinario"]),
                administrador=Administrador(
                    id_admin=row["id_admin"],
                    nome=row["nome_admin"],
                    email=row["email_admin"]
                ),
                data_verificacao=row["data_verificacao"],
                status_verificacao=row["status_verificacao"]
            )
            for row in rows]



def obter_por_id(id: int) -> Optional[VerificacaoCRMV]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id,))
        row = cursor.fetchone()
        if row:
            return VerificacaoCRMV(
                id=row["id"],
                veterinario=Veterinario(id_veterinario=row["id_veterinario"]),
                administrador=Administrador(id_admin=row["id_admin"],nome=row["nome_admin"],email=row["email_admin"]),
                data_verificacao=row["data_verificacao"],
                status_verificacao=row["status_verificacao"])
        return None

```

# data\verificacao_crmv_sql.py

```py
CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS verificacao_crmv (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_veterinario INTEGER NOT NULL,
    id_admin INTEGER NOT NULL,
    data_verificacao DATE DEFAULT CURRENT_DATE,
    status_verificacao TEXT CHECK(status_verificacao IN ('pendente', 'verificado', 'rejeitado')),
    FOREIGN KEY (id_veterinario) REFERENCES veterinario(id_usuario),
    FOREIGN KEY (id_admin) REFERENCES administrador(id_admin)
);
"""

INSERIR = """
INSERT INTO verificacao_crmv (id_veterinario, id_admin, status_verificacao)
VALUES (?, ?, ?);
"""

ATUALIZAR = """
UPDATE verificacao_crmv 
SET status_verificacao = ?, id_admin = ?
WHERE id_veterinario = ?;
"""

EXCLUIR = """
DELETE FROM verificacao_crmv 
WHERE id_veterinario = ?;
"""

OBTER_TODOS_PAGINADO = """
SELECT 
    v.id,
    v.data_verificacao,
    v.status_verificacao,
    u.id_usuario AS id_veterinario,
    u.nome AS nome_veterinario,
    a.id_admin,
    a.nome AS nome_admin,
    a.email AS email_admin
FROM verificacao_crmv v
JOIN usuario u ON v.id_veterinario = u.id_usuario
JOIN administrador a ON v.id_admin = a.id_admin
ORDER BY v.data_verificacao DESC
LIMIT ? OFFSET ?;
"""


OBTER_POR_ID = """
SELECT 
    v.id,
    v.data_verificacao,
    v.status_verificacao,
    u.id_usuario AS id_veterinario,
    u.nome AS nome_veterinario,
    a.id_admin,
    a.nome AS nome_admin
FROM verificacao_crmv v
JOIN usuario u ON v.id_veterinario = u.id_usuario
JOIN administrador a ON v.id_admin = a.id_admin
WHERE v.id = ?;
"""
```

# data\veterinario_model.py

```py
from dataclasses import dataclass

from data.usuario_model import Usuario

@dataclass
class Veterinario(Usuario):
    pass
    crmv: str
    verificado: bool
    bio: str
    id_veterinario: int = 0
```

# data\veterinario_repo.py

```py
from typing import Optional, List
from data import usuario_repo
from data.usuario_model import Usuario
from data.veterinario_model import Veterinario
from data.veterinario_sql import *
from util import get_connection


def criar_tabela_tutor() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False

def inserir_veterinario(vet: Veterinario) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR,(vet.id_veterinario, vet.crmv, vet.verificado, vet.bio))
        return (cursor.rowcount > 0)


def atualizar_veterinario(vet: Veterinario) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        usuario = Usuario(
            vet.nome, 
            vet.email, 
            vet.senha)
        usuario_repo.ATUALIZAR(usuario, cursor)
        cursor.execute(ATUALIZAR, (
            vet.id_veterinario,
            vet.crmv,
            vet.verificado,
            vet.bio,
        ))
        return (cursor.rowcount > 0)

def excluir_veterinario(id_veterinario: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_veterinario,))
        usuario_repo.EXCLUIR(id_usuario, cursor)
        return (cursor.rowcount > 0)
    


def obter_todos() -> list[Veterinario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        veterinarios = [
            Veterinario(
                id_veterinario=row["id_veterinario"], 
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                crmv=row["crmv"],
                verificado=row["verificado"],
                bio=row["bio"])
                for row in rows]
        return veterinarios
    

def obter_por_id(id_veterinario: int) -> Optional[Veterinario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_veterinario,))
        row = cursor.fetchone()
        veterinario = Veterinario(
                id_veterinario=row["id_veterinario"], 
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                telefone=row["telefone"],
                crmv=row["crmv"],
                verificado=row["verificado"],
                bio=row["bio"])
        return veterinario
    


```

# data\veterinario_sql.py

```py
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
SELECT
v.id_veterinario,
u.nome, 
u.email, 
u.telefone, 
v.crmv, 
v.bio
FROM veterinario v
INNER JOIN usuario u ON v.id_veterinario = u.id_usuario
ORDER BY v.id_veterinario;
"""

OBTER_POR_ID = """
SELECT 
v.id_veterinario,
u.nome,
u.email,
u.telefone,
v.crmv,
v.bio
FROM veterinario v
INNER JOIN usuario u ON v.id_veterinario = u.id_usuario
WHERE v.id_veterinario = ?;
"""



```

# pytest.ini

```ini
[tool:pytest]
# Diretórios onde o pytest deve procurar por testes
testpaths = tests
# Padrões de arquivos de teste
python_files = test_*.py *_test.py
# Padrões de classes de teste
python_classes = Test*
# Padrões de funções de teste
python_functions = test_*
# Marcadores personalizados
markers =
    slow: marca testes que demoram para executar
    integration: marca testes de integração
    unit: marca testes unitários
# Opções padrão do pytest
addopts = 
    -v
    --strict-markers
    --disable-warnings
    --color=yes
# Filtros de warnings
filterwarnings =
    ignore::DeprecationWarning
    ignore::PendingDeprecationWarning
```

# README.md

```md
VetConecta
```

# requirements.txt

```txt
fastapi[standard]
uvicorn[standard]
jinja2
Babel
python-multipart
itsdangerous

# Dependências de teste
pytest
pytest-asyncio
pytest-cov
```

# tests\__init__.py

```py

```

# tests\conftest.py

```py
import pytest
import os
import sys
import tempfile


# Adiciona o diretório raiz do projeto ao PYTHONPATH
# Isso permite importar módulos do projeto nos testes
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Fixture para criar um banco de dados temporário para testes
@pytest.fixture
def test_db():
    # Cria um arquivo temporário para o banco de dados
    db_fd, db_path = tempfile.mkstemp(suffix='.db')
    # Configura a variável de ambiente para usar o banco de teste
    os.environ['TEST_DATABASE_PATH'] = db_path
    # Retorna o caminho do banco de dados temporário
    yield db_path    
    # Remove o arquivo temporário ao concluir o teste
    os.close(db_fd)
    if os.path.exists(db_path):
        os.unlink(db_path)

```

# tests\test_administrador_repo.py

```py
import os
import sys
from data.administrador_repo import *
from data.administrador_model import Administrador

class TestAdministradorRepo:
    def test_criar_tabela_administrador(self, test_db):
        #Arrange
        # Act
        resultado = criar_tabela_administrador()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_inserir_administrador(self, test_db):
        # Arrange
        criar_tabela_administrador()
        admin_teste = Administrador(0, "Admin Teste", "admin@gmail.com", "12345678")
            # Act
        id_admin_inserido = inserir_administrador(admin_teste)
            # Assert
        admin_db = obter_administrador_por_id(id_admin_inserido)
        assert admin_db is not None, "O administrador inserido não deveria ser None"
        assert admin_db.id_admin == 1, "O administrador inserido deveria ter um ID igual a 1"
        assert admin_db.nome == "Admin Teste", "O nome do administrador inserido não confere"
        assert admin_db.email == "admin@gmail.com", "O email do administrador inserido não confere"
        assert admin_db.senha == "12345678", "A senha do administrador inserido não confere"

    def test_atualizar_administrador(self, test_db):
        # Arrange
        criar_tabela_administrador()
        admin_teste = Administrador(0, "Admin Teste", "admin@gmail.com", "12345678")
        id_admin_inserido = inserir_administrador(admin_teste)
        admin_inserido = obter_administrador_por_id(id_admin_inserido)
            # Act
        admin_inserido.nome = "Admin Atualizado"
        admin_inserido.email = "emailAtualizado@gmail.com"
        admin_inserido.senha = "12345678"
        resultado = atualizar_administrador(admin_inserido)
        # Assert
        assert resultado == True, "A atualização do administrador deveria retornar True"
        admin_db = obter_administrador_por_id(id_admin_inserido)
        assert admin_db.nome == "Admin Atualizado", "O nome do administrador atualizado não confere"
        assert admin_db.email == "emailAtualizado@gmail.com", "O email do administrador atualizado não confere"
        assert admin_db.senha == "12345678", "A senha do administrador atualizado não confere"

    def test_atualizar_senha(self, test_db):
        # Arrange
        criar_tabela_administrador()
        admin_teste = Administrador(0, "Admin Teste", "admin@gmail.com", "12345678")
        id_admin_inserido = inserir_administrador(admin_teste)
        # Act
        nova_senha = "87654321"
        resultado = atualizar_senha(id_admin_inserido, nova_senha)  
        # Assert
        assert resultado == True, "A atualização da senha deveria retornar True"
        admin_db = obter_administrador_por_id(id_admin_inserido)
        assert admin_db.senha == nova_senha, "A senha do administrador atualizado não confere"



    def test_excluir_administrador(self, test_db):
        # Arrange
        criar_tabela_administrador()
        admin_teste = Administrador(0, "Admin Teste", "admin@gmail.com", "12345678")
        id_admin_inserido = inserir_administrador(admin_teste)
        # Act
        resultado = excluir_administrador(id_admin_inserido)
        # Assert    
        assert resultado == True, "A exclusão do administrador deveria retornar True"
        admin_excluido = obter_administrador_por_id(id_admin_inserido)  
        assert admin_excluido == None, "O administrador excluído deveria ser None"


    def test_obter_todos_administradores(self, test_db):
        # Arrange
        criar_tabela_administrador()
        admin1 = Administrador(0, "Admin 1", "admin@gmail.com", "12345678")
        admin2 = Administrador(0, "Admin 2", "admin@@gmail.com", "87654321")
        inserir_administrador(admin1)
        inserir_administrador(admin2)   
        # Act
        administradores = obter_todos_administradores()
        # Assert
        assert len(administradores) == 2, "Deveria haver 2 administradores"
        assert administradores[0].nome == "Admin 1", "O nome do primeiro administrador não confere"
        assert administradores[1].nome == "Admin 2", "O nome do segundo administrador não confere"

    def test_obter_administrador_por_id(self, test_db):
        # Arrange
        criar_tabela_administrador()
        admin_teste = Administrador(0, "Admin Teste", "admin@gmail.com", "12345678")
        id_admin_inserido = inserir_administrador(admin_teste)
        # Act   
        admin_obtido = obter_administrador_por_id(id_admin_inserido)
        # Assert
        assert admin_obtido is not None, "O administrador obtido não deveria ser None"
        assert admin_obtido.id_admin == id_admin_inserido, "O ID do administrador obtido não confere"
        assert admin_obtido.nome == admin_teste.nome, "O nome do administrador obtido não confere"
        assert admin_obtido.email == admin_teste.email, "O email do administrador obtido não confere"
        assert admin_obtido.senha == admin_teste.senha, "A senha do administrador obtido não confere"


```

# tests\test_categoria_artigo_repo.py

```py
import os
import sys
from data.categoria_artigo_repo import *
from data.categoria_artigo_model import CategoriaArtigo

class TestCategoriaArtigoRepo:
    def test_criar_tabela(self, test_db):
        #Arrange
        # Act
        resultado = criar_tabela_categoria_artigo()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_inserir_categoria(self, test_db):
        # Arrange
        criar_tabela_categoria_artigo()
        categoria_teste = CategoriaArtigo(0,"Categoria Teste", "Descrição Teste")
        # Act
        id_categoria_inserida = inserir_categoria(categoria_teste)
        # Assert
        categoria_db = obter_categoria_por_id(id_categoria_inserida)
        assert categoria_db is not None, "A categoria inserida não deveria ser None"
        assert categoria_db.id == 1, "A categoria inserida deveria ter um ID igual a 1"
        assert categoria_db.nome == "Categoria Teste", "O nome da categoria inserida não confere"
        assert categoria_db.descricao == "Descrição Teste", "O campo de descrição não pode ser vazio"

    def test_atualizar_categoria(self, test_db):
        # Arrange
        criar_tabela_categoria_artigo()
        categoria_teste = CategoriaArtigo(0, "Categoria Teste", "Descrição Teste")
        id_categoria_inserida = inserir_categoria(categoria_teste)
        categoria_inserida = obter_categoria_por_id(id_categoria_inserida)
        # Act
        categoria_inserida.nome = "Categoria Atualizada"
        categoria_inserida.descricao = "Descrição Atualizada"
        resultado = atualizar_categoria(categoria_inserida)
        # Assert
        assert resultado == True, "A atualização da categoria deveria retornar True"
        categoria_db = obter_categoria_por_id(id_categoria_inserida)
        assert categoria_db.nome == "Categoria Atualizada", "O nome da categoria atualizada não confere"
        assert categoria_db.descricao == "Descrição Atualizada", "A descrição da categoria atualizada não confere"


    def test_excluir_categoria(self, test_db):
        # Arrange
        criar_tabela_categoria_artigo()
        categoria_teste = CategoriaArtigo(0, "Categoria Teste", "Descrição Teste")
        id_categoria_inserida = inserir_categoria(categoria_teste)
        # Act
        resultado = excluir_categoria(id_categoria_inserida)
        # Assert
        assert resultado == True, "A exclusão da categoria deveria retornar True"
        categoria_excluida = obter_categoria_por_id(id_categoria_inserida)
        assert categoria_excluida == None, "A categoria excluída deveria ser None"

    def test_obter_todas_categorias(self, test_db):
        # Arrange
        criar_tabela_categoria_artigo()
        categoria1 = CategoriaArtigo(0, "Categoria 1", "Descrição 1")
        categoria2 = CategoriaArtigo(0, "Categoria 2", "Descrição 2")
        inserir_categoria(categoria1)
        inserir_categoria(categoria2)
        # Act
        categorias = obter_todas_categorias()
        # Assert
        assert len(categorias) == 2, "Deveria retornar duas categorias"
        assert categorias[0].nome == "Categoria 1", "O nome da primeira categoria não confere"
        assert categorias[1].nome == "Categoria 2", "O nome da segunda categoria não confere"

    def test_obter_categoria_por_id(self, test_db):
        # Arrange
        criar_tabela_categoria_artigo()
        categoria_teste = CategoriaArtigo(0, "Categoria Teste", "Descrição Teste")
        id_categoria_inserida = inserir_categoria(categoria_teste)
        # Act
        categoria_db = obter_categoria_por_id(id_categoria_inserida)
        # Assert
        assert categoria_db is not None, "A categoria obtida não deveria ser diferente de None"
        assert categoria_db.id == id_categoria_inserida, "O ID da categoria obtida não confere"
        assert categoria_db.nome == categoria_teste.nome, "O nome da categoria obtida não confere"
        


```

# tests\test_comentario_repo.py

```py
import os
import sys
import pytest

from data.comentario_repo import *

class TestComentarioRepo:
    def test_criar_tabela(self, test_db):
        #Arrange
        # Act
        resultado = criar_tabela()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"



    def test_inserir(self, test_db):
        # Arrange: prepara o banco e cria a tabela
        criar_tabela()
        comentario_teste = Comentario(0, "Usuario", "Artigo", "Texto", "Data Comentario", "Data Moderação")
        # Act: insere o tutor de exemplo
        id_comentario_inserido = inserir(comentario_teste)
        # Assert: verifica se o tutor foi inserido corretamente
        comentario_db = obter_por_id(id_comentario_inserido)

        assert comentario_db is not None, "O comentário inserido não deveria ser None"
        assert comentario_db.usuario > "Usuario", "O usuário inserido deveria ter um ID válido"
        assert comentario_db.artigo == "Artigo", "O nome do artigo não confere"
        assert comentario_db.texto == "Texto", "O texto do comentario não confere"
        assert comentario_db.data_comentario == "Data Comentario", "A data do comentário não confere"
        assert comentario_db.data_moderacao == "Data Moderação", "A data da moderação não confere"



    def test_atualizar(self, test_db):
        # Arrange
        criar_tabela()
        comentario_teste = Comentario(0, "Texto Teste", "Data da Moderacao Teste")
        comentario_inserido = inserir(comentario_teste)
        # Act
        comentario_inserido.texto = "Texto Atualizado"
        comentario_inserido.data_moderacao = "Data da Moderacao Atualizado"
        resultado = atualizar(comentario_inserido)
        # Assert
        assert resultado == True, "A atualização do comentário deveria retornar True"
        comentario_db = obter_por_id(comentario_inserido)
        assert comentario_db.texto == "Texto atualizado", "O Texto do comentário atualizado não confere"
        assert comentario_db.data_moderacao == "Data da Moderacao Atualizada", "A Data da Moderacao do comentário atualizada não confere"



    def test_excluir(self, test_db):
        # Arrange
        criar_tabela()
        comentario_teste = Comentario(0, "Usuario", "Artigo", "Texto", "Data Comentario", "Data Moderação")
        id_comentario_inserido = inserir(comentario_teste)
        # Act
        resultado = excluir(id_comentario_inserido)
        # Assert
        assert resultado == True, "A exclusão do comentario deveria retornar True"
        comentario_excluido = obter_por_id(id_comentario_inserido)
        assert comentario_excluido == None, "A categoria excluída deveria ser None"





    def test_obter_por_id(self, test_db):
        # Arrange
        criar_tabela()
        comentario_teste = Comentario(0, "Usuario", "Artigo", "Texto", "Data Comentario", "Data Moderação")
        id_comentario_inserido = inserir(comentario_teste)
        # Act   
        comentario_obtido = obter_por_id(id_comentario_inserido)
        # Assert
        assert comentario_obtido is not None, "O comentario obtido não deveria ser None"
        assert comentario_obtido.id == id_comentario_inserido, "O ID do comentario obtido não confere"
        assert comentario_obtido.usuario == comentario_teste.usuario, "O usuário obtido não confere"
        assert comentario_obtido.artigo == comentario_teste.artigo, "O artigo obtido não confere"
        assert comentario_obtido.texto == comentario_teste.texto, "O texto obtido não confere"
        assert comentario_obtido.data_comentario == comentario_teste.data_comentario, "A data do comentario obtido não confere"
        assert comentario_obtido.data_moderacao == comentario_teste.data_moderacao, "A data da moderação obtida não confere"


```

# tests\test_curtida_artigo_repo.py

```py
import os
import sys
from data.curtida_artigo_repo import *
from data.curtida_artigo_model import CurtidaArtigo

class TestCurtidaArtigoRepo:
    def test_criar_tabela_curtida_artigo(self, test_db):
        #Arrange
        # Act
        resultado = criar_tabela()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"



    def test_inserir(self, test_db):
        # Arrange
        criar_tabela()
        curtida_artigo_teste = CurtidaArtigo(0, "", "admin@gmail.com", "12345678")
            # Act
        id_admin_inserido = inserir_administrador(admin_teste)
            # Assert
        admin_db = obter_administrador_por_id(id_admin_inserido)
        assert admin_db is not None, "O administrador inserido não deveria ser None"
        assert admin_db.id_admin == 1, "O administrador inserido deveria ter um ID igual a 1"
        assert admin_db.nome == "Admin Teste", "O nome do administrador inserido não confere"
        assert admin_db.email == "admin@gmail.com", "O email do administrador inserido não confere"
        assert admin_db.senha == "12345678", "A senha do administrador inserido não confere"

```

# tests\test_denuncia_repo.py

```py
import os
import sys
from data.administrador_model import Administrador
from data.denuncia_repo import *
from data.usuario_model import *
from data.administrador_repo import *
from data.denuncia_model import Denuncia
from data.usuario_model import Usuario

class TestDenunciaRepo:
    def test_criar_tabela_denuncia(self, test_db):
        # Arrange
        # Act
        resultado = criar_tabela_denuncia()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_inserir_denuncia(self, test_db):
    # Arrange
    criar_tabela_usuario()       # Certifique que a tabela usuario existe
    criar_tabela_administrador() # Certifique que a tabela administrador existe
    criar_tabela_denuncia()      # Crie a tabela denuncia
    
    # Insere um usuário para a FK id_usuario
    usuario_id = inserir_usuario(Usuario(
        id_usuario=0, nome="Usuário Teste", email="teste@teste.com", senha="12345678", telefone="12345678900"
    ))
    
    # Insere um administrador para a FK id_admin
    admin_id = inserir_administrador(Administrador(
        id_admin=0, nome="Admin Teste", email="admin@teste.com", senha="admin123"
    ))
    
    # Cria uma denúncia com os IDs válidos
    denuncia_teste = Denuncia(
        id_denuncia=0,
        id_usuario=usuario_id,
        id_admin=admin_id,
        motivo="Motivo Teste",
        data_denuncia="2025-06-30",
        status="pendente"  
    )
    
    # Act
    id_denuncia_inserida = inserir_denuncia(denuncia_teste)
    
    # Assert
    denuncia_db = obter_denuncia_por_id(id_denuncia_inserida)
    assert denuncia_db is not None, "A denúncia inserida não deveria ser None"
    assert denuncia_db.id_usuario.id_usuario == usuario_id, "O ID do usuário da denúncia inserida não confere"
    assert denuncia_db.id_denuncia == 1, "A denúncia inserida deveria ter um ID igual a 1"
    assert denuncia_db.motivo == "Motivo Teste", "O motivo da denuncia da denúncia inserida não confere"
    assert denuncia_db.status == "pendente", "O status da denúncia inserida não confere"

    
      

```

# tests\test_tutor_repo.py

```py
from data.tutor_model import Tutor
from data.tutor_repo import *
from data.usuario_repo import *
from data.usuario_model import Usuario



class TestTutorRepo:
    def test_criar_tabela(self, test_db):
        # Act
        resultado = criar_tabela_tutor()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_inserir_tutor(self, test_db):
        # Arrange
        criar_tabela_tutor()

        tutor_exemplo = Tutor(1, "Tutor Teste", "tutor@gmail.com", "12345678", "123456789")
            # Act
        id_tutor_inserido = inserir_tutor(tutor_exemplo)
            # Assert
        tutor_obtido = obter_tutor_por_id(id_tutor_inserido)
        assert tutor_obtido is not None, "O tutor inserido não deveria ser None"
        assert tutor_obtido.id_usuario == 1, "O tutor inserido deveria ter um ID igual a 1"
        assert tutor_obtido.nome == "Tutor Teste", "O nome do tutor inserido não confere"
        assert tutor_obtido.email == "tutor@gmail.com", "O email do tutor inserido não confere"
        assert tutor_obtido.senha == "12345678", "A senha do tutor inserido não confere"
        assert tutor_obtido.telefone == "123456789", "O telefone do tutor inserido não confere"



    def test_atualizar_tutor(self, test_db):
        # Arrange
        criar_tabela_tutor()
        tutor_exemplo = Tutor(1, "Tutor Teste", "tutor@gmail.com", "12345678", "123456789")
        id_tutor_inserido = inserir_tutor(tutor_exemplo)
        tutor_inserido = obter_tutor_por_id(id_tutor_inserido)
        # Act
        tutor_inserido.nome = "Tutor Atualizado"
        tutor_inserido.email = "email Atualizada"
        tutor_inserido.senha = "12345678"
        tutor_inserido.telefone = "123456789"
        resultado = atualizar_tutor(tutor_obtido)
        # Assert
        assert resultado == True, "A atualização do tutor deveria retornar True"
        tutor_obtido = obter_tutor_por_id(tutor_inserido)
        assert tutor_obtido.nome == "Tutor Atualizado", "O nome do tutor atualizado não confere"
        assert tutor_obtido.email == "Email Atualizada", "O email do tutor atualizado não confere"
        assert tutor_obtido.senha == "Senha Atualizada", "A senha do tutor atualizado não confere"
        assert tutor_obtido.telefone == "Telefone Atualizado", "O telefone do tutor atualizado não confere"
    
    def test_atualizar_senha(self, test_db):
        criar_tabela_tutor
        tutor_exemplo = Tutor(1, "Tutor Teste", "tutor@gmail.com", "12345678", "123456789")
        id_tutor_inserido = inserir_tutor(tutor_exemplo)
        #Act
        nova_senha ="87654321"
        resultado = atualizar_senha_usuario(id_tutor_inserido, nova_senha)
        #Assert
        assert resultado == True, "A atualização da senha deveria retornar True"
        tutor_db = obter_tutor_por_id(id_tutor_inserido)
        assert tutor_db.senha == nova_senha, "A senha do tutor atualizado não confere"

    def test_excluir_tutor(self, test_db):
        # Arrange
        tutor_exemplo = Tutor(1, "Tutor Teste", "tutor@gmail.com", "12345678", "123456789")
        id_tutor_inserido = inserir_tutor(tutor_exemplo)
        # Act
        resultado = excluir_tutor(id_tutor_inserido)
        # Assert
        assert resultado == True, "A exclusão do tutor deveria retornar True"
        tutor_excluido = obter_tutor_por_id(id_tutor_inserido)
        assert tutor_excluido == None, "O tutor excluído deveria ser None"

    def test_obter_todos_tutores(self, test_db):
        # Arrange
        criar_tabela_tutor
        tutor1 = Tutor(1, "Tutor 1", "tutor1@gmail.com", "12345678", "123456789")
        tutor2 = Tutor(2, "Tutor 2", "tutor2@gmail.com", "12345678", "123456789")
        inserir_tutor(tutor1)
        inserir_tutor(tutor2)
        # Act
        tutores = obter_todos_tutores_paginado()
        # Assert
        assert len(tutores) == 2, "Deveria retornar duas categorias"
        assert tutores[0].nome == "Tutor 1", "O nome do primeiro tutor não confere"
        assert tutores[1].nome == "Tutor 2", "O nome do segundo tutor não confere"
    
    def test_obter_tutor_por_id(self, test_db):
        #Arrange
        criar_tabela_tutor()
        tutor_teste = (1, "Tutor Teste", "tutor@gmail.com", "12345678", "123456789")
        id_tutor_inserido = inserir_tutor(tutor_teste)
        # Act
        tutor_obtido = obter_tutor_por_id(id_tutor_inserido)
        # Assert
        assert tutor_obtido.nome == "Tutor Atualizado", "O nome do tutor atualizado não confere"
        assert tutor_obtido.email == "Email Atualizada", "O email do tutor atualizado não confere"
        assert tutor_obtido.senha == "Senha Atualizada", "A senha do tutor atualizado não confere"
        assert tutor_obtido.telefone == "Telefone Atualizado", "O telefone do tutor atualizado não confere"        
```

# tests\test_usuario_repo.py

```py
import os
import sys
from data.usuario_repo import *
from data.usuario_model import Usuario

class TestUsuarioRepo:
    def test_criar_tabela(self, test_db):
        # Arrange
        # Act
        resultado = criar_tabela_usuario()
        # Assert
        assert resultado == True, "A criação da tabela de usuários deveria retornar True"


    def test_inserir_usuario(self, test_db, usuario_teste):
        #Arrange 
        criar_tabela_usuario()
        #Act
        id_usuario_inserido = inserir_usuario(usuario_teste)
        #Assert
        usuario_db = obter_usuario_por_id(id_usuario_inserido)
        assert usuario_db is not None, "O usuario inserido não deveria ser None"
        assert usuario_db.id_usuario == 1, "O usuario inserido deveria ter um ID igual a 1"
        assert usuario_db.nome == "Nome Teste", "O nome do usuario inserido não confere"
        assert usuario_db.email == "emailteste@gmail", "O email do usuario não confere"
        assert usuario_db.senha == "12345678", "A senha do usuario não confere"
        assert usuario_db.telefone == "99912345678", "O telefone do usuario não confere"

    def test_atualizar_usuario(self, test_db):
        #Arrange
        criar_tabela_usuario()
        usuario_teste = Usuario(0, "Nome Teste", "emailteste@gmail", "12345678", "99912345678")
        id_usuario_inserido = inserir_usuario(usuario_teste)
        usuario_inserido = obter_todos_usuarios_paginado
        #Act
        usuario_inserido.nome = "Usuario Atualizado"
        usuario_inserido.email = "emailteste@gmail"
        usuario_inserido.senha = "12345678"
        usuario_inserido.telefone = "99912345678"
        resultado = atualizar_senha_usuario(usuario_inserido)
        #Assert
        assert resultado == True, "A atualização da categoria deveria retornar True"
        usuario_db = obter_usuario_por_id(id_usuario_inserido)
        assert usuario_db.nome == "Nome Teste", "O nome do usuario inserido não confere"
        assert usuario_db.email == "emailteste@gmail", "O email do usuario não confere"
        assert usuario_db.senha == "12345678", "A senha do usuario não confere"
        assert usuario_db.telefone == "99912345678", "O telefone do usuario não confere"

    def test_atualizar_senha_usuario(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(0, "Teste", "teste@email.com", "senha_antiga", "11999999999")
        id_usuario = inserir_usuario(usuario)
        
        # Act
        nova_senha = "senha_nova123"
        resultado = atualizar_senha_usuario(id_usuario, nova_senha, test_db.cursor())
        
        # Assert
        assert resultado is True, "A atualização da senha deveria retornar True"
        usuario_atualizado = obter_usuario_por_id(id_usuario)
        assert usuario_atualizado.senha == nova_senha, "A senha do usuário não foi atualizada corretamente"


    def test_excluir_usuario(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(0, "Teste", "teste@email.com", "senha123", "11999999999")
        id_usuario = inserir_usuario(usuario)

        # Act
        resultado = excluir_usuario(id_usuario, test_db.cursor())

        # Assert
        assert resultado is True, "A exclusão do usuário deveria retornar True"
        usuario_excluido = obter_usuario_por_id(id_usuario)
        assert usuario_excluido is None, "O usuário excluído deveria ser None"


    def test_obter_todos_usuarios_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario1 = Usuario(0, "Usuário 1", "u1@email.com", "senha1", "1111111111")
        usuario2 = Usuario(0, "Usuário 2", "u2@email.com", "senha2", "2222222222")
        inserir_usuario(usuario1)
        inserir_usuario(usuario2)

        # Act
        usuarios = obter_todos_usuarios_paginado(limite=10, offset=0)

        # Assert
        assert len(usuarios) == 2, "Deveria retornar dois usuários"
        assert usuarios[0].nome == "Usuário 1", "O nome do primeiro usuário não confere"
        assert usuarios[1].nome == "Usuário 2", "O nome do segundo usuário não confere"


    def test_obter_usuario_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(0, "Teste", "teste@email.com", "senha123", "11999999999")
        id_usuario = inserir_usuario(usuario)

        # Act
        usuario_db = obter_usuario_por_id(id_usuario)

        # Assert
        assert usuario_db is not None, "O usuário obtido não deveria ser None"
        assert usuario_db.id == id_usuario, "O ID do usuário obtido não confere"
        assert usuario_db.nome == usuario.nome, "O nome do usuário obtido não confere"
```

# util.py

```py
import sqlite3
import os

def get_connection():
    conn = None
    try:
        database_path = os.environ.get('TEST_DATABASE_PATH', 'dados.db')
        conn = sqlite3.connect(database_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")  # Ativa as chaves estrangeiras
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn
```

