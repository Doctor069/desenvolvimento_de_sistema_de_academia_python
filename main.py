from services.sistema import SistemaAcademia

def carga_inicial(sistema):
    """Adiciona dados fictícios APENAS na primeira execução."""
    print("[Info] Primeiro uso detectado. Carregando dados fictícios...")

    aluno1 = sistema.cadastrar_aluno("Raposo Cleik", "111.111.111-11", 25, "Mensal")
    aluno2 = sistema.cadastrar_aluno("Floquinho Carvalho", "222.222.222-22", 30, "Trimestral")

    if aluno1 and aluno2:
        sistema.adicionar_reserva(aluno1.cpf, "Musculação", "20/11/2025", "18:00")
        sistema.adicionar_reserva(aluno2.cpf, "Spinning", "21/11/2025", "09:00")

    print("-" * 30)

def exibir_menu():
    """Mostra as opções para o usuário."""
    print("\n--- BEM-VINDO AO SISTEMA DA ACADEMIA ---")
    print("1. Cadastrar Novo Aluno")
    print("2. Fazer Nova Reserva")
    print("3. Listar Todas as Reservas")
    print("4. Atualizar Status de uma Reserva")
    print("5. Ver Relatório de Reservas por Aluno")
    print("0. Sair")

def main():
    """Função principal que executa o loop do menu."""

    # 1. Cria a instância (que agora CARREGA os dados do .txt)
    sistema = SistemaAcademia()

    # 2. Verifica se precisa da carga inicial
    if not sistema.alunos:  # Se a lista de alunos estiver vazia
        carga_inicial(sistema)

    # 3. Loop principal do menu
    while True:
        exibir_menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            # --- Cadastrar Aluno ---
            print("\n--- Cadastro de Aluno ---")
            nome = input("Nome completo: ")
            cpf = input("CPF (ex: 123.456.789-00): ")

            # Validação de idade
            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("\n[Erro] Idade inválida. Deve ser um número.")
                continue  # Volta ao menu

            plano = input("Plano (Mensal, Trimestral, etc.): ")

            sistema.cadastrar_aluno(nome, cpf, idade, plano)

        elif opcao == '2':
            # --- Adicionar Reserva ---
            print("\n--- Nova Reserva de Aula ---")
            cpf = input("Digite o CPF do aluno: ")
            atividade = input("Atividade (ex: Musculação, Natação): ")
            data = input("Data (DD/MM/AAAA): ")
            horario = input("Horário (HH:MM): ")

            sistema.adicionar_reserva(cpf, atividade, data, horario)

        elif opcao == '3':
            # --- Listar Reservas ---
            print("\n--- Reservas Atuais ---")
            reservas = sistema.listar_reservas()

            if not reservas:
                print("[Info] Nenhuma reserva cadastrada no momento.")
            else:
                for res in reservas:
                    print(
                        f"- Aluno: {res.aluno.nome} | Atividade: {res.atividade} | Data: {res.data} | Status: {res.status}")

        elif opcao == '4':
            # --- Atualizar Status da Reserva ---
            print("\n--- Atualizar Status da Reserva ---")
            cpf = input("Digite o CPF do aluno para ver suas reservas: ")

            reservas_encontradas = sistema.buscar_reservas_por_cpf(cpf)

            if not reservas_encontradas:
                print("\n[Info] Nenhuma reserva encontrada para este CPF.")
                continue

            print("\nReservas encontradas para este aluno:")
            for indice, res in enumerate(reservas_encontradas):
                print(f"  {indice + 1}. Atividade: {res.atividade} | Data: {res.data} | Status Atual: {res.status}")

            try:
                escolha_str = input("\nDigite o número da reserva que deseja alterar (ou 0 para cancelar): ")
                escolha = int(escolha_str)

                if escolha == 0:
                    continue  # Volta ao menu

                reserva_escolhida = reservas_encontradas[escolha - 1]
            except (ValueError, IndexError):
                print("\n[Erro] Escolha inválida.")
                continue

            novo_status = input("Digite o novo status (Reservado, Confirmado, Concluído, Cancelado): ").capitalize()

            sistema.atualizar_status_reserva(reserva_escolhida, novo_status)

        elif opcao == '5':
            # --- Relatório de Contagem ---
            print("\n--- Relatório: Reservas Ativas por Aluno ---")

            relatorio = sistema.gerar_relatorio_contagem()

            if not relatorio:
                print("[Info] Nenhum aluno cadastrado para gerar relatório.")
            else:
                for nome, contagem in relatorio.items():
                    print(f"- {nome}: {contagem} reservas")

        elif opcao == '0':
            print("\n[Info] Obrigado por usar o sistema. Até logo!")
            break

        else:
            print("\n[Erro] Opção inválida! Por favor, tente novamente.")


# -----------------------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[ERRO FATAL] O programa encontrou um erro inesperado: {e}")
        input("Pressione ENTER para sair.")