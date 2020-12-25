from django.urls import path
from . import views

appname = 'shows'

urlpatterns = [
    path('shows/new', views.newshow, name = 'newshow'),
    path('', views.homeroute, name = 'home'),
    path('shows', views.showlist, name = 'showlist'),
    path('shows/<int:showid>', views.display_show, 'display_show')
]