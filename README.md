# Flask Web App
## _Proyecto de Aplicaciones Web con Flask - Desarrollo Web UTT_

https://github.com/franlop24/FlaskApp3B

Proyecto realizado en la materia de Desarrollo Web de la carrera de TSU en TI Área de Desarrollo de Software Multiplataforma, donde se integran las siguientes tecnologías:

- HTML
- CSS
- MySQL
- Python - Flask

## Flask App

- Uso Blueprints para organizar rutas (Views)
- Diseño de Clases para las Tablas de la Base de Datos.
-- Se utiliza mysql-connector-python para conección con MySQL 
-- Se crean métodos para consultas (Insert Into, Update, Delete, Select)
-- Encriptado de Contraseñas en Clase de usuarios
- Uso de Flask WTF para Formularios 
-- Distintos tipos de Fields de wtforms
-- Validaciones con wtforms.validators
-- Subida de archivos con FileField
- Templates con jinja, manejo de archivos estáticos
- Manejo de Sesiones con Flask Login (En construcción)

## Instalación

Se requiere tener instalado Python y MySQL, git, Visual Studio Code

Clonar Repositorio e Ingresar a él

```sh
git clone https://github.com/franlop24/FlaskApp3B FlaskApp
cd FlaskApp
```

Crear entorno Virtual, activarlo e instalar los paquetes de la aplicación (Windows)
En terminal de **GitBash**

```sh
py -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

Abrir la carpeta en Visual Studio Code

```sh
code .
```

Esquema de Base de Datos Utilizado

#### Tabla categories

```sh
DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(100) DEFAULT NULL,
  `description` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```

#### Tabla products

```sh
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `description` varchar(150) NOT NULL,
  `price` float NOT NULL DEFAULT '0',
  `stock` int NOT NULL DEFAULT '0',
  `category_id` int NOT NULL,
  `image` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
);
```

Tabla users
```sh
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `first_name` varchar(150) DEFAULT NULL,
  `last_name` varchar(150) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `role` varchar(20) NOT NULL DEFAULT 'customer',
  `image` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```

Actualiza el archivo de la conexión a la Base de Datos

- app/models/db.py

Ejecuta Aplicación

```sh
python app/app.py
```

Se ejecutará en la dirección siguiente:

```sh
localhost:5000/
```