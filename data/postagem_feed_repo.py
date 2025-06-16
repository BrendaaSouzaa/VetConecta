from typing import Optional, List
from data.postagem_feed_model import PostagemFeed
from data.postagem_feed_sql import *
from data.util import get_connection


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


def inserir(postagem: PostagemFeed) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            postagem.id_usuario,
            postagem.texto
        ))
        return cursor.lastrowid


def atualizar(postagem: PostagemFeed) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            postagem.texto,
            postagem.id
        ))
        return cursor.rowcount > 0


def excluir(id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id,))
        return cursor.rowcount > 0


def obter_todos() -> List[PostagemFeed]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [PostagemFeed(
            id=row["id"],
            id_usuario=row["id_usuario"],
            texto=row["texto"],
            data_postagem=row["data_postagem"]
        ) for row in rows]


def obter_por_id(id: int) -> Optional[PostagemFeed]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id,))
        row = cursor.fetchone()
        if row:
            return PostagemFeed(
                id=row["id"],
                id_usuario=row["id_usuario"],
                texto=row["texto"],
                data_postagem=row["data_postagem"]
            )
        return None
