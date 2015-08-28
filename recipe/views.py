import re
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q

from django.views.generic import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect

from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Food, Restaurant, Rating

from .forms import FoodForm, RatingForm, RestaurantForm, FoodFormUpdate

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import UserProfile
from django.core.serializers.json import DjangoJSONEncoder

from django.http import Http404

# Create your views here.
def showImages(request, food_id):

    food = Food.objects.get(id=food_id)
    food_picturename = food.picturename
            
    #return HttpResponse('<img src="/media/images/{{food.picture}}">')
    return render(request, 'recipe/pic.html', {'FOOD': food})

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
    text = ""
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
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FoodList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        curruser = UserProfile.objects.get(user=self.request.user)
        if 'rating' in self.kwargs:
            rating = self.kwargs['rating']
            if rating == '':

                self.queryset = Food.objects.filter(user=curruser)
                return self.queryset
            else:
                #filter based on current logged in user
                self.queryset = Food.objects.all().filter(user=curruser).filter(rating__num__iexact=rating)
                return self.queryset
            
    def get_context_data(self, **kwargs):
        context = super(FoodList, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        #provided so that the avatar can be displayed in base.html
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context


    
class FoodDetail(DetailView):
    model = Food
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FoodDetail, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(FoodDetail, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context


class FoodCreate(CreateView):
    model = Food
    form_class = FoodForm
    success_url = reverse_lazy('listing')

class FoodUpdate(UpdateView):
    model = Food
    form_class = FoodFormUpdate
    #success_url = reverse_lazy('listing')
    success_url = '/listall/'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FoodUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(FoodUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(FoodUpdate, self).get_object()
        if not UserProfile.objects.get(user=self.request.user) == obj.user:
            raise Http404
        return obj
    
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
        curruser = UserProfile.objects.filter(user=self.request.user) 
        allfood = Food.objects.filter(user=curruser).filter(query).distinct().order_by('restaurant__title')
        self.queryset = allfood #Setting the queryset to allow get_context_data to apply count
        return allfood
    
    def get_context_data(self, **kwargs):
        context = super(FoodByRestaurant, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
class MyView(TemplateView):

    rating_form_class = RatingForm
    restaurant_form_class = RestaurantForm
    food_form_class = FoodForm
    template_name = "recipe/food_hybrid.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)
    
    
    def get(self, request, *args, **kwargs):

        kwargs.setdefault("createrating_form", self.rating_form_class())
        kwargs.setdefault("createrestaurant_form", self.restaurant_form_class())
        kwargs.setdefault("createfood_form", self.food_form_class())
        
        kwargs.setdefault('curruser', UserProfile.objects.get(user=self.request.user))
        return super(MyView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST,
        }
        

        if "btn_createrating" in request.POST['form']: 
            form = self.rating_form_class(**form_args)

            if not form.is_valid():

                return self.get(request, createrating_form=form)
            else:
                form.save()
                data = Rating.objects.all()
                result_list = list(data.values('id','num'))
                return HttpResponse(json.dumps(result_list, cls=DjangoJSONEncoder))

        elif "btn_createrestaurant" in request.POST['form']: 
            form = self.restaurant_form_class(**form_args)
            if not form.is_valid():
                return self.get(request, createrestaurant_form=form)
            else:
                form.save() 
                data = Restaurant.objects.all() 
                result_list = list(data.values('id','name'))
                return HttpResponse(json.dumps(result_list, cls=DjangoJSONEncoder)) #return to ajax as success with all the new records.

        elif "btn_createfood" in request.POST['form']:
            form = self.food_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,createfood_form=form) 
            else:
                try:
                    #Find out which user is logged in and get the correct UserProfile record.
                    curruser = UserProfile.objects.get(user=self.request.user)
                    obj = form.save(commit=False)
                    obj.user = curruser #Save the note note under that user
                    obj.save() #save the new object
                    
                except Exception, e:
                    print("errors" + str(e))
                response = {'status': 1, 'message':'ok'}
                return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder)) #return to ajax as success with all the new records.
            
        return super(MyView, self).get(request)


class FoodDelete(DeleteView):
    model = Food
    success_url = '/listall/'
    #success_url = reverse_lazy('listing')
            #url = reverse('detail', args=str(food.id))
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FoodDelete, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(FoodDelete, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(FoodDelete, self).get_object()
        if not UserProfile.objects.get(user=self.request.user) == obj.user:
            raise Http404
        return obj
        
class Landing(TemplateView):
    template_name = "recipe/landing.html"

    