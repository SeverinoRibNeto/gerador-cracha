class Estudante:
    def __init__(self, matricula: int, nome: str, fator_rh: str,
                 curso: str, data_nascimento: str, sus_numero: str):
        self.matricula = matricula
        self.nome = nome
        self.fator_rh = fator_rh
        self.curso = curso
        self.data_nascimento = data_nascimento
        self.sus_numero = sus_numero

    def __str__(self) -> str:
        return f'Estudante {self.nome}'
