

# Guide dj4e course project
https://samples.dj4e.com/ 


## Setup Virtual Env
```sh
python3.9 -m venv .venv

# activate virtual environnment - macos
source .venv/bin/activate

# activate virtual environnment - windows
.venv\Scripts\activate


pip freeze > requirements.txt

# install project dependencies
pip install -r requirements.txt
```


## First Django App
https://docs.djangoproject.com/en/4.2/intro/tutorial01/ 


### Writing your first Django app, part 1¶

You can tell Django is installed and which version by running the following command in a shell prompt
```sh
 python -m django --version

 # Creating a project
django-admin startproject mysite

 # The development server
 python manage.py runserver
 python manage.py runserver 8080
```

If you want to change the server’s IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:
```sh
python manage.py runserver 0.0.0.0:8000
```

### Creating the Polls app

```sh
python manage.py startapp polls
```

#### Write your first view

```py
# polls/views.py¶
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

**In the polls/urls.py file include the following code:**
```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```


The next step is to point the root URLconf at the polls.urls module. In mysite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:
```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```


### Django Project Tutorial 2

#### Learning Objectives:
- Understand Django models and models.py
- Use the Django shell
- Understand the django admin feature
- Understand databases and Django migration
- Follow the instructions in this tutorial:

https://docs.djangoproject.com/en/4.2/intro/tutorial02/

#### Database setup¶
```sh
python manage.py makemigrations
python manage.py migrate

```

#### Creating models¶
`Philosophy`

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Django follows the DRY Principle. The goal is to define your data 

#### Activating models
That small bit of model code gives Django a lot of information. With it, Django is able to:

Create a database schema (CREATE TABLE statements) for this app.
Create a Python database-access API for accessing Question and Choice objects.
But first we need to tell our project that the polls app is installed.

`Philosophy`
Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation

```py
INSTALLED_APPS = [
    # add polls app
    "polls.apps.PollsConfig",

    # django based apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
```sh
python manage.py makemigrations polls

# The sqlmigrate command takes migration names and returns their SQL:
python manage.py sqlmigrate polls 0001
```
The sqlmigrate command doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

If you’re interested, you can also run `python manage.py check`; this checks for any problems in your project without making migrations or touching the database.
```sh
python manage.py check

# Now, run migrate again to create those model tables in your database
python manage.py migrate
```

The `migrate` command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:
- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.

#### Playing with the API
```sh
python manage.py shell

from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
from django.utils import timezone
q = Question(question_text="What's new?",pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
q.save()

# Now it has an ID.
q.id
# 1

# Access model field values via Python attributes.
q.question_text
#"What's new?"

q.pub_date
#datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()

# objects.all() displays all the questions in the database.
Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

Wait a minute. <Question: Question object (1)> isn’t a helpful representation of this object. Let’s fix that by editing the Question model (in the polls/models.py file) and adding a __str__() method to both Question and Choice:

#### Ajust the models.py


Save these changes and start a new Python interactive shell by running python manage.py shell again:
```sh
from polls.models import Choice, Question

# Make sure our __str__() addition worked.
Question.objects.all()
#<QuerySet [<Question: What's up?>]>

#Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
Question.objects.filter(id=1)
# <QuerySet [<Question: What's up?>]>

Question.objects.filter(question_text__startswith="What")
# <QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
# <Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
Question.objects.get(id=2)
#Traceback (most recent call last):
    ...
#DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
Question.objects.get(pk=1)
# <Question: What's up?>

# Make sure our custom method worked.
q = Question.objects.get(pk=1)
q.was_published_recently()
# True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
q.choice_set.all()
# <QuerySet []>

# Create three choices.
q.choice_set.create(choice_text="Not much", votes=0)
# <Choice: Not much>

q.choice_set.create(choice_text="The sky", votes=0)
# <Choice: The sky>

c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice objects have API access to their related Question objects.
c.question
# <Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
q.choice_set.all()
# <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
q.choice_set.count()
# 3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
Choice.objects.filter(question__pub_date__year=current_year)
# <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
c = q.choice_set.filter(choice_text__startswith="Just hacking")
c.delete()
```

#### Introducing the Django Admin

`Philosophy`

Generating admin sites for your staff or clients to add, change, and delete content is tedious work that doesn’t require much creativity. For that reason, Django entirely automates creation of admin interfaces for models.

Django was written in a newsroom environment, with a very clear separation between “content publishers” and the “public” site. Site managers use the system to add news stories, events, sports scores, etc., and that content is displayed on the public site. Django solves the problem of creating a unified interface for site administrators to edit content.

The admin isn’t intended to be used by site visitors. It’s for site managers.

```sh
# Creating an admin user
python manage.py createsuperuser
- Username: admin
- Email_address: admin@example.com
- password : admin


python manage.py runserver
```

Now, open a web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/. You should see the admin’s login screen:


#### Make the poll app modifiable in the admin
```py
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

#### Auto-grader: Django Tutorial part 2
For this assignment work through Part 2 of the Django tutorial at https://www.dj4e.com/assn/dj4e_tut02.md. 

Once you have completed tutorial, make a second admin user with the following information:
```sh
Account: dj4e
Password: bca83e6da
```

### Django Tutorial 03
Writing your first Django app, part 3
https://docs.djangoproject.com/en/4.2/intro/tutorial03/  

`Overview`
A view is a “type” of web page in your Django application that generally serves a specific function and has a specific template. For example, in a blog application, you might have the following views:



### Django Tutorial 04
Writing your first Django app, part 4
https://docs.djangoproject.com/en/4.2/intro/tutorial04/ 

#### Write a minimal form¶
Let’s update our poll detail template (“polls/detail.html”) from the last tutorial, so that the template contains an HTML <form> element:

#### dj4e assigment
https://www.dj4e.com/tools/dj-tutorial/?PHPSESSID=3f0eb86a490be131cd2d09bacc6bd3ed 

```py
You can mix function and class views in your mysite/polls/urls.py file as shown below:
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('owner', views.owner, name='owner'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```


## Django Features and Libraries

### Week 1 - DIY Hello World / Sessions
https://www.dj4e.com/tools/dj-tutorial/?PHPSESSID=5698078ea83ae7706cc34918116e1583 

```sh
# Building a Main Page
cd ~/django_projects/mysite
python manage.py startapp home


# Playing With Sessions (DIY)
python manage.py startapp hello
```


### Week 3 - Login / Autos CRUD
https://www.dj4e.com/assn/dj4e_autos.md?PHPSESSID=086179c51c5c735d0c59bfc7afabad22 

```sh
workon django42      # or django4 as needed
cd ~/django_projects/mysite
python manage.py startapp autos

python manage.py check 

python manage.py makemigrations
python manage.py migrate

# create user 
Account: dj4e_user 
Password: Meow_f3711e_42
```

### Week 4: Cat Database CRUD
```sh
workon django42 
cd ~/django_projects/mysite
python manage.py startapp cats

```


### Week 5:  Building a Classified Ad Web Site (Django 4.2)
```sh
cp ~/dj4e-samples/dj4e-samples/settings.py ~/django_projects/mysite/mysite
cp ~/dj4e-samples/dj4e-samples/urls.py ~/django_projects/mysite/mysite
cp -r ~/dj4e-samples/home/* ~/django_projects/mysite/home

pip install mysqlclient
python manage.py makemigrations 

python manage.py startapp ads