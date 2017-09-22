from django.shortcuts import render

from Messenger.models import Person


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
