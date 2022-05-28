from django.urls import path

from .views import home, show, create, update, delete, done

app_name = "todo"
urlpatterns = [
    path('', home, name="home"),
    path('details/<str:name>', show, name="show"),
    path('create/', create, name="create"),
    path('details/<str:name>/update', update, name="update"),
    path('<str:name>/delete', delete, name="delete"),
    path('<str:name>/done', done, name="done"),
]
