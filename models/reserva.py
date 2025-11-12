from models.aluno import Aluno

# Reserva - atributos: atividade, data, horário, status

class Reserva:
    """
        Representa uma reserva de atividade para um aluno.
        Atributos: atividade, data, horário, status.
        Implementa a associação entre Reserva e Aluno.
    """

    def __init__(self, aluno: Aluno, atividade: str, data: str, horario: str):
        """
            Construtor da classe Reserva.

            Args:
                aluno (Aluno): O objeto Aluno que está fazendo a reserva.
                atividade (str): A atividade reservada (ex: Musculação).
                data (str): A data da reserva (formato DD/MM/AAAA).
                horario (str): O horário da reserva (formato HH:MM).
        """
        # Esta é a associação
        self.aluno = aluno

        self.atividade = atividade
        self.data = data
        self.horario = horario

        # O status inicial padrão será "Reservado"
        self.status = "Reservado"

    def __repr__(self):
        """Retorna uma representação em string do objeto Reserva."""
        return f"Reserva(aluno='{self.aluno.nome}', atividade='{self.atividade}', data='{self.data}')"