from django.shortcuts import render, redirect
from django.http import HttpResponse, request, HttpResponseRedirect
from Messenger.models import Person
from django.contrib import messages

#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^new/', new_person),
#     url(r'^modify/(?P<id>(<\d+))', modify),
#     url(r'^delete/(?P<id>(<\d+))', delete),
#     url(r'^show/(?P<id>(<\d+))', show),
#     url(r'^$', show_all)


def show_all(request):
    persons = Person.objects.all()
    return render(request, 'persons_list.html', {'persons': persons})


def new_person(request):
    if request.method == "GET":

        return render(request, 'new_person.html', )

    else:
        n_person = Person.objects.create(first_name=request.POST[
            'first_name'], last_name=request.POST['last_name'],
                                         description=request.POST[
                                             'description'])

        return redirect('/new?new_person_added=True')
