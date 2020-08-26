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

Acessar http://localhost:8000

## Fazendo Login
Por razões de simplicidade o login foi feito maneira “hard-code”.

```
Login: enaval
Senha: 123456
```

## Acessando o Django Admin (opcional)

```bash
python manage.py createsuperuser
```
Acessar http://localhost:8000/admin
