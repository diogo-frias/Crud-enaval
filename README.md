# Crud Enaval

## Pré Requisitos

* Python >= 3.x
* Django = 3.1

## Subindo o Projeto

```bash
cd enaval 
python manage.py migrate
```

```bash
python manage.py runserver
```

## Acessando o Django Admin

É necessário realizar o cadastro das Funções através do Django Admin.  
```bash
python manage.py createsuperuser
```
Acessar http://localhost:8000/admin


## Fazendo Login na aplicação
Por razões de simplicidade o login foi feito maneira “hard-code”.

Acessar http://localhost:8000

```
Login: enaval
Senha: 123456
```
