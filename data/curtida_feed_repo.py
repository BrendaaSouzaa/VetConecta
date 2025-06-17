from typing import Optional, List
from data.curtida_feed_model import CurtidaFeed
from data.curtida_feed_sql import *
from data.util import get_connection


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


def inserir(curtida: CurtidaFeed) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            curtida.id_usuario,
            curtida.id_feed
        ))
        return cursor.rowcount > 0


def excluir(id_usuario: int, id_feed: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_usuario, id_feed))
        return cursor.rowcount > 0


def obter_todos() -> List[CurtidaFeed]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [CurtidaFeed(
            id_usuario=row["id_usuario"],
            id_feed=row["id_feed"],
            data_curtida=row["data_curtida"]
        ) for row in rows]


def obter_por_id(id_usuario: int, id_feed: int) -> Optional[CurtidaFeed]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_usuario, id_feed))
        row = cursor.fetchone()
        if row:
            return CurtidaFeed(
                id_usuario=row["id_usuario"],
                id_feed=row["id_feed"],
                data_curtida=row["data_curtida"]
            )
        return None
