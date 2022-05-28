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
    if request.method == "POST":
        task_name = request.POST["taskName"]
        todo.append({
            "name": task_name,
            "status": False
        })
    return redirect(reverse("todo:home"))


def update(request, **kwargs):
    task_name = kwargs["name"]
    return render(request, 'todoList/to_do_update.html', context={"name": task_name})


def save_update(request, **kwargs):
    if request.method == "POST":
        new_task_name = request.POST["taskName"]
        task_name = kwargs["name"]
        selected_task = contains(todo, lambda x: x["name"] == task_name)
        todo.remove(selected_task)
        selected_task["name"] = new_task_name
        todo.append(selected_task)
    return redirect(reverse("todo:home"))


def contains(tasks, predicate):
    for task in tasks:
        if predicate(task):
            return task


def delete(request, **kwargs):
    task_name = kwargs["name"]
    selected_task = contains(todo, lambda x: x["name"] == task_name)
    todo.remove(selected_task)
    return redirect(reverse("todo:home"))


def done(request, **kwargs):
    task_name = kwargs["name"]
    selected_task = contains(todo, lambda x: x["name"] == task_name)
    selected_task["status"] = not selected_task["status"]
    return redirect(reverse("todo:home"))
