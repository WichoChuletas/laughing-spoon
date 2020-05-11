"""Platzigram Views"""
#Django
from django.http import HttpResponse
from django.http import JsonResponse
#Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting"""
    return HttpResponse('Hello World!')

def time_server(request):
    """Return time server"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, Hi! The time server is {now}'.format(now=str(now)))

def sort_integers(request):
    """Return Sort Intergers in JSON"""
    numbers = sorted(map(int, request.GET['numbers'].split(',')))
    return HttpResponse(json.dumps(numbers, indent=4), content_type='application/json')

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {name}, you are not welcome here'.format(name=name)
    else:
        message = 'Hello {name}, Welcome to Platzigram'.format(name=name)
    return HttpResponse(message)