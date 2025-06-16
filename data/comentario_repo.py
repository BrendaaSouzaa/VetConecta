from typing import Optional, List
from data.comentario_model import Comentario
from data.comentario_sql import *
from data.util import get_connection


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


def inserir(comentario: Comentario) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            comentario.id_usuario,
            comentario.id_artigo,
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


def obter_todos() -> List[Comentario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [Comentario(
            id=row["id"],
            id_usuario=row["id_usuario"],
            id_artigo=row["id_artigo"],
            texto=row["texto"],
            data_comentario=row["data_comentario"],
            data_moderacao=row["data_moderacao"]
        ) for row in rows]


def obter_por_id(id: int) -> Optional[Comentario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id,))
        row = cursor.fetchone()
        if row:
            return Comentario(
                id=row["id"],
                id_usuario=row["id_usuario"],
                id_artigo=row["id_artigo"],
                texto=row["texto"],
                data_comentario=row["data_comentario"],
                data_moderacao=row["data_moderacao"]
            )
        return None
