# django_tracking_user
django_tracking es un proyecto personal para realizar auditoria a los registros de la BD


- Este proyecto es para crear un modelo que ayude a auditar un registro usando los campos `created`, `created_by` , `modified`, `modified_by`, los cuales permiten revisar quien hizo el ultimo cambio.

- Se reviso la libreria `django-crum` en https://pythonhosted.org/django-crum
- Como BD use el por defecto sqlite3, asi el administrador de BD = DBeaver

---
## Instalando el proyecto
 
- Instalar pip `sudo apt-get install python-pip`
- Instalar enviroment `sudo pip install virtualenv`
- Crear un entorno virtual virtualenv env_log
- activar entorno `source env_log\bin\active`


 Descargar el git y el enviroment (.env)
 - Luego instalar los requerimientos con el entorno activado :
 `(env_log)$ pip install --upgrade -r requirements.txt`
 - Activar las herramientas : 
 `(env_log)$ pip install django-extensions`
 - Correr las migraciones iniciales :
 `(env_log)$ python manage.py migrate`
