from typing import Optional, List
from data.seguida_model import Seguida
from data.seguida_sql import *
from data.tutor_model import Tutor
from data.util import get_connection
from data.veterinario_model import Veterinario


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


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


def obter_todos() -> List[Seguida]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [Seguida(
            id_veterinario=Veterinario(id_usuario=row["id_veterinario"], nome=row["nome_veterinario"]),
            id_tutor=Tutor(id_usuario=row["id_tutor"], nome=row["nome_tutor"]),
            data_inicio=row["data_inicio"])
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
