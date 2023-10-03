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
        form = MovieForm(request.POST)
        if form.is_valid():
            _title = request.POST['title']
            _director = request.POST['director']
            _release_date_0 = request.POST['release_date_0']
            _release_date_1 = request.POST['release_date_1']
            _release_date = _release_date_0 + " " + _release_date_1
            _genre = request.POST['genre']
            _duration = request.POST['duration']
            movie = Movie(title=_title, director=_director,release_date=_release_date,genre=_genre,duration=_duration)
            movie.save()
            
            return HttpResponseRedirect(reverse('movies:index'))

    else:
        form=MovieForm()

    return render(request, "movies/add.html", {"form": form})
    
def edit(request, movie_id):
    context = {}
 
    try:
        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(request.POST or None, instance = movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('movies:show',kwargs={'movie_id':movie_id}))
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
 
    context["form"] = form
 
    return render(request, "movies/edit.html", context)
    
def remove(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    
    try:
        if request.method == 'POST':
            movie.delete()
        
            return HttpResponseRedirect(reverse('movies:index'))
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
        
    return render(request, "movies/remove.html", {'movie': movie})
    