from django.conf.urls import include, url
from west import views
urlpatterns = [
    url(r'^$', views.first_page),
]