# artikule-server
Refresher for Django to ver 1.10


Most OS's comes with python, if not get python from python.org

PS: preferred to set-up a virtualenv per project, but if you don't know how, follow along, but you may want to read about it later. 


# Let's get the beast up

```
pip install -r requirements.txt
python manage.py createsuperuser  # give user name and password
python manage.py runserver
```

Now the server should be running at http://localhost:8000
Open http://localhost:8000/admin
go to article section and start adding articles
