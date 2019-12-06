from django.db import models
from django.urls import reverse 
import uuid 



class Genre(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class photo(models.Model):
    
	title = models.CharField(max_length=200)
	author = models.ForeignKey('artista', on_delete=models.SET_NULL, null=True)
    
	summary = models.TextField(max_length=1000, help_text='Ingrese una pequeña informacion de la foto')
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre)
    
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular photo across whole library')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Book availability',
	)

	class Meta:
		ordering = ['due_back']

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.book.title})'


class Author(models.Model):
	"""Model representing an author."""
	first_name = models.CharField(max_length=100)
	address = models.DateField(null=True, blank=True)
	date = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name']

	def get_absolute_url(self):
		return reverse('artidta', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.first_name}'	