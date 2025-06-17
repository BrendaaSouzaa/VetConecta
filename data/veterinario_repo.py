from typing import Optional, List
from data.veterinario_model import Veterinario
from data.veterinario_sql import *
from data.util import get_connection


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


def inserir(vet: Veterinario) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            vet.id_usuario,
            vet.crmv,
            vet.verificado,
            vet.bio
        ))
        return cursor.rowcount > 0


def atualizar(vet: Veterinario) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            vet.crmv,
            vet.verificado,
            vet.bio,
            vet.id_usuario
        ))
        return cursor.rowcount > 0


def excluir(id_usuario: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_usuario,))
        return cursor.rowcount > 0


def obter_todos() -> List[Veterinario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [Veterinario(
            id_usuario=row["id_usuario"],
            crmv=row["crmv"],
            verificado=row["verificado"],
            bio=row["bio"]
        ) for row in rows]


def obter_por_id(id_usuario: int) -> Optional[Veterinario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_usuario,))
        row = cursor.fetchone()
        if row:
            return Veterinario(**row)
        return None
