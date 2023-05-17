class Estudante:
    def __init__(self, nome, fator_rh, curso, data_nascimento, sus_numero):
        self.nome = nome
        self.fator_rh = fator_rh
        self.curso = curso
        self.data_nascimento = data_nascimento
        self.sus_numero = sus_numero

    def __str__(self) -> str:
        return f'Estudante {self.nome}'
