from data.tutor_model import Tutor
from data import tutor_repo, usuario_repo


class TestTutorRepo:
    def test_criar_tabela(self, test_db):
        # Act
        resultado = tutor_repo.criar_tabela_tutor()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"

    def test_inserir_tutor(self, test_db, tutor_exemplo):
        # Arrange: prepara o banco e cria a tabela
        tutor_repo.criar_tabela_tutor()
        # Act: insere o tutor de exemplo
        id_tutor_inserido = tutor_repo.inserir_tutor(tutor_exemplo)
        # Assert: verifica se o tutor foi inserido corretamente
        tutor_inserido = tutor_repo.obter_tutor_por_id(id_tutor_inserido)
        assert tutor_inserido is not None, "O tutor inserido não deveria ser None"
        assert tutor_inserido.id_usuario > 0, "O tutor inserido deveria ter um ID válido"
        assert tutor_inserido.nome == tutor_exemplo.nome, "O nome do tutor não confere"
        assert tutor_inserido.email == tutor_exemplo.email, "O email do tutor não confere"
        assert tutor_inserido.telefone == tutor_exemplo.telefone, "O telefone não confere"
        assert tutor_inserido.cpf == tutor_exemplo.cpf, "O CPF não confere"


    def test_atualizar_tutor(self, test_db):
        # Arrange
        tutor_teste = tutor_model.Tutor(0, "Tutor Teste", "Descrição Teste")
        id_tutor_inserido = tutor_repo.inserir_tutor(tutor_teste)
        tutor_inserido = tutor_repo.obter_tutor_por_id(id_tutor_inserido)
        # Act
        tutor_inserido.nome = "Tutor Atualizado"
        tutor_inserido.descricao = "Descrição Atualizada"
        resultado = tutor_repo.atualizar_tutor(tutor_inserido)
        # Assert
        assert resultado == True, "A atualização do tutor deveria retornar True"
        tutor_db = tutor_repo.obter_tutor_por_id(id_tutor_inserido)
        assert tutor_db.nome == "Tutor Atualizado", "O nome do tutor atualizado não confere"
        assert tutor_db.descricao == "Descrição Atualizada", "A descrição do tutor atualizado não confere"
    def test_excluir_tutor(self, test_db):
        # Arrange
        tutor_teste = tutor_model.Tutor(0, "Tutor Teste", "Descrição Teste")
        id_tutor_inserido = tutor_repo.inserir_tutor(tutor_teste)
        # Act
        resultado = tutor_repo.excluir_tutor(id_tutor_inserido)
        # Assert
        assert resultado == True, "A exclusão do tutor deveria retornar True"
        tutor_excluido = tutor_repo.obter_tutor_por_id(id_tutor_inserido)
        assert tutor_excluido is None, "O tutor excluído deveria ser None"
    def test_obter_todos_tutores(self, test_db):
        # Arrange
        tutor1 = tutor_model.Tutor(0, "Tutor 1", "Descrição 1")
        tutor2 = tutor_model.Tutor(0, "Tutor 2", "Descrição 2")
        tutor_repo.inserir_tutor(tutor1)
        tutor_repo.inserir_tutor(tutor2)
        # Act
        tutores = tutor_repo.obter_todos_tutores()
        # Assert
        assert len(tutores) == 2, "Deveria retornar duas categorias"
        assert tutores[0].nome == "Tutor 1", "O nome do primeiro tutor não confere"
        assert tutores[1].nome == "Tutor 2", "O nome do segundo tutor não confere"
        