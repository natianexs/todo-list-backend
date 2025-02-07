# Sistema de Lista de Tarefas

## Descrição do Projeto

O **Sistema de Lista de Tarefas** é uma aplicação web para gerenciamento de tarefas com as seguintes funcionalidades principais:

-   **Cadastro de usuários**: Permite o registro de novos usuários.
-   **Cadastro de Tarefas**: O usuário pode cadastrar, listar e atualizar tarefas.
-   **Comentários**: É possível adicionar múltiplos comentários em cada tarefa.
-   **Atribuição de tempo de trabalho**: O usuário pode atribuir tempo de trabalho em uma tarefa e registrar quem realizou a tarefa.
-   **Obter tempo de trabalho**: O sistema permite consultar o tempo total trabalhado em uma tarefa.
-   **Horas trabalhadas por usuário**: Visualizar o total de horas trabalhadas por cada usuário.

## Tecnologias Utilizadas

-   **Python 3.10**
-   **Django 4.2.18**: Framework para o backend.
-   **Django Filter 24.3**: Para facilitar a filtragem de objetos na API.
-   **Django Rest Framework 3.15.2**: Framework para a criação de APIs RESTful.

## Requisitos

-   **Docker**: Para executar a aplicação em containers.
-   **Docker Compose**: Para orquestrar múltiplos containers (backend e banco de dados).