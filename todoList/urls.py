from django.urls import path

from .views import home, show

app_name = "todo"
urlpatterns = [
    path('', home, name="home"),
    path('details/<str:name>', show, name="show"),
]
