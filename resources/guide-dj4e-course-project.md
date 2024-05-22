

# Guide dj4e course project

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