from models.aluno import Aluno
from models.reserva import Reserva
import os  # Usaremos 'os' para garantir que a pasta 'data' exista

# Adicionar persistência simples (arquivo.txt).

# Caminhos dos arquivos
DATA_DIR = "data"
ALUNOS_FILE = os.path.join(DATA_DIR, "alunos.txt")
RESERVAS_FILE = os.path.join(DATA_DIR, "reservas.txt")


def _garantir_pasta_data():
    """
        Função auxiliar interna (privada).
        Verifica se o diretório 'data' existe. Se não existir, tenta criá-lo.
        Levanta uma exceção (interrompe o programa) se a criação falhar.
    """
    if not os.path.exists(DATA_DIR):
        try:
            os.makedirs(DATA_DIR)
            print(f"[Info] Pasta '{DATA_DIR}' criada.")
        except IOError as e:
            print(f"[Erro Fatal] Não foi possível criar a pasta '{DATA_DIR}': {e}")
            raise


def salvar_dados(lista_alunos, lista_reservas):
    """
    Salva o estado atual das listas de alunos e reservas nos arquivos .txt.
    Implementa a persistência simples em arquivo.

    Formato Aluno: nome;cpf;idade;plano
    Formato Reserva: aluno_cpf;atividade;data;horario;status
    O CPF é usado para salvar a associação.

    Args:
        lista_alunos (list[Aluno]): A lista de objetos Aluno a ser salva.
        lista_reservas (list[Reserva]): A lista de objetos Reserva a ser salva.
    """
    _garantir_pasta_data()  # Garante que a pasta existe antes de salvar

    # --- Salva Alunos ---
    try:
        with open(ALUNOS_FILE, "w", encoding="utf-8") as f:
            for aluno in lista_alunos:
                f.write(f"{aluno.nome};{aluno.cpf};{aluno.idade};{aluno.plano}\n")
    except IOError as e:
        print(f"[Erro] Falha ao salvar alunos: {e}")

    # --- Salva Reservas ---
    try:
        with open(RESERVAS_FILE, "w", encoding="utf-8") as f:
            for res in lista_reservas:
                # Salvamos o CPF para manter a associação
                f.write(f"{res.aluno.cpf};{res.atividade};{res.data};{res.horario};{res.status}\n")
    except IOError as e:
        print(f"[Erro] Falha ao salvar reservas: {e}")


def carregar_dados():
    """
        Carrega os dados dos arquivos .txt e recria os objetos em memória.
        [FONTE: 25] Implementa a leitura da persistência.

        A lógica reconstrói a associação [FONTE: 41, 43] ao carregar
        alunos primeiro e, em seguida, vincular as reservas a eles
        através do CPF (usando um mapa/dicionário).

        Returns:
            tuple: Uma tupla contendo (lista_alunos_carregados, lista_reservas_carregadas).
                   Retorna listas vazias se os arquivos não existirem ou houver erro.
    """
    _garantir_pasta_data()  # Garante que a pasta existe antes de ler

    alunos_carregados = []
    mapa_alunos_por_cpf = {}    # Mapa para recriar a associação

    # --- Carrega Alunos ---
    try:
        with open(ALUNOS_FILE, "r", encoding="utf-8") as f:
            for linha in f:
                if not linha.strip(): continue  # Ignora linhas em branco
                nome, cpf, idade_str, plano = linha.strip().split(';')
                novo_aluno = Aluno(nome, cpf, int(idade_str), plano)

                alunos_carregados.append(novo_aluno)
                mapa_alunos_por_cpf[cpf] = novo_aluno   # Guarda no mapa

    except FileNotFoundError:
        print("[Info] 'alunos.txt' não encontrado. Começando com lista vazia.")
    except IOError as e:
        print(f"[Erro] Falha ao carregar alunos: {e}")
    except ValueError as e:
        print(f"[Erro] Formato de dados inválido em 'alunos.txt': {e}")

    reservas_carregadas = []

    # --- Carrega Reservas ---
    try:
        with open(RESERVAS_FILE, "r", encoding="utf-8") as f:
            for linha in f:
                if not linha.strip(): continue  # Ignora linhas em branco
                cpf, atividade, data, horario, status = linha.strip().split(';')

                # Usa o mapa para recriar a associação
                aluno_obj = mapa_alunos_por_cpf.get(cpf)

                if aluno_obj:
                    nova_reserva = Reserva(aluno_obj, atividade, data, horario)
                    nova_reserva.status = status # Restaura o status salvo
                    reservas_carregadas.append(nova_reserva)
                else:
                    # Isso pode acontecer se um aluno for removido mas a reserva não
                    print(f"[Aviso] Reserva para CPF {cpf} ignorada (aluno não encontrado).")

    except FileNotFoundError:
        print("[Info] 'reservas.txt' não encontrado. Começando com lista vazia.")
    except IOError as e:
        print(f"[Erro] Falha ao carregar reservas: {e}")
    except ValueError as e:
        print(f"[Erro] Formato de dados inválido em 'reservas.txt': {e}")

    return alunos_carregados, reservas_carregadas