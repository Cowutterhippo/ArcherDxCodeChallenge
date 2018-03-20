ArcherDX Coding Task
==========

#### Prerequisites
- Python 2.7
- pip
- Mozilla Firefox web browser (for running tests)
- Mozilla geckodriver (for running tests; on Mac, `brew install geckodriver`)

#### Setup
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Visit the running application at http://127.0.0.1:8000/ to get started on your task!

#### Testing
```
python manage.py test
```

#### Third-Party Documentation
- https://docs.djangoproject.com/en/1.11/
- http://getbootstrap.com/docs/3.3/
- https://pypi.python.org/pypi/selenium
