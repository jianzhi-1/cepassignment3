from django.shortcuts import render
from django.http import HttpResponse
from .models import Food, Restaurant, Rating
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import re
from django.db.models import Q

# Create your views here.

def showImages(request, food_id):
    return HttpResponse('<img src="/media/images/' + food_id + '.png"/>')

def food_list(request, rating):
    #allfood = Food.objects.all()
    allrestaurant = Restaurant.objects.all()
    text = "All available food"
    if rating == "":
        allfood = Food.objects.all().order_by("rating__num")
        total = allfood.count()
    else:
        allfood = Food.objects.filter(rating__num__iexact=rating)
        total = allfood.count()
        text = "All food with rating " + rating
    return render(request, 'recipe/index.html', {'recipe': allfood, 'total':total, 'resto':allrestaurant, "text":text})
    '''
    responsetext = ""
    for food in allfood:
        url = reverse('detail', args=str(food.id))
        responsetext += "<a href='" + url + "'>"
        responsetext += "<h3>" + food.name + "</h3>"
    
    return  HttpResponse(responsetext)
    '''
    
def food_detail(request, food_id):
    
    food = Food.objects.get(id=food_id)
    return render(request, 'recipe/food.html', {'food':food})
    '''
    food = Food.objects.get(id=food_id)
    responsetext = ""
    responsetext += "<h1>" + str(food.id) + "</h1>"
    responsetext += "<h3>" + food.name + "</h3>"
    #responsetext += '<img src="../food_headshots/' + str(food.id) + '.png" alt="' + food.name + '">'
    #responsetext += '<img src="cepassignment1final/food_headshots/1.png" alt="French Apple">'
    #responsetext += '<img src="' + food.headshot.path +'" alt="' + food.name + '">'
    responsetext += "<h3>" + food.information + "</h3>"
    
    return HttpResponse(responsetext)
    '''
    
def food_restaurants(request, restaurants):
    text = "Food at "
    allrestaurant = Restaurant.objects.all()
    for restaurant in allrestaurant:
        if restaurant.name == restaurants:
            text += restaurant.content
    
    pieces = restaurants.split('/')
    queries = [Q(restaurant__name__iexact=value) for value in pieces]
    query = queries.pop()
    for item in queries:
        query |= item
    print(query)
    
    
    allfood = Food.objects.filter(query).distinct().order_by('rating__num')
    total = allfood.count()
    return render(request, 'recipe/index.html', {'pieces':pieces, 'recipe':allfood, 'total':total, 'text':text})
    
def food(request, food_id):
    food = Food.objects.get(id=food_id)
    return render(request, 'recipe/food.html', {'food':food})
    