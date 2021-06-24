# Wall App - Backend

Wall App was my first API made using Django Rest Framework 

## Installation

Clone the project and install it's requirements.

```bash
git clone
cd pasta
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