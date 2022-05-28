from django.urls import path

from .views import home, create, update, delete, done, save

app_name = "todo"
urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('save/', save, name="save"),
    path('details/<str:name>/update', update, name="update"),
    path('<str:name>/delete', delete, name="delete"),
    path('<str:name>/done', done, name="done"),
]
