from django.shortcuts import render

todo = {

}


# Create your views here.
def home(request):
    return render(request, 'todoList/to_do_list.html', context={})


def show(request, **kwargs):
    return render(request, 'todoList/to_do_details.html', context={})
