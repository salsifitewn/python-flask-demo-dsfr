# Python flask course

## Intro

Project as support for learning Python+Flask and adapted Front-end.  
Adapted from <https://github.com/jimdevops19/FlaskSeries>

⭐️ Course Contents ⭐️

- P1  (0:00:00) Introduction
- P2  (0:20:37) Styling & Templates
- P3  (0:41:37) Sending data to Templates
- P4  (1:02:56) Template Inheritance
- P5  (1:21:14) Models and Databases
- P6  (1:51:13) Project Restructure
- P7  (2:05:41) Model Relationships
- P8  (2:25:37) Flask Forms
- P9  (2:51:58) Flask Validations
- P10 (3:14:05) Flashes & Advanced Validations
- P11 (3:41:04) User Authentication Part 1
- P12 (3:59:56) User Authentication Part 2
- P13 (4:34:16) Logout and Customizations
- P14 (4:51:25) Item Purchasing Part 1
- P15 (5:18:39) Item Purchasing Part 2
- P16 (5:54:13) Item Selling

## CLI

```bash
# if local env 
python3 -m venv venv
source venv/bin/activate

pip install flask
pip install python-dotenv
flask run
pip freeze > requirements.txt
pip install -r requirements.txt

```

## Course Content

### P2: Styling & Templates

`render_template('home.html')` (default folder: template)
multiple decorators
bootstrap inclusion

### P3: Sending data to Templates

Introduction to jinja

### P4: Template Inheritance

layout extends with jinja

```jinja
{% extends 'base.html' %}
{% block title %}
Home Page
{% endblock %}
{% block content %}
<h1>Home Page</h1>
{% endblock %}
```

routing helper `url_for(function_name)`

## P5 : Models and Databases

SQLAlchemy: Data Mapper based ORM

Insert in console

```python
flask shell
from market import db
db.create_all()
from market.models import Item,User
user1 = User(username="salsifite",email_address="example@test.com",password_hash="123456789012",budget=900)
user2 = User(username="henry",email_address="example2@test.com",password_hash="123456789012",budget=900)
item1 =Item(name="Iphone 10",price=500,barcode="123456789012",description='desc')
db.session.add(item1)
 item1.owner = User.query.filter_by(username='jsc').first().id
db.session.commit()
Item.query.all()
item2 =Item(name="Laptop",price=90,barcode="123985473165")
db.session.add(item2)
db.session.commit()
item1.owner = User.query.filter_by(username='salsifite').first().id

for item in Item.query.filter_by(price=500):
...     item.name
... 
```

## P6 : Models and Databases

>Package 
>Pour créer votre propre package, commencez par créer dans le même dossier que votre programme - un dossier portant le nom de votre package. Dans notre exemple, nous le nommerons " utils ".
>Dans ce dossier, créons le fichier suivant: __init__.py , cela indique à python qu'il s'agit d'un package . Ce fichier peut être vide, seule sa présence est importante. 
> <https://python.doctor/page-python-modules-package-module-cours-debutants-informatique-programmation>

__init__.py

beware of cyclic dependancies. change import order at the end if needed

### Migrations

flask db init
flask db migrate -m 'migration_name'
flask db upgrade


## Resource

- <http://www.jimshapedcoding.com/courses/Flask%20Full%20Series>
- <https://www.youtube.com/watch?v=Qr4QMBUPxWo>
- <https://flask.palletsprojects.com/en/1.1.x/quickstart/>
- <https://gouvfr.atlassian.net/wiki/spaces/DB/pages/193036295/COMPOSANTS>
- <https://web.archive.org/web/20150113060057/http://effbot.org/zone/import-confusion.htm> :cyclic import dependancy
- <https://flask.palletsprojects.com/en/2.0.x/cli/#environment-variables-from-dotenv> : dotenv
