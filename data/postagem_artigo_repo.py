from typing import Optional, List
from data.categoria_artigo_model import CategoriaArtigo
from data.postagem_artigo_model import PostagemArtigo
from data.postagem_artigo_sql import *
from data.util import get_connection


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


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
            postagem.categoria_artigo.id,
            postagem.visualizacoes,
            postagem.id
        ))
        return cursor.rowcount > 0


def excluir(id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id,))
        return cursor.rowcount > 0


def obter_todos() -> List[PostagemArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [PostagemArtigo(
            id=row["id"],
            id_veterinario=row["id_veterinario"],
            titulo=row["titulo"],
            conteudo=row["conteudo"],
            categoria=CategoriaArtigo(id=row["categoria_id"],),
            data_publicacao=row["data_publicacao"],
            visualizacoes=row["visualizacoes"]
        ) for row in rows]


def obter_por_id(id: int) -> Optional[PostagemArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id,))
        row = cursor.fetchone()
        if row:
            return PostagemArtigo(
                id=row["id"],
                id_veterinario=row["id_veterinario"],
                titulo=row["titulo"],
                conteudo=row["conteudo"],
                categoria=CategoriaArtigo(id=row["categoria_id"],),
                data_publicacao=row["data_publicacao"],
                visualizacoes=row["visualizacoes"]
            )
        return None
