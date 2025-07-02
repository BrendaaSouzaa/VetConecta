import os
import sys
import pytest

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
        comentario_teste = Comentario(0, "Texto Teste", "Data da Moderacao Teste")
        comentario_inserido = inserir(comentario_teste)
        # Act
        comentario_inserido.texto = "Texto Atualizado"
        comentario_inserido.data_moderacao = "Data da Moderacao Atualizado"
        resultado = atualizar(comentario_inserido)
        # Assert
        assert resultado == True, "A atualização do comentário deveria retornar True"
        comentario_db = obter_por_id(comentario_inserido)
        assert comentario_db.texto == "Texto atualizado", "O Texto do comentário atualizado não confere"
        assert comentario_db.data_moderacao == "Data da Moderacao Atualizada", "A Data da Moderacao do comentário atualizada não confere"



    def test_excluir(self, test_db):
        # Arrange
        criar_tabela()
        comentario_teste = Comentario(0, "Usuario", "Artigo", "Texto", "Data Comentario", "Data Moderação")
        id_comentario_inserido = inserir(comentario_teste)
        # Act
        resultado = excluir(id_comentario_inserido)
        # Assert
        assert resultado == True, "A exclusão do comentario deveria retornar True"
        comentario_excluido = obter_por_id(id_comentario_inserido)
        assert comentario_excluido == None, "A categoria excluída deveria ser None"





    def test_obter_por_id(self, test_db):
        # Arrange
        criar_tabela()
        comentario_teste = Comentario(0, "Usuario", "Artigo", "Texto", "Data Comentario", "Data Moderação")
        id_comentario_inserido = inserir(comentario_teste)
        # Act   
        comentario_obtido = obter_por_id(id_comentario_inserido)
        # Assert
        assert comentario_obtido is not None, "O comentario obtido não deveria ser None"
        assert comentario_obtido.id == id_comentario_inserido, "O ID do comentario obtido não confere"
        assert comentario_obtido.usuario == comentario_teste.usuario, "O usuário obtido não confere"
        assert comentario_obtido.artigo == comentario_teste.artigo, "O artigo obtido não confere"
        assert comentario_obtido.texto == comentario_teste.texto, "O texto obtido não confere"
        assert comentario_obtido.data_comentario == comentario_teste.data_comentario, "A data do comentario obtido não confere"
        assert comentario_obtido.data_moderacao == comentario_teste.data_moderacao, "A data da moderação obtida não confere"

