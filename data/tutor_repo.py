from typing import Optional, List
from data.tutor_model import Tutor
from data.tutor_sql import *
from data.util import get_connection

  
def criar_tabela_tutor() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return cursor.rowcount > 0

def inserir_usuario(tutor: Tutor) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            tutor.id_tutor, 
            tutor.telefone, 
            tutor.endereco
            ))
        return cursor.lastrowid


def atualizar_tutor(tutor: Tutor) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            tutor.telefone, 
            tutor.endereco, 
            tutor.id_tutor
            ))
        return cursor.rowcount > 0


def excluir_tutor(id_tutor: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
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
                telefone=row["telefone"], 
                endereco=row["endereco"])
            for row in rows]
        return tutores
    
def obter_tutor_por_id(id_tutor: int) -> Optional[Tutor]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_tutor,))
        row = cursor.fetchone()
        tutor = Tutor(
                id_tutor=row["id_tutor"], 
                telefone=row["telefone"], 
                endereco=row["endereco"])
        return tutor