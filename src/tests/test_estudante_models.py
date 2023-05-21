import pytest
from models.estudante import Estudante


class TestEstudante:
    def test_criacao_classe_estudante_deve_retornar_valores_iguais_aos_passados_em_parametros(self):
        # Given
        # Valores esperados
        matricula = 111
        nome = "Teste"
        fator_rh = "A+"
        curso = "Analise de Sistema"
        data_nascimento = "01/01/2001"
        sus_numero = "123456789"

        # When
        # criação do objeto
        teste_estudante = Estudante(
            111, "Teste", "A+", "Analise de Sistema", "01/01/2001", "123456789")

        # Then
        # Teste de inicializacao
        assert teste_estudante.matricula == matricula
        assert teste_estudante.nome == nome
        assert teste_estudante.fator_rh == fator_rh
        assert teste_estudante.curso == curso
        assert teste_estudante.data_nascimento == data_nascimento
        assert teste_estudante.sus_numero == sus_numero

        # Teste de representação em String
        assert str(teste_estudante) == "Estudante Teste"
