from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title','director','release_date_0','release_date_1','genre','duration']
    
    title = forms.CharField(required=True, max_length=200)
    director = forms.CharField(required=True, max_length=30)
    release_date_0 = forms.DateField(required=True)
    release_date_1 = forms.TimeField(required=True)
    genre = forms.CharField(required=True, max_length=200)
    duration = forms.FloatField(required=True)
    
    