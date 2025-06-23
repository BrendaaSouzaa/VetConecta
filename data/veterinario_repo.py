from typing import Optional, List
from data.veterinario_model import Veterinario
from data.veterinario_sql import *
from data.util import get_connection


def criar_tabela_tutor() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return (cursor.rowcount > 0)

def inserir_veterinario(vet: Veterinario) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            vet.id_veterinario,
            vet.crmv,
            vet.verificado,
            vet.bio
            ))
        return cursor.lastrowid


def atualizar_veterinario(vet: Veterinario) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR, (
            vet.crmv,
            vet.verificado,
            vet.bio,
            vet.id_veterinario
        ))
        return (cursor.rowcount > 0)

def excluir_veterinario(id_veterinario: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR, (id_veterinario,))
        return (cursor.rowcount > 0)
    


def obter_todos_veterinarios() -> list[Veterinario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        veterinarios = [
            Veterinario(
                id_veterinario=row["id_veterinario"], 
                crmv=row["crmv"],
                verificado=row["verificado"],
                bio=row["bio"])
            for row in rows]
        return veterinarios
    
def obter_veterinario_por_id(id_veterinario: int) -> Optional[Veterinario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_veterinario,))
        row = cursor.fetchone()
        veterinario = Veterinario(
                id_veterinario=row["id_veterinario"], 
                crmv=row["crmv"],
                verificado=row["verificado"],
                bio=row["bio"])
        return veterinario
    

