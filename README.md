# My First Django Website

This was the first website I built with Django, back in sixth grade. It is a small learning project with a homepage, a polls app, custom models, templates, and basic admin customization.

The project is kept here as an early record of how I learned routing, views, models, templates, and SQLite. It is not a production application, and its old Django configuration may need updates before it runs on a modern Python environment.

## Project structure

The Django project lives in [`django-polls/`](django-polls/). The `homepage` and `polls` apps contain the application code, while the templates and static assets hold the site's pages, styles, images, and audio.

## Running it

```bash
git clone https://github.com/Andrey199123/Django-First-Website.git
cd Django-First-Website/django-polls
python3 -m venv .venv
source .venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000. The repository no longer includes a generated SQLite database or compiled Python files; Django creates a fresh local database through the migration step.
