# Aluno - atributos: nome, CPF, idade, plano

class Aluno:
    """
        Representa um aluno da academia.
        Atributos: nome, CPF, idade, plano.
    """
    def __init__(self, nome, cpf, idade, plano):
        """
            Construtor da classe Aluno.

            Args:
                nome (str): O nome completo do aluno.
                cpf (str): O CPF do aluno (usado como identificador).
                idade (int): A idade do aluno.
                plano (str): O tipo de plano (ex: Mensal, Trimestral).
        """
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.plano = plano

    def __repr__(self):
        """Retorna uma representação em string do objeto Aluno."""
        return f"Aluno(nome='{self.nome}', cpf='{self.cpf}')"