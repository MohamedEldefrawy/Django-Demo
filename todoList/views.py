from django.shortcuts import render, redirect
from django.urls import reverse

todo = [
    {
        "name": "study",
        "status": False
    },
    {
        "name": "practice",
        "status": False
    },
    {
        "name": "chilling",
        "status": False
    },

]


# Create your views here.
def home(request):
    return render(request, 'todoList/to_do_list.html', context={"data": todo})


def create(request):
    return render(request, 'todoList/to_do_create.html')


def save(request):
    print(request)
    if request.method == "POST":
        task_name = request.POST["taskName"]
        todo.append({
            "name": task_name,
            "status": False
        })
    return redirect(reverse("todo:home"))


def update(request, **kwargs):
    print(kwargs["name"])

    return render(request, 'todoList/to_do_update.html', context={})


def delete(request, **kwargs):
    return redirect(reverse("todo:home"))


def done(request, **kwargs):
    return redirect(reverse("todo:home"))
