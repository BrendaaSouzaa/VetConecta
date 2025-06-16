from typing import Optional, List
from data.administrador_model import Administrador
from data.administrador_sql import *
from data.util import get_connection


def criar_tabela_administrador() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


def inserir_administrador(admin: Administrador) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (admin.id_usuario, admin.nivel_acesso))
        return cursor.rowcount > 0


def atualizar_administrador(admin: Administrador) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (admin.nivel_acesso, admin.id_usuario))
        return cursor.rowcount > 0


def excluir_administrador(id_usuario: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_usuario,))
        return cursor.rowcount > 0


def obter_todos_administradores() -> List[Administrador]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [Administrador(**row) for row in rows]


def obter_administrador_por_id(id_usuario: int) -> Optional[Administrador]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_usuario,))
        row = cursor.fetchone()
        return Administrador(**row) if row else None
