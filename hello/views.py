from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import *

from .helpers import *

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

@csrf_exempt
def member_id(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    dob = request.POST.get('dob')
    country = request.POST.get('country')
    member_id = generate_id(first_name, last_name)

    member = Members(member_id=member_id, first_name=first_name, last_name=last_name, date_of_birth=dob, country=country).save()

    data = {
        'first_name' : first_name,
        'last_name' : last_name,
        'dob' : dob,
        'country' : country,
        'member_id' : member_id
    }
    return HttpResponse(
        json.dumps(data), 
        content_type='application/json'
        )

@csrf_exempt
def validate_member_id(request):
    member_id = request.POST.get('member_id')
    member = Members.objects.filter(member_id=member_id)
    if member:
        return render(request, "member_found.html")
        
    else:
        return render(request, "member_not_found.html")
        

# simple html to input member id
def validate_member_id_html(request):
    return render(request, "validate_member_id.html")