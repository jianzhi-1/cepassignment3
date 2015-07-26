from django.conf.urls import patterns, include, url
from django.contrib import admin
from recipe import views
from django.conf import settings

from recipe.models import Food
from django.views.generic import ListView, DetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cepassignment1final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^list/$', views.food_list, name = "food_list"),
    url(r'^admin/', include(admin.site.urls)),
    
    #assignment 1
    
    url(r'^food/(?P<food_id>\d+)$', views.food_detail, name="food_detail"),
    url(r'^list/(?P<rating>.*)$', views.food_list, name = "food_list"),
    url(r'^showImages/(?P<food_id>\d+)$', views.showImages, name = "show_image"),
    url(r'^restaurant/(?P<restaurants>.*)$', views.food_restaurants, name='restaurant_list'),
    
    #assignment 2
    url(r'^listall/$', ListView.as_view(model=Food), name = "listing"),
    url(r'^lists/(?P<rating>.*)$', views.FoodList.as_view(), name='recipe_list'),
    #url(r'^detail/(?P<pk>\d+)S', DetailView.as_view(model=Food)),
    url(r'^add/$', views.FoodCreate.as_view(), name = 'food_add'),
    url(r'^food/(?P<pk>\d+)/edit/$', views.FoodUpdate.as_view(), name = 'food_update'),
    url(r'^food/(?P<pk>\d+)$', views.FoodDetail.as_view(), name = 'food_detail'),
    url(r'^food/(?P<pk>\d+)/delete$', views.FoodDelete.as_view(), name = 'food_delete'),
)

urlpatterns += patterns(
    'django.views.static',
    (r'^media/images/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}),
)


