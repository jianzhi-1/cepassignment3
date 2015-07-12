from django.conf.urls import patterns, include, url
from django.contrib import admin
from recipe import views
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cepassignment1final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^food/(?P<food_id>\d+)$', views.food_detail, name="food_detail"),
    #url(r'^list/$', views.food_list, name = "food_list"),
    url(r'^list/(?P<rating>.*)$', views.food_list, name = "food_list"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^showImages/(?P<food_id>\d+)$', views.showImages, name = "show_image"),
    url(r'^restaurant/(?P<restaurants>.*)$', views.food_restaurants, name='restaurant_list'),
)

urlpatterns += patterns(
    'django.views.static',
    (r'^media/images/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}),
)
