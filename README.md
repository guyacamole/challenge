# API challenge

En este repositorio se cumplio con los objetivos propuestos en el documento



## Environment Variables

Para la definicion, creacion y autenticacion del proytecto se definieron variables en un archivo `.env`, cualquiera de ellas es personalizable, si estas se cambian una vez levantado el servicio, basta con poner la bandera `--build` a docker para que estas surtan efecto en el proyecto. Entre estas variables, las mas importantes son: 

`DJANGO_ADMIN_USERNAME`

`DJANGO_ADMIN_PASSWORD`

`POSTGRES_USER`

`POSTGRES_PASSWORD`

`PGADMIN_DEFAULT_EMAIL`

`PGADMIN_DEFAULT_PASSWORD`
## Deployment

Para el uso de esta API es necesario levantar dos servicios (`django-backend` y `db`), en el archivo de definicion del docker hay tres, esto es porque agregue un observador amigable a la base de datos.

Con Logs en terminal:
```bash
  docker-compose up
```

Solo correr el servicio:
```bash
  docker-compose up -d
```
## API Reference
#### Auto Documentacion
En esta ruta, podemos acceder a la documentacion autogenerada con ejemplos de codigo para el uso de los endpoints de esta API

```http
  GET /docs/
```

### Obtencion de Token
Con las credenciales definidas en el archivo `.env`, podemos obtener el token con un `POST` a la siguiente ruta

```http
  POST /auth/
```
### Formato de Token

| Header | Value     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Token {String}` | **Required**. Token generado |

#### Get all items

```http
  GET /api/v1/properties/
```
#### Get item

```http
  GET /api/v1/properties/${id}
```
#### Create item
```http
  POST /api/v1/properties/
```
#### Delte item

```http
  DELETE /api/v1/properties/${id}
```
#### Update item

```http
  PUT /api/v1/properties/${id}
```

## Usage/Examples
#### Create or Update
```JSON
{
    "id": 1,
    "title": "Abedulesss",
    "description": "casa numero 1",
    "price": "5.00",
    "location": "elcielo",
    "property_type": "house",
    "bedrooms": 2,
    "bathrooms": 2,
    "square_feet": 2,
    "available": true
}
```
#### Get Token
```JSON
{
  "username": 
    "admin"
  ,
  "password": 
    "admin"
}
```


## Demo

#### Get Token
![Alt text](img/auth.png?raw=true "Auth")

#### Get all items
![Alt text](img/read.png?raw=true "Read")

#### Get item
![Alt text](img/getItem.png?raw=true "Get Single")

#### Create item
![Alt text](img/create0.png?raw=true "Create item")

#### Delte item
![Alt text](img/delete0.png?raw=true "Deleting")
![Alt text](img/delete1.png?raw=true "After Delete")

#### Update item
![Alt text](img/update.png?raw=true "Update")


#### PGAdmin Conecction
![Alt text](img/Screenshot2023-12-14223637.png?raw=true "PgAdmin con")

#### DB Table
![Alt text](img/db.png?raw=true "db con")
#### Web Admin
![Alt text](img/webAdmin.png?raw=true "Web Admin")
#### Auto Doc
![Alt text](img/autoDoc.png?raw=true "Auto Doc")




## Authors

- [@guyacamole](https://github.com/guyacamole)


