# TBS: Turbo Sales
Turbo Sales is a project developed in Python-Django, consists in 2 modules: Stock and Sales, talking with each other using a REST API.
## Introduction:
This project was developed as an academic test. It is, at the moment, not suited for production.
## Requirements
  Docker and Docker-Compose 1.8+
## Setup
Get running:
```bash
docker-compose up
```
Stop:
```bash
docker-compose down
```
Run in background:
```bash
docker-compose start
```

## Sample compose
Check this raw file [here](https://raw.githubusercontent.com/Cassianosricardo/TBS/master/dac/docker-compose.yml "Raw File").
```yml
version: '2' 
services:
  estoque_db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: estoque
      MYSQL_USER: admin 
      MYSQL_PASSWORD: admin
    volumes:
       - estoque_vol:/var/lib/mysql 
  estoque_web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - ./estoque/:/code
    ports:
      - "9001:8000"
    depends_on:
      - estoque_db
  vendas_db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: vendas
      MYSQL_USER: admin 
      MYSQL_PASSWORD: admin
    volumes:
       - vendas_vol:/var/lib/mysql 
  vendas_web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - ./vendas/:/code
    ports:
      - "9002:8000"
    depends_on:
      - vendas_db
volumes:
  vendas_vol:
  estoque_vol:
```
## License
GLP
## Support
The provided software is available for free, with no support. 
## Contributing
    Fork it
    Create a branch for your new feature
    Commit your new features.
    Create a Pull Request
