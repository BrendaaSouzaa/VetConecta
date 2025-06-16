from typing import Optional, List
from data.curtida_artigo_model import CurtidaArtigo
from data.curtida_artigo_sql import *
from data.util import get_connection


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


def inserir(curtida: CurtidaArtigo) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (curtida.id_usuario, curtida.id_artigo))
        return cursor.rowcount > 0


def remover(id_usuario: int, id_artigo: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (id_usuario, id_artigo))
        return cursor.rowcount > 0


def obter_todos() -> List[CurtidaArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [CurtidaArtigo(
            id_usuario=row["id_usuario"],
            id_artigo=row["id_artigo"],
            data_curtida=row["data_curtida"]
        ) for row in rows]


def obter_por_id(id_usuario: int, id_artigo: int) -> Optional[CurtidaArtigo]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_usuario, id_artigo))
        row = cursor.fetchone()
        if row:
            return CurtidaArtigo(
                id_usuario=row["id_usuario"],
                id_artigo=row["id_artigo"],
                data_curtida=row["data_curtida"]
            )
        return None
