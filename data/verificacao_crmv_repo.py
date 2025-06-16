from typing import Optional, List
from data.verificacao_crmv_model import VerificacaoCRMV
from data.verificacao_crmv_sql import *
from data.util import get_connection


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


def inserir(verificacao: VerificacaoCRMV) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            verificacao.id_veterinario,
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


def obter_todos() -> List[VerificacaoCRMV]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [VerificacaoCRMV(
            id=row["id"],
            id_veterinario=row["id_veterinario"],
            data_verificacao=row["data_verificacao"],
            status_verificacao=row["status_verificacao"]
        ) for row in rows]


def obter_por_id(id: int) -> Optional[VerificacaoCRMV]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id,))
        row = cursor.fetchone()
        if row:
            return VerificacaoCRMV(
                id=row["id"],
                id_veterinario=row["id_veterinario"],
                data_verificacao=row["data_verificacao"],
                status_verificacao=row["status_verificacao"]
            )
        return None
