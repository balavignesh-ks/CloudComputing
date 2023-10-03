from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = []
        labels = {'title': "Title", "director": "Director", 'release_date': "Release Date", "genre": "Genre", 'duration': "Duration",}
    
    title = forms.CharField(required=True, max_length=200)
    director = forms.CharField(required=True, max_length=30)
    release_date = forms.SplitDateTimeField(required=True, widget=forms.SplitDateTimeWidget(date_format="YYYY-MM-DD",time_format="HH:MM[:ss[.uuuuuu]][TZ]"))
    genre = forms.CharField(required=True, max_length=200)
    duration = forms.FloatField(required=True)
    
    