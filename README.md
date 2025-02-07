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

## Organização da Estrutura do Projeto

### Backend com Docker

O backend está programado para funcionar em um container Docker. O Docker Compose serve para coordenar os containers requeridos.

#### Procedimentos para Configuração e Implementação

1. Autorizar o script `wait-for-it.sh`  
O `wait-for-it.sh` é empregado para assegurar que o banco de dados esteja apto a aceitar conexões antes de iniciar o servidor Django. Autorize a execução do script através do seguinte comando:
  
	`chmod +x wait-for-it.sh`
    
2.  Dockerfile  
O Dockerfile é encarregado de estabelecer o ambiente da aplicação, instalar as dependências e ajustar o container para executar o Django.
    
    -   Copiar o arquivo de dependências:  
        COPY requirements.txt /app/
        
    -   Instalar as dependências  
        RUN pip install --no-cache-dir -r requirements.txt
        
    -   Copiar o script [wait-for-it.sh](http://wait-for-it.sh/) e conceder permissões  
        COPY [wait-for-it.sh](http://wait-for-it.sh/) /path/to/container/  
        RUN chmod +x /path/to/container/wait-for-it.sh
        
    -   Copiar o código-fonte da aplicação  
        COPY . /app/
        
    -   Expor a porta do servidor  
        EXPOSE 8000
        
    -   Comando para iniciar o servidor  
        CMD [“python”, “[manage.py](http://manage.py/)”, “runserver”, “0.0.0.0:8000”]`
        
3.  Docker Compose  
    O documento `docker-compose.yml` estabelece e ajusta as configurações dos containers usados no ambiente, abrangendo o banco de dados e o backend.
    
4.  Subir os containers  
    Para subir os containers, utilize o comando abaixo:
    
     `docker-compose up --build`
    
    Isso irá iniciar o banco de dados PostgreSQL e o servidor Django. O backend será acessível na porta `8000`.
