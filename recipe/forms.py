from django import forms
from .models import Food, Restaurant, Rating
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Hidden, Button, HTML, Div, Field, Row, Fieldset

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ('user','picture',)
        
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "foodform"
        
        rating = Div('rating', css_class="col-xs-12", style = "padding:0px;")
        self.helper.layout.pop(5)
        self.helper.layout.insert(5,Fieldset("Select Rating",rating, Button("createratingmodal", value="Create New Rating", css_class="btn btn-primary btn-sm col-xs-12 ", data_toggle="modal", data_target="#myModal")))
        
        restaurant = Div('restaurant',css_class = "col-xs-12", style="padding:0px;") 
        self.helper.layout.pop(6)
        self.helper.layout.insert(6, Fieldset("Select Restaurant",restaurant, Button("createrestaurantmodal", value="Create New Restaurant", css_class="btn btn-primary btn-sm col-xs-12", data_toggle="modal", data_target="#myModal2")))
        
        self.helper.layout.append(Button('btn_createfood', 'Create Food', css_class='createfood', style="margin-top:15px;"))
        self.helper.layout.append(Hidden(name='btn_createfood', value="btn_createfood"))
        
    def full_clean(self):
        super(FoodForm, self).full_clean()
        if 'restaurant' in self._errors:
            self.cleaned_data['restaurant'] = []
            print("remove restaurant errors")
            del self._errors['restaurant']

        
    #helper = FormHelper()
    #helper.form_method = 'POST'
    #helper.add_input(Submit('Save', 'Save', css_class = 'btn-primary'))
    
#template
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(RatingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "ratingform"
        self.helper.layout.append(Hidden(name='btn_createrating', value="btn_createrating"))
        self.helper.layout.append(Button('btn_createrating', 'Create Rating', css_class='createrating', data_dismiss="modal"))
        

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "restaurantform"
        self.helper.layout.append(Hidden(name='btn_createrestaurant', value="btn_createrestaurant"))
        self.helper.layout.append(Button('btn_createrestaurant', 'Create Restaurant', css_class='createrestaurant', data_dismiss="modal"))


class FoodFormUpdate(forms.ModelForm):
    class Meta: 
        model = Food
        #fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(FoodFormUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "foodformupdate"
        
        self.helper.add_input(Submit('submit', 'Update'))
        