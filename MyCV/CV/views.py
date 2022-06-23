from django.shortcuts import render
from .models import Person
# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def person_by_id (request,person_id):
    person = Person.objects.get(pk=person_id)
    return render(request, 'index.html',{'person':person})
