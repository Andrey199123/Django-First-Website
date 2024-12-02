from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('secret', views.secret, name='secret'),
    re_path(r"^static/homepage/other/favicon.ico$", RedirectView.as_view(url=staticfiles_storage.url("homepage/other/favicon.ico")))
]
