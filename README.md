# AXIOMA-BANKSTER
========================

Esta aplicacion ha sido desarrollada como una prueba tecnica de integracion de las tecnologias Python, Django, Javascript, Bootstrap 5, y Ubuntu


## Deploy

Las siguientes instrucciones son especificas para un deploy en Ubuntu 18.04.

Es recomendable actualizar los paquetes del sistema utilizando:

```
    sudo apt-get update
    sudo apt-get dist-upgrade
```

Se recomienda instalar pip:

```
    sudo apt-get install python3-pip
```

Debe tambien instalar las dependencias de Django:
```
    pip3 install django
    pip3 install django-axes 
```

Para obtener una copia del proyecto, puede utilizar los siguientes comandos:

```
    wget -O master.zip https://github.com/bryan-menendez/axioma-bankster/archive/refs/heads/master.zip
    unzip master.zip
    cd axioma-bankster-master
```

Dentro de la carpeta del proyecto, puede arrancar el servidor web utilizando:

```
    python3 manage.py runserver
```

El servidor estara disponible en la url 127.0.0.1:8000  

Se han incluido las siguientes cuentas en la base de datos de muestra.

```
    admin:admin
    12.325.182-8:12345678?
    16.325.182-8:12345678?
```

### Rutas

#### GET /
Vista que sirve como landing y login page.  La ruta "/persona" renderiza el mismo endpoint para resolver una redireccion forzada a los nuevos usuarios del sitio. 
  
 
#### GET /details

Vista que contiene la vista de detalles de la cuenta de un usuario. Requiere autenticacion.


#### POST /auth_cred_submit

API endpoint para la autenticacion de credenciales de usuario. 

Request:
```
headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': your_csrf_token
}

body: JSON.stringify({ 
    username: your_username, 
    password: your_password 
})
```

Los usuarios solo tienen 3 intentos para ingresar a su cuenta. De otro modo, se bloquea.  
Los bloqueos de cuenta responden a combinaciones de IP + cuenta de la tabla axes_accessattempt.  
Responde con un codigo HTTP 200 de contenido "ok" para un ingreso exitoso, 401 para fallos de autenticacion, y 403 para errores de CORS y bloqueos de cuenta.  

#### GET /admin/auth/user/

Endpoint del admin de django que contiene la lista de usuarios del sistema. Requiere autenticacion.
Para utilizar la funcion de desbloqueo de cuentas, seleccione las cuentas a desbloquear, seleccione la accion "Desbloquear cuentas seleccionadas", y presione el boton "GO"

#### GET /admin/auth/user/add/

Endpoint del admin de django que permite la creacion de nuevas cuentas. Tambien se ha incluido un inline para el modelo Cliente que permite el ingreso de informacion pertinente.