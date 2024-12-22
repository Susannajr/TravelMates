<h2 align="center">travelmates by Django</h2>

### Development Tools
## Start

#### 1) Create an image

    docker-compose build

##### 2) Run the container

    docker-compose up
    
##### 3) Go to the following address

    http://127.0.0.1:8000/api/v1/swagger/

## Development with Docker

##### 1) Fork the repository

##### 2) Clone the repository

    git clone <your_generated_repository_link>

##### 3) Create .env.dev in the root of the project

    DEBUG=1
    SECRET_KEY=fdsadqw3f32wg<43g3hv$%#@%F$F$$F$F
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    # Data Base
    POSTGRES_DB=travelmates
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DATABASE=travelmates
    POSTGRES_USER=travelmate_user
    POSTGRES_PASSWORD=travelmate_pass
    POSTGRES_HOST=travelmates-db
    POSTGRES_PORT=5432
    DATABASE=postgres

    # Email
    DEFAULT_FROM_EMAIL=your@your.com
    EMAIL_USE_TLS=True
    EMAIL_HOST=your_smtp
    EMAIL_HOST_USER=your@your.com
    EMAIL_HOST_PASSWORD=pass
    EMAIL_PORT=587
    
##### 4) Create an image

    docker-compose build

##### 5) Run the container

    docker-compose up
    
##### 6) Create a superuser

    docker exec -it travelmate_travelmate_back_1 python manage.py createsuperuser
                                                        
##### 7) If you need to clear the database

    docker-compose down -v
