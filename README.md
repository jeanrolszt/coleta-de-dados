docker build -t mysql-votante .   
docker run -d -p 3377:3306 -e MYSQL_ROOT_PASSWORD=r00t -e MYSQL_DATABASE=coleta -e MYSQL_USER=useer -e MYSQL_PASSWORD=vot@ante mysql-votante


Para conectar no banco (A aplicação já está configurada para conectar no banco assim que ele subir pelo docker): <br>
host: localhost <br>
porta: 3377 <br>
usuario: root <br>
senha: r00t <br>

CPF PARA TESTE DADOS PUXADOS DA TABELA INSERIDA PELO PARTIDO <BR>
04411786675 - Josefino da Silva Andrade (FICTICIO)<BR>
28973666367 - Luciene Alves (FICTICIO)<BR>
45808735369 - Kayke Andrade (FICTICIO)<BR>

