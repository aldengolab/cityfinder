from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *



def priorities(request):
  # All this happens before any HTML is sent to the browser
  request.session.set_test_cookie()
  if request.session.test_cookie_worked():
    request.session.delete_test_cookie()
  else:
    return HttpResponse("Please enable cookies and try again.")
  
  # this enables us to show any previous selections if user went back
  # to the first page. 
  # context = {'previous_priorities': []}
  # if request.session and request.session['priorities']:
  #   for priority in request.session['priorities']:
  #     context['previous_priorities'].append(priority)

  return render(request, 'priorities.html')

def transform_post_to_dict(post):
  '''
  Given a post item, transform values into a dict
  '''

  d = {}
  post = post.items()[1]
  key = str(post[0])
  values = str(post[1]).split(',')

  d[key] = values

  return d

def process_weather_input(post):
  '''
  Given a list from JS like so ["sun", 2, "temp", 0]
  Change to dict like so {"sun" : 2, "temp" : 0}
  '''
  print post
  print type(post)
  weather_dict = {}


def preferences(request):
  # we get ordered priorities from revious page via request.POST
  # we now save these priorities for later use, or if user goes back
  request.session['priorities'] = request.POST

  return render(request, 'preferences.html')

def preferences_citysize(request):
  request.session["priorities"] = request.POST
  return render(request, 'preferences_citysize.html')

def preferences_weather(request):
  request.session["citysize"] = request.POST
  return render(request, 'preferences_weather.html')

def preferences_community(request):
  request.session["weather"] = request.Post
  return render(request, 'preferences_community.html')

def city_results_experimental(request):
  cities = ["New York", "Minneapolis", "Chicago", "Seattle", "Miami", "Austin", "Dallas", "San Francisco", "San Diego", "Salt Lake City"]
  match_scores = [98, 76, 74, 53, 32, 31, 30, 25, 20, 10, 5]
  fall_temp = [12, 65, 78, 32, 65, 78, 98, 90, 12, 65]
  winter_temp = [12, 65, 78, 32, 12, 65, 78, 32, 12, 65]
  spring_temp = [78, 32, 12, 65, 78, 32, 12, 65, 78, 32]
  summer_temp = [80, 89, 70, 67, 47, 89, 90, 50, 70, 77]
  bike_score = [80, 89, 70, 67, 47, 89, 90, 50, 70, 77]
  transit_score = [78, 32, 12, 65, 78, 32, 12, 65, 78, 32]
  walk_score = [12, 65, 78, 32, 65, 78, 98, 90, 12, 65]

  return render(request, 'city_results_experimental.html', {"cities": cities})

def city_results(request):

  #first get priorities list and turn it into a dict
  priorities = transform_post_to_dict(request.session['priorities'])
  print priorities

  #now get post from preferences view and turn into dict too
  preferences = transform_post_to_dict(request.POST)
  print preferences

  #city size preference to dictionary
  citysize_preference = process_weather_input[request.session["citysize"]]
  print citysize_preference

  #weather preferences to dictionary
  weather_preferences = process_weather_input(request.session["weather"])
  print weather_preferences

  #community preferences to dictionary
  community_preferences = transform_post_to_dict(request.POST)
  print community_preferences

  #example to pass in to results to show city data
  #need to call here a func algorithm // Alden
  walk_city = Walk.objects.order_by('-city')[:50]

  return render(request, 'city_results.html', {'results': walk_city})


#each view has to return an httpresponse or exception
'''
func to get kwargs, transform and get data from model objects

#keep this code for example
#  walk_city = Walk.objects.order_by('-city')[:50]


getting data:
Walk.objects.get(city='Chicago')
.filter(**kwargs)
.exlucde(**kwargs)
.get().filter()
.filter(something __lt=10)
.filter(city__inexact="Chicago")
.filter(city__icontains="Chicago")

get data from multiple table objects

'''

