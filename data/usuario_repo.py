from typing import Optional, List
from data.usuario_model import Usuario
from data.usuario_sql import *
from data.util import get_connection


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return True


def inserir(usuario: Usuario) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            usuario.nome,
            usuario.email,
            usuario.senha,
            usuario.telefone,
            usuario.tipo_usuario))
        id_inserido = cursor.lastrowid
        return id_inserido


def atualizar(usuario: Usuario) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            usuario.nome,
            usuario.email,
            usuario.senha,
            usuario.telefone,
            usuario.tipo_usuario,
            usuario.id
        ))
        return cursor.rowcount > 0


def excluir(id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id,))
        return cursor.rowcount > 0


def obter_todos() -> List[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [Usuario(
            id=row["id"],
            nome=row["nome"],
            email=row["email"],
            telefone=row["telefone"],
            tipo_usuario=row["tipo_usuario"]
        ) for row in rows]


def obter_por_id(id: int) -> Optional[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id,))
        row = cursor.fetchone()
        if row:
            return Usuario(**row)
        return None
