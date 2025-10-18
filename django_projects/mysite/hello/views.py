from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    num_visits = request.session.get('num_visits', 1) # gets current count, default to 1 if it isn't set yet
    response = HttpResponse(f'view count={num_visits}') # display count
    request.session['num_visits'] = num_visits + 1 #increment count
    response.set_cookie('dj4e_cookie', '22d7fa9c', max_age=1000) # set cookie (from probelm desc)
    if num_visits > 4:
        request.session['num_visits'] = 1

    return response