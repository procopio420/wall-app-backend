# Wall App - Backend

Wall App was my first API made using Django Rest Framework  
The project is hosted using Heroku: https://wall-app-back.herokuapp.com/wall

## Installation

Clone the project and install it's requirements.

```bash
git clone git@github.com:procopio420/wall-app-backend.git
cd wall-app-backend
pip install -r requirements.txt
python3 manage.py migrate
```

## Env

It's neccessary to create a .env file at the project's root directory

```env
SECRET_KEY=
SENDGRID_API_KEY=
DEBUG=
```

SECRET_KEY: You can generate a key, [here](https://djecrety.ir/)  
SENDGRID_API_KEY: Create an API Key in Sendgrid in order to be able to send emails, [here](https://app.sendgrid.com/settings/api_keys)  
DEBUG: You can set it to True when running locally, default is False  
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