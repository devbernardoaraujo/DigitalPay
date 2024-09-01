Virtualenv
é recomendado que as dependencias do projeto sejam instaladas dentro de um ambiente virtual (virtual env)

dependências
pip install -r requirements.txt

Arquivo de configuração
crie um arquivo chamado config_local e coloque a variável abaixo dentro dele substituindo as informações em maiúsculo dentro da string pelos nomes locais:


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://USERNAME:PASSWORD@HOST/inovafinance'

Banco de dados
agora é preciso rodar os comandos abaixo:
flask db init
flask db migrate
flask db upgrade

Agora será necessário popular a base para que possa pegar as configurações de lá
