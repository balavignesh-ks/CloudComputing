from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

from .models import Movie
from .forms import MovieForm

def index(request):
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movies/index.html', context)

def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/show.html', {'movie': movie})
    
def add(request):
        if request.method == 'POST':
            print("Here 1")
            form = MovieForm(request.POST)
            print("Here 2")
            if form.is_valid(): # Failing Here.... Need to Check further in this ....
                print("Here 3")
                _title = request.POST['title']
                _director = request.POST['director']
                _release_date = request.POST['release_date']
                _genre = request.POST['genre']
                _duration = request.POST['duration']
                print("Here 4")
                movie = Movie(title=_title, director=_director,release_date=_release_date,genre=_genre,duration=_duration)
                print("Here 5")
                movie.save()
                print("Here 6")
                
                return render(request, 'movies/index.html')  

        else:
            form=MovieForm()
            
        return render(request, "movies/add.html", {"form": form})