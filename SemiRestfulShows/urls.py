from django.urls import path
from . import views

urlpatterns = [
    path('', views.showlist, name = 'home'),
    path('shows/new', views.newshow, name = 'newshow'),
    path('shows', views.showlist, name = 'showlist'),
    path('shows/<showid>', views.display_show, name = 'display_show'),
    path('shows/<showid>/edit', views.editshow, name = 'editshow'),
    path('shows/<showid>/update', views.updateshow, name = 'updateshow'),
    path('shows/<showid>/destroy', views.destroy, name = 'destroyshow'),
]