from django.shortcuts import render, redirect
from . import HabitForm
from .forms import NameForm

def add(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid:
            habit = form.save(commit = False)
            habit.user = request.user
            habit.save()
            return redirect("habit_list ")
        else:
            form = HabitForm()
        return render(request, "habits/add_habit.html",{
            "form": form
        })


