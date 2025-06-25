from typing import Any, Optional
from data import usuario_repo
from data.tutor_model import Tutor
from data.tutor_sql import *
from data.usuario_model import Usuario
from data.util import get_connection

  
def criar_tabela_tutor() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return cursor.rowcount > 0

    
def inserir_tutor(tutor: Tutor) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        usuario = Usuario(0, 
            tutor.nome, 
            tutor.email, 
            tutor.senha)
        id_usuario = usuario_repo.inserir_usuario(usuario, cursor)
        cursor.execute(INSERIR, (
            id_usuario,
            tutor.telefone))
        return id_usuario

def atualizar_tutor(tutor: Tutor) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            tutor.id_tutor
            ))
        return cursor.rowcount > 0
def atualizar_tutor(tutor: Tutor) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        usuario = Usuario(tutor.id_usuario, 
            tutor.nome, 
            tutor.email, 
            tutor.senha,
            tutor.telefone)
        usuario_repo.alterar_usuario(usuario, cursor)
        cursor.execute(ATUALIZAR, (
            tutor.id_usuario))
        return (cursor.rowcount > 0)
    
def excluir_tutor(id_tutor: int, cursor: Any) -> bool:
    cursor.execute(EXCLUIR, (id_tutor,))
    return (cursor.rowcount > 0)

def obter_todos_tutores() -> list[Tutor]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        tutores = [
            Tutor(
                id_tutor=row["id_tutor"], 
                telefone=row["telefone"])
            for row in rows]
        return tutores
    
def obter_tutor_por_id(id_tutor: int) -> Optional[Tutor]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_tutor,))
        row = cursor.fetchone()
        tutor = Tutor(
                id_tutor=row["id_tutor"], 
                telefone=row["telefone"])
        return tutor