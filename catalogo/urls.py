from django.urls import path 
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('photo/', views.BookListView.as_view(), name='photo'),
    path('photo/<int:pk>', views.BookDetailView.as_view(), name='photo-detail'),
]