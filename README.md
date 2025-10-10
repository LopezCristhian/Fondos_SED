# API Fondos Educativos SED

Este proyecto es una **API desarrollada con Django y Django REST Framework**, que permite gestionar los Fondos educativos SED. Incluye documentación interactiva y un script de carga inicial de datos.

---

## Requisitos previos

Tener instalado:

- Python 3.10+
- pip
- Git

---

## Instalación y configuración

### 1.Clonar el repositorio
```bash
git clone https://github.com/LopezCristhian/Fondos_SED.git
cd Fondos_SED
```

### 2. Ejecución en contendero Docker

### 2.1 Ejecutar docker-compose
```bash
docker-compose up -d --build 
```

### 2.2 Crear superusuario para acceder al panel de administración
```bash
docker-compose exec backend python manage.py createsuperuser
```
### 2.3 Para acceder al panel de administración
- En el navegador web, acceder a la siguiente URL:  
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## Documentación de la API

- Documentación interactiva (Scalar UI):  
  [http://127.0.0.1:8000/api/scalar](http://127.0.0.1:8000/api/scalar)

- Interfaz Django REST Framework:  
  [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## Estructura del proyecto

```
├── manage.py
├── data
├── requirements.txt
├── FondosApp/
├── management/
│   ├── commands/
│   │    ├── poblar_db.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── Fondos_SED/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── README.md
```

---

## Tecnologías utilizadas

- Django  
- Django REST Framework (DRF)  
- SQLite 
- Scalar API Docs  

---

## Ejemplo de uso

```bash
GET http://127.0.0.1:8000/api/budget_item_revenue/
```

**Respuesta esperada**
```json
{
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "code": "string",
    "level": "string",
    "type": "string",
    "account_name": "string",
    "father": null,
    "created_at": "2025-10-10T18:18:45.162Z",
    "updated_at": "2025-10-10T18:18:45.162Z"
}
```

---

## Autor

**López Cristhian**   
[https://github.com/LopezCristhian](https://github.com/LopezCristhian)
