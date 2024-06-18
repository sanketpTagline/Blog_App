from django.urls import path
from . import views

app_name = "author"
urlpatterns = [
   path('', views.BloggerListView.as_view(), name='all_authors'),
   path('<int:pk>',views.BloggerDetailView.as_view(),name='author_detail'),
   # path('<int:pk>/profile/',views.AuthorRegisterForm.as_view(), name = 'author_profile')
   path('register/',views.AuthorRegisterView.as_view(),name = 'register')
   
]
