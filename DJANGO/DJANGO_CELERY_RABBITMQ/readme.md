Envio masivo de correos en django y se realiza se forma asincrona

Actualizar dependencias :
    - sudo apt-get update
    - sudo apt-get upgrade
Instalar:
    1. Instalar erlang complemento para que funcione rabbitmq 
        Step 1: Import Erlang GPG Key
            sudo apt update
            sudo apt install software-properties-common apt-transport-https
            wget -O- https://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc | sudo apt-key add -
        Step 2: Add Erlang Repository to Ubuntu
            echo "deb https://packages.erlang-solutions.com/ubuntu focal contrib" | sudo tee /etc/apt/sources.list.d/rabbitmq.list
        Step 3: Install Erlang on Ubuntu 
            sudo apt update
            sudo apt install erlang
        Step 3: try
            erl
    2. Instalar rabbitmq-server
        sudo apt-get install -y rabbitmq-server
    3. sudo rabbitmq-plugins enable rabbitmq_management
    

Activar entorno virtual:
    linux:
        source ./venv/bin/activate

Correr rabbitmq:
    - sudo service rabbitmq-server start
Ver estado de rabbitmq:
    service rabbitmq-server status

Crear proyecto django:
    - django-admin startproject django_celery
    Crear aplicacion:
        - django-admin startapp tareas

Vamos a usar sqlite3 la que viene por defecto en django:
    Realizar migraciones manage.py migrate
Crear superusuario django:
    python manage.py createsuperuser
    username : root
    password : root

django-extensions nos permite importar todos los modelos disponibles cuando entremos mediante al shell
    python manage.py shell_plus

# Comenzar con celery
    - celery -A django_celery worker -l info