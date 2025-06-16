from typing import Optional, List
from data.tutor_model import Tutor
from data.tutor_sql import *
from data.util import get_connection


def criar_tabela_tutor() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


def inserir_tutor(tutor: Tutor) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (tutor.id_usuario, tutor.telefone, tutor.endereco))
        return cursor.rowcount > 0


def atualizar_tutor(tutor: Tutor) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (tutor.telefone, tutor.endereco, tutor.id_usuario))
        return cursor.rowcount > 0


def excluir_tutor(id_usuario: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_usuario,))
        return cursor.rowcount > 0


def obter_todos_tutores() -> List[Tutor]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [Tutor(**row) for row in rows]


def obter_tutor_por_id(id_usuario: int) -> Optional[Tutor]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_usuario,))
        row = cursor.fetchone()
        return Tutor(**row) if row else None
