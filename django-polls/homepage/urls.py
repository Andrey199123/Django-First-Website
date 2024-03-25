from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
app_name = 'homepage'
urlpatterns = [
    url('', views.home, name='homepage'),
    url('secret', views.secret, name='secret'),
    url("static/homepage/other/favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("{% static 'homepage/other/favicon.ico' %}")))
]
