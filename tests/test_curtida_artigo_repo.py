import os
import sys
from data.curtida_artigo_repo import *
from data.curtida_artigo_model import CurtidaArtigo

class TestCurtidaArtigoRepo:
    def test_criar_tabela_curtida_artigo(self, test_db):
        #Arrange
        # Act
        resultado = criar_tabela()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"



    def test_inserir(self, test_db):
        # Arrange
        criar_tabela()
        curtida_artigo_teste = CurtidaArtigo(0, "", "admin@gmail.com", "12345678")
            # Act
        id_admin_inserido = inserir_administrador(admin_teste)
            # Assert
        admin_db = obter_administrador_por_id(id_admin_inserido)
        assert admin_db is not None, "O administrador inserido não deveria ser None"
        assert admin_db.id_admin == 1, "O administrador inserido deveria ter um ID igual a 1"
        assert admin_db.nome == "Admin Teste", "O nome do administrador inserido não confere"
        assert admin_db.email == "admin@gmail.com", "O email do administrador inserido não confere"
        assert admin_db.senha == "12345678", "A senha do administrador inserido não confere"
