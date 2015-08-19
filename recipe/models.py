from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import UserProfile

# Create your models here.
class Food(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, null=True)
    name = models.CharField(max_length = 255)
    information = models.TextField()
    picturename = models.CharField(max_length = 255, default = "")
    picture = models.ImageField(upload_to='')
    
    color = models.CharField(max_length=50, default = "yellow")
    fontcolor = models.CharField(max_length=50, default = "black")
    
    #for the rating
    rating = models.ForeignKey('Rating', related_name="recipe", null=True, blank=True)
    
    #for the restaurant
    restaurant = models.ManyToManyField('Restaurant', related_name="recipe", null=True, blank=True)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})
        
class Restaurant(models.Model):
    name = models.CharField(max_length = 255)
    information = models.TextField()
    content = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length = 8)
    color = models.CharField(max_length=50, default = "purple")
    fontcolor = models.CharField(max_length=50, default = "white")
    
    def __unicode__(self):
        return self.name
        
class Rating(models.Model):
    num = models.CharField(max_length = 2)
    information = models.TextField()
    color = models.CharField(max_length=50, default = "red")
    fontcolor = models.CharField(max_length=50, default = "black")
    
    def __unicode__(self):
        return self.num
        
