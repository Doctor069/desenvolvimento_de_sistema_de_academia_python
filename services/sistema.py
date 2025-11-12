from models.aluno import Aluno
from models.reserva import Reserva
from services.persistencia import salvar_dados, carregar_dados

# SistemaAcademia - gerencia os objetos das classes anteriores

class SistemaAcademia:
    """
        Classe principal que gerencia todas as operações da academia.
        Gerencia os objetos Aluno e Reserva e aplica as regras de negócio.
    """

    def __init__(self):
        """
            Construtor. Carrega os dados salvos (alunos e reservas) dos arquivos .txt ao iniciar o sistema.
        """
        self.alunos, self.reservas = carregar_dados()
        print(f"[Info] Sistema iniciado. {len(self.alunos)} alunos e {len(self.reservas)} reservas carregadas.")

    def _salvar_automaticamente(self):
        """
            Método privado auxiliar. Chama a função de persistência
            para salvar o estado atual das listas de alunos e reservas.
        """
        salvar_dados(self.alunos, self.reservas)

    def cadastrar_aluno(self, nome, cpf, idade, plano):
        """
            Cadastra um novo aluno no sistema.
            Inclui validação para impedir CPF duplicado.

            Args:
                nome (str): Nome do aluno.
                cpf (str): CPF do aluno.
                idade (int): Idade do aluno.
                plano (str): Plano do aluno.

            Returns:
                Aluno: O objeto Aluno criado, ou None se o cadastro falhar.
        """

        if self.buscar_aluno_por_cpf(cpf):
            print(f"\n[Erro] Já existe um aluno cadastrado com o CPF {cpf}.")
            return None

        if not nome or not cpf or idade <= 0:
            print("\n[Erro] Dados do aluno inválidos (Nome, CPF ou Idade).")
            return None

        novo_aluno = Aluno(nome, cpf, idade, plano)
        self.alunos.append(novo_aluno)

        self._salvar_automaticamente()
        print(f"\n[Sucesso] Aluno '{nome}' cadastrado.")
        return novo_aluno

    def buscar_aluno_por_cpf(self, cpf):
        """Encontra um aluno na lista pelo CPF."""
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                return aluno
        return None

    def adicionar_reserva(self, aluno_cpf, atividade, data, horario):
        """Cria uma nova Reserva e a adiciona na lista."""

        aluno_encontrado = self.buscar_aluno_por_cpf(aluno_cpf)

        if not aluno_encontrado:
            print(f"\n[Erro] Aluno com CPF {aluno_cpf} não encontrado. Reserva não realizada.")
            return None

        if not atividade or not data or not horario:
            print(f"\n[Erro] Dados da reserva inválidos (Atividade, Data ou Horário).")
            return None

        nova_reserva = Reserva(aluno_encontrado, atividade, data, horario)
        self.reservas.append(nova_reserva)

        self._salvar_automaticamente()

        print(f"\n[Sucesso] Reserva para '{atividade}' no nome de '{aluno_encontrado.nome}' realizada.")
        return nova_reserva

    def listar_reservas(self):
        """Retorna a lista de todas as reservas cadastradas."""
        return self.reservas

    def buscar_reservas_por_cpf(self, cpf):
        """Retorna todas as reservas de um aluno específico."""
        reservas_aluno = []
        for res in self.reservas:
            if res.aluno.cpf == cpf:
                reservas_aluno.append(res)
        return reservas_aluno

    def atualizar_status_reserva(self, reserva: Reserva, novo_status: str):
        """Atualiza o status de um objeto Reserva."""
        status_validos = ["Reservado", "Confirmado", "Concluído", "Cancelado"]

        if novo_status in status_validos:
            reserva.status = novo_status
            self._salvar_automaticamente()
            print(
                f"\n[Sucesso] Status da reserva ({reserva.atividade} em {reserva.data}) atualizado para '{novo_status}'.")
            return True
        else:
            print(f"\n[Erro] Status '{novo_status}' é inválido. Válidos: {status_validos}")
            return False

    def gerar_relatorio_contagem(self):
        """Adicionar contagem de reservas por aluno."""

        if not self.alunos:
            return {}

        contagem = {aluno.nome: 0 for aluno in self.alunos}

        for reserva in self.reservas:
            if reserva.status != "Cancelado" and reserva.status != "Concluído":
                nome_aluno = reserva.aluno.nome
                if nome_aluno in contagem:
                    contagem[nome_aluno] += 1

        return contagem