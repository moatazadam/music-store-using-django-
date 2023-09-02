from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.Index , name = 'index'),
    path('fav' , views.Favorites , name = 'favorites'),
    path('contact' , views.Contact , name = 'contact'),
    path('<int:id>' , views.Single_Page , name = 'singlepage'),
    path('specials' , views.Specials , name = 'specials'),
    path('artists' , views.Artists , name = 'artists'),


]