# Wall App - Backend

Wall App was my first API made using Django Rest Framework  
The project is hosted using Heroku: https://wall-app-back.herokuapp.com/

## Installation

Clone the project and install it's requirements.

```bash
git clone git@github.com:procopio420/wall-app-backend.git
cd wall-app-backend
pip install -r requirements.txt
python3 manage.py migrate
```

## Usage

```bash
python3 manage.py runserver
```

## Test

```bash
python3 manage.py test
```

## Tests Coverage

```bash
coverage run --source='.' manage.py test
coverage report
```

## To Do

- [x] Hide API keys and secret keys
- [x] Fix SendGrid