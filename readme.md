docker build -t mysql-votante .   
docker run -d -p 3377:3306 -e MYSQL_ROOT_PASSWORD=r00t -e MYSQL_DATABASE=coleta -e MYSQL_USER=useer -e MYSQL_PASSWORD=vot@ante mysql-votante


para conectar no banco: <br>
host: localhost <br>
porta: 3377 <br>
usuario: useer <br>
senha: vot@ante <br>

CPF PARA TESTE DADOS PUXADOS DA TABELA INSERIDA PELO PARTIDO <BR>
04411786675

