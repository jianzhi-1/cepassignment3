import re

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q

from django.views.generic import View
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Food, Restaurant, Rating

from .forms import FoodForm

# Create your views here.


def showImages(request, food_id):

    food = Food.objects.get(id=food_id)
    food_picturename = food.picturename
            
    return HttpResponse('<img src="/media/images/' + food_picturename + '.png"/>')

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

class FoodList(ListView):
    model = Food
    queryset = Food.objects.all()
    
    def get_queryset(self):
        rating = self.kwargs['rating']
        if rating == '':
            self.queryset = Food.objects.all()
            return self.queryset
        else:
            self.queryset = Food.objects.filter(rating__num__iexact=rating)
            return self.queryset
            
    def get_context_data(self, **kwargs):
        context = super(FoodList, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        return context

    
class FoodDetail(DetailView):
    model = Food

class FoodCreate(CreateView):
    model = Food
    form_class = FoodForm
    success_url = reverse_lazy('listing')

class FoodUpdate(UpdateView):
    model = Food
    form_class = FoodForm
    success_url = reverse_lazy('listing')
    
class FoodDelete(DeleteView):
    model = Food
    success_url = reverse_lazy('listing')
            #url = reverse('detail', args=str(food.id))
    
class FoodByRestaurant(ListView):
    model = Food
    
    queryset = Food.objects.all()
    def get_queryset(self):
        restaurants = self.kwargs['restaurants']
        pieces = restaurants.split('/')
        
        queries = [Q(rest__name__iexact=value) for value in pieces]
        # Take one Q object from the list
        query = queries.pop()
        # Or the Q object with the ones remaining in the list
        for item in queries:
            query |= item
        # Query the model
        allfood = Food.objects.filter(query).distinct().order_by('resturant__name')
        self.queryset = allfood #Setting the queryset to allow get_context_data to apply count
        return allfood
    
    def get_context_data(self, **kwargs):
        context = super(FoodByRestaurant, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        return context
    