# Inova Finance

Bem-vindo ao projeto **Inova Finance**! Este guia irá ajudá-lo a configurar e iniciar o ambiente para o desenvolvimento do projeto.

## Configuração do Ambiente

Para garantir que todas as dependências sejam gerenciadas corretamente, utilize um ambiente virtual.

### 1. Criação do Ambiente Virtual

Primeiro, instale o `virtualenv` se ainda não estiver instalado:

```bash
$ pip install virtualenv
```

Em seguida, crie e ative o ambiente virtual:

```bash
$ virtualenv .venv
$ source .venv/bin/activate   
```

### 2. Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto com:

```bash
pip install -r requirements.txt
```

### 3. Banco de dados
Agora, vamos criar um banco de dados e criar também o arquivo de conexão para o banco no MySQL!

Crie um banco de dados no prompt mysql 'inovafinance' e configure-o do seu jeito.

Depois que tiver criado o Banco e o Usuário, execute este comando abaixo:

```bash
cp config_local.example.py config_local.py
```

Será criado um arquivo chamado config_local.py no diretório raiz do projeto e adicione a seguinte configuração. Substitua os valores em maiúsculas pelos valores apropriados para sua configuração local!


Configuração do Banco de Dados

Para configurar o banco de dados, siga os passos abaixo:

Inicialize o Banco de dados:
```bash 
flask db init
```

Crie as migrações:
```bash
flask db migrate
```

Aplique as migrações para atualizar com o banco de dados: 
```bash
flask db upgrade
```

Após configurar o banco de dados, será necessário popular a base para que o sistema possa utilizar as configurações e dados apropriados.
