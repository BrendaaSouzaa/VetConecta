from typing import Optional, List
from data.chamado_model import Chamado, RespostaChamado
from data.chamado_sql import *
from data.util import get_connection


def criar_tabelas() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        cursor.execute(CRIAR_TABELA_RESPOSTA)
        return True


def inserir_chamado(chamado: Chamado) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chamado (id_usuario, titulo, descricao) VALUES (?, ?, ?)",
            (chamado.id_usuario, chamado.titulo, chamado.descricao)
        )
        return cursor.lastrowid


def inserir_resposta(resposta: RespostaChamado) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO resposta_chamado (id_chamado, titulo, descricao) VALUES (?, ?, ?)",
            (resposta.id_chamado, resposta.titulo, resposta.descricao)
        )
        return cursor.lastrowid


def atualizar_status_chamado(id_chamado: int, novo_status: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (novo_status, id_chamado))
        return cursor.rowcount > 0


def excluir_chamado(id_chamado: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_chamado,))
        return cursor.rowcount > 0


def obter_todos_chamados() -> List[Chamado]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chamado ORDER BY data DESC")
        rows = cursor.fetchall()
        return [Chamado(
            id=row["id"],
            id_usuario=row["id_usuario"],
            titulo=row["titulo"],
            descricao=row["descricao"],
            status=row["status"],
            data=row["data"]
        ) for row in rows]


def obter_todas_respostas() -> List[RespostaChamado]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM resposta_chamado ORDER BY data DESC")
        rows = cursor.fetchall()
        return [RespostaChamado(
            id=row["id"],
            id_chamado=row["id_chamado"],
            titulo=row["titulo"],
            descricao=row["descricao"],
            data=row["data"]
        ) for row in rows]


def obter_chamado_por_id(id_chamado: int) -> Optional[Chamado]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chamado WHERE id = ?", (id_chamado,))
        row = cursor.fetchone()
        if row:
            return Chamado(
                id=row["id"],
                id_usuario=row["id_usuario"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                status=row["status"],
                data=row["data"]
            )
        return None


def obter_resposta_por_id(id_resposta: int) -> Optional[RespostaChamado]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM resposta_chamado WHERE id = ?", (id_resposta,))
        row = cursor.fetchone()
        if row:
            return RespostaChamado(
                id=row["id"],
                id_chamado=row["id_chamado"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                data=row["data"]
            )
        return None
