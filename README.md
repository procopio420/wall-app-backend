# Wall App - Backend

Wall App was my first API made using Django Rest Framework 

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

## Security

There are some API keys and Secret Keys exposed, but it's to make it easier to test
And all of those keys are new and temporary