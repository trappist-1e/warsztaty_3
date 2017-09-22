from django.shortcuts import render

from Messenger.models import Person


def show_all(request):
    persons = Person.objects.all()
    return render(request, 'persons_list.html', {'persons': persons})
