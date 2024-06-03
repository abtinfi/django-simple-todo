from django.shortcuts import render, redirect
from django.http import HttpResponse
from homescreen.forms import ToDoCreatForms
from .models import ToDo
from django.contrib import messages


# Create your views here.
def say_hello(request):
    person = {"name": "amir"}
    return render(request, "hello.html", context=person)


def home(request):
    all = ToDo.objects.all()
    info = {"todos": all}
    return render(request, "home.html", context=info)


def detail(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    return render(request, "detail.html", {"todo": todo})


def delete(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    messages.success(request, "task deleted success", "success")
    return redirect("home")


def create(request):
    if request.method == "POST":
        form = ToDoCreatForms(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            ToDo.objects.create(
                title=clean_data["title"],
                body=clean_data["body"],
                created=clean_data["created"],
            )
            messages.success(request, 'todo created successfully', 'success')
            return redirect('home')
    else:
        form = ToDoCreatForms()
    return render(request, "create.html", {"form": form})
