from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
def index(request):

    num_photo=photo.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_artista=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count() 
    
 
    return render(
        request,
        'index.html',
        context={'num_photo':num_photo,'num_artista':num_artista,'num_lugar':num_lugar,},
    )
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model = Book
