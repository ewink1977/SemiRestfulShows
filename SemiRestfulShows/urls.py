from django.urls import path
from . import views

appname = 'shows'

urlpatterns = [
    path('', views.showlist, name = 'home'),
    path('shows/new', views.newshow, name = 'newshow'),
    path('shows', views.showlist, name = 'showlist'),
    path('shows/<int:showid>', views.display_show, name = 'display_show'),
    path('shows/<int:showid>/edit', views.edit_show, name = 'edit_show'),
]