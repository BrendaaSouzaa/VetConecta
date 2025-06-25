from typing import Any, Optional
from data import usuario_repo
from data.tutor_model import Tutor
<<<<<<< HEAD
import data.tutor_sql as tutor_sql
import data.usuario_sql as usuario_sql
from util import get_connection
=======
from data.tutor_sql import *
from data.usuario_model import Usuario
from data.util import get_connection
>>>>>>> b6b400e565b0d901d87fa390e028bbba04e7abfb

  
def criar_tabela_tutor() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(tutor_sql.CRIAR_TABELA)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False

    
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
<<<<<<< HEAD
        cursor.execute(tutor_sql.ATUALIZAR, (
            tutor.telefone, 
            tutor.endereco, 
=======
        cursor.execute(ATUALIZAR, (
>>>>>>> b6b400e565b0d901d87fa390e028bbba04e7abfb
            tutor.id_tutor
            ))
        return cursor.rowcount > 0
def atualizar_tutor(tutor: Tutor) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
<<<<<<< HEAD
        cursor.execute(tutor_sql.EXCLUIR, (id_tutor,))
=======
        usuario = Usuario(tutor.id_usuario, 
            tutor.nome, 
            tutor.email, 
            tutor.senha,
            tutor.telefone)
        usuario_repo.alterar_usuario(usuario, cursor)
        cursor.execute(ATUALIZAR, (
            tutor.id_usuario))
>>>>>>> b6b400e565b0d901d87fa390e028bbba04e7abfb
        return (cursor.rowcount > 0)
    
def excluir_tutor(id_tutor: int, cursor: Any) -> bool:
    cursor.execute(EXCLUIR, (id_tutor,))
    return (cursor.rowcount > 0)

def obter_todos_tutores() -> list[Tutor]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(tutor_sql.OBTER_TODOS)
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
        cursor.execute(tutor_sql.OBTER_POR_ID, (id_tutor,))
        row = cursor.fetchone()
        tutor = Tutor(
                id_tutor=row["id_tutor"], 
                telefone=row["telefone"])
        return tutor