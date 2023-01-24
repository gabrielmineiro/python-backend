
from django.urls import path
from .views import home, saveDb

urlpatterns = [
    path("", home, name="home"),
    path("save/", saveDb, name="save")
]