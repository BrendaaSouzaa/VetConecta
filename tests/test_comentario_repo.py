import os
import sys

from data.comentario_repo import *

class TestComentarioRepo:
    def test_criar_tabela(self, test_db):
        #Arrange
        # Act
        resultado = criar_tabela()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_inserir(self, test_db):
        # Arrange: prepara o banco e cria a tabela
        criar_tabela()
        comentario_teste = Comentario(0, "Usuario", "Artigo", "Texto", "Data Comentario", "Data Moderação")
        # Act: insere o tutor de exemplo
        id_comentario_inserido = inserir(comentario_teste)
        # Assert: verifica se o tutor foi inserido corretamente
        comentario_db = obter_por_id(id_comentario_inserido)

        assert comentario_db is not None, "O comentário inserido não deveria ser None"
        assert comentario_db.usuario > "Usuario", "O usuário inserido deveria ter um ID válido"
        assert comentario_db.artigo == "Artigo", "O nome do artigo não confere"
        assert comentario_db.texto == "Texto", "O texto do comentario não confere"
        assert comentario_db.data_comentario == "Data Comentario", "A data do comentário não confere"
        assert comentario_db.data_moderacao == "Data Moderação", "A data da moderação não confere"

    def test_atualizar(self, test_db):
        # Arrange
        criar_tabela()
        comentario_teste = Comentario(0, "Usuário Teste", "Artigo Teste", "Texto Teste")
        comentario_inserido = inserir(comentario_teste)
        # Act
        comentario_inserido.usuario = "Usuário Atualizado"
        comentario_inserido.artigo = "Artigo Atualizado"
        comentario_inserido.texto = "Texto Atualizado"
        resultado = atualizar_comentario(comentario_inserido)
        # Assert
        assert resultado == True, "A atualização do comentário deveria retornar True"
        comentario_db = obter_comentario_por_id(id_comentario_inserido)
        assert comentario_db == nova_senha, "A senha do administrador atualizado não confere"