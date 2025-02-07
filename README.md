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
O `wait-for-it.sh` é utilzado para assegurar que o banco de dados esteja apto a aceitar conexões antes de iniciar o servidor Django. Autorize a execução do script através do seguinte comando:
  
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

    **Arquivo docker-compose.yml**

-  Definindo a versão do formato do arquivo `docker-compose.yml`.

	`version: '3.8'`

- Indica o início da definição dos serviços que compõem a aplicação. Cada serviço representa um contêiner Docker.

	`services:`

-  Define um serviço chamado `db`. Este será o contêiner que executa o banco de dados PostgreSQL.
  
	  `db:`
   
- Especifica a imagem Docker que será usada para criar o contêiner. Aqui, está usando a imagem oficial do PostgreSQL na versão `14`.
  
   ` image: postgres:14`
  
- Define variáveis de ambiente que serão passadas para o contêiner.
 
    environment:
      `POSTGRES_USER: postgres - Definindo o usuário padrão do Postgres;`
      `POSTGRES_PASSWORD: et3ch - Define a senha do usuário`
      `POSTGRES_DB: todolist - Cria um banco automáticamente ao iniciar o contêiner.`
 - Mapeia um volume persistente (`db_data`) para o diretório `/var/lib/postgresql/data` dentro do contêiner. Isso garante que os dados do banco de dados sejam salvos mesmo após o contêiner ser reiniciado ou removido.
   ` volumes:`
` db_data:/var/lib/postgresql/data`

- Conecta o serviço `db` à rede backend, que será definida mais abaixo. Isso permite que outros serviços (como o backend) comuniquem-se com o banco de dados
  
    `networks:`
      `- backend`
  
- Define outro serviço chamado `backend`. Este será o contêiner que executa a aplicação backend da aplicação.

   `backend:`
  
- Indica que o Docker deve construir a imagem deste serviço usando o `Dockerfile` localizado no diretório atual (`./`).

  ` build: ./ `
  
- Define o comando que será executado quando o contêiner for iniciado

    command: ["sh", "-c", "./wait-for-it.sh db:5432 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
	-   `./wait-for-it.sh db:5432`: Um script que aguarda até que o banco de dados (`db`) esteja disponível na porta `5432`.
	-   `python manage.py migrate`: Executa as migrações do Django para configurar o banco de dados.
	-   `python manage.py runserver 0.0.0.0:8000`: Inicia o servidor de desenvolvimento do Django na porta `8000`.
   
- Monta o diretório local `./todo-list-backend` dentro do contêiner.
  
   ` volumes:`
      `- ./todo-list-backend`

      
 - Mapeia a porta `8000` do contêiner para a porta `8000` do host. Isso permite acessar a aplicação backend através de `http://localhost:8000`.
 
    `ports:`
      `- "8000:8000"`

      
- Garante que o serviço `backend` só será iniciado após o serviço `db` estar em execução. No entanto, isso não garante que o banco de dados esteja pronto para receber conexões (daí o uso do `wait-for-it.sh`).

    `depends_on:`
      `- db `
  
 - Conecta o serviço `backend` à mesma rede `backend` que o serviço `db`. Isso permite que os serviços se comuniquem entre si.

    `networks:`
     ` - backend`
   
- Define as redes que serão usadas pelos serviços.

   `networks:`

-   Cria uma rede chamada `backend` com o driver `bridge`. O driver `bridge` é o padrão para redes Docker e permite que os contêineres se comuniquem entre si.
	
	  `backend:`
	    `driver: bridge`
    
- Define os volumes que serão usados pelos serviços.
  
`volumes:`

- Cria um volume persistente chamado `db_data` com o driver `local`. Esse volume será usado para armazenar os dados do banco de dados
 PostgreSQL.

  `db_data:`
    `driver: local`

    
5.  Subir os containers  
    Para subir os containers, utilize o comando abaixo:
    
     `docker-compose up --build`
    
    Isso irá iniciar o banco de dados PostgreSQL e o servidor Django. O backend será acessível na porta `8000`.
