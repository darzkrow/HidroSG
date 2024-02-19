### Tecnologías Utilizadas

- Lenguaje de programación: [Python](https://www.python.org/)
- Framework web: [Django](https://www.djangoproject.com/)
- Base de datos: [MySQL](https://www.mysql.com/), [PostgreSQL](https://www.postgresql.org/), o [SQLite](https://www.sqlite.org/) (según la elección del usuario)

### Requisitos de Instalación

- Python 3.12 o superior
- Django 5.0 o superior
- MySQL, PostgreSQL o SQLite (según la elección del usuario)
- Otros requisitos se pueden encontrar en el archivo `requirements.txt`

### Instalación

1. Clona este repositorio: `https://github.com/darzkrow/HidroSG.git`
2. Ve al directorio del proyecto: `cd HidroSG`
3. Crea y activa un entorno virtual (opcional): `python3 -m venv env` y `source env/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Configura la base de datos en el archivo `settings.py`
6. Realiza las migraciones de la base de datos: `python manage.py migrate`
7. Inicia el servidor local: `python manage.py runserver 0.0.0.0:8080`
8. Accede al sistema a través de tu navegador web: `http://localhost:8000`

### Uso



## Contribuciones

Las contribuciones son bienvenidas. Si deseas realizar mejoras en este proyecto, sigue los siguientes pasos:

1. Haz un fork de este repositorio.
2. Crea una rama para tu función o corrección: `git checkout -b feature/mi-nueva-funcion`
3. Realiza los cambios necesarios y realiza los commits: `git commit -am 'Agrega una nueva función'`
4. Sube los cambios a tu repositorio remoto: `git push origin feature/mi-nueva-funcion`
5. Abre un Pull Request en este repositorio y describe los cambios que has realizado.
