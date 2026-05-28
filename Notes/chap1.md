# Chapter One: Setup

Not much to note really, all familiar things.

Sort project into a central folder.

## Virtual Environments

Use virtual environments for everything.

Create a virtual environment:

`python3 -m venv .venv`

I use an alias `mkvnv`

Activate it:

`source .env/source/activate`

I use an alias `actv`

Last argument in the creation of an env can be whatever you want, but keep it consistent.

## Installing Django
(In the environment)

`python -m pip install django~=5.0.0`

Using `5.0.0` to match book. Use `5.2` for LTS support. `5.0.0` is technically unsafe, so you should never post this publicly. Ideally use the latest option, but for internal learning its perfectly fine.

The difference from 5.0.0 and latest 6.x.x isn't major on the side of changing/breaking things. Thats against Django ethos or some self intellectual crap, probably. Most are feature additions. Those will be listed in end of entire notes.

## Creating Django project.

**This assumes you are in venv, which you should be**

To create a new Django project use:

`django-admin startproject django_project .`

`django-admin` is the general Django management command thats used.

`startproject` indicates starting the project.

*`django_project`* This is the name of the project. It could be whatever you want, but stick to best practices for standardized naming. Should be brief and what the project is.

`.` is used here. If you spent time in terminal you should know what this will do. This is your choice, but here is what it looks like with using a dot:

```
*(chapter)*
.
├── django_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
### And this is without:

```
*(chapter)*
.
└── django_project
    ├── django_project
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
```

You will see that without the `.` the django project is nested in an additional folder. Some say you should not do this, some say you should. Its mostly standards. If you are working with people, probably stick to something everyone knows. But if it is just you, using the `.` is fine. There could also be situation where you use an external tool that expects the deeper nested folder, but if that happens, just account for it. Its an unlikely situation.

## Starting the Django server

Django includes a built in, lightweight, local, insecure, development server. It is insecure, and lightweight. It can not handle real traffic. It is not designed for having multiple people visit it. It is for your `dev` environment and that only. By default it will run on `localhost`/ `127.0.0.1` on port 8000. If you need to debug it from some other server thats still on your local network, you could change this in settings, by setting allowed hosts in `settings.py` (project folder) to `[*]`. And passing `0.0.0.0:8000` in startup command.

Its a good idea to check if creating the project worked, you never know. In the root project folder (where your .venv) is, run:

`python manage.py runserver`.

Then visit your browser at `localhost` or `127.0.0.1` port `8000`. Like, `localhost:8000`.

You should see the default welcome Django welcome page. You will also see red text about unapplied migrations. Ignore that for now, thats normal. We just have not initialized the database yet. Enter `ctrl+c` to quit.

You will now see there is a new file. It will be `db.sqlite3`. This is an SQLite database folder.