# 🏋️‍♂️ Sistema de Reservas para Academia (CLI em Python)

Este é um projeto acadêmico que simula um sistema de gerenciamento de reservas para uma academia, desenvolvido inteiramente em Python e executado no terminal (CLI).

O objetivo principal é aplicar os conceitos de **Programação Orientada a Objetos (POO)** e **Métodos Ágeis** em um desenvolvimento incremental, focado na manutenção e evolução do software.

## ✨ Conceitos de POO Aplicados

O projeto foi estruturado seguindo os pilares da POO:
* **Classes e Objetos:** `Aluno` e `Reserva` são os "moldes" (models) do sistema.
* **Encapsulamento:** A lógica de negócios é gerenciada pela classe `SistemaAcademia`, que atua como um "cérebro" e protege os dados.
* **Associação:** A classe `Reserva` está diretamente associada a um objeto `Aluno`, demonstrando a relação "um-para-muitos".

## 🚀 Funcionalidades (Iterações 1 e 2)

O sistema de terminal implementa as seguintes funcionalidades:

* **Gerenciamento de Alunos:** Cadastrar novos alunos.
* **Validação:** O sistema impede o cadastro de alunos com CPF duplicado.
* **Gerenciamento de Reservas:** Adicionar e listar todas as reservas.
* **Manutenção de Reservas:** Atualizar o status de uma reserva (ex: Reservado, Confirmado, Cancelado).
* **Relatórios:** Gerar um relatório simples de contagem de reservas ativas por aluno.
* **Persistência de Dados:** O sistema salva e carrega automaticamente todos os dados (alunos e reservas) de arquivos `.txt`, garantindo que os dados não sejam perdidos ao fechar o programa.

## 📂 Estrutura Modular do Projeto

Para facilitar a manutenção e seguir os princípios ágeis, o código foi modularizado da seguinte forma:

* **`projeto_academia/`** (Pasta raiz do projeto)
    * **`models/`**: Contém as classes de dados (os "moldes").
        * `aluno.py`: Define a classe `Aluno`.
        * `reserva.py`: Define a classe `Reserva`.
    * **`services/`**: Contém as classes de lógica e serviços (o "cérebro").
        * `sistema.py`: Define a classe `SistemaAcademia`, que gerencia o sistema.
        * `persistencia.py`: Define a lógica para salvar e carregar os arquivos `.txt`.
    * **`data/`**: Pasta criada automaticamente para armazenar os dados de persistência.
        * `alunos.txt`
        * `reservas.txt`
    * **`main.py`**: Ponto de entrada da aplicação e responsável pelo menu do terminal.
    * **`__init__.py`** (dentro de `models` e `services`): Arquivos (vazios) que sinalizam ao Python que as pastas são "pacotes".

## ▶️ Como Executar

1.  Clone este repositório.
2.  Certifique-se de ter o **Python 3** instalado.
3.  Navegue até a pasta raiz do projeto pelo seu terminal.
4.  Execute o menu principal:

    ```bash
    python main.py
    ```
5.  Na primeira execução, a pasta `/data` e os arquivos com dados fictícios serão criados automaticamente.
