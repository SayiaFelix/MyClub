from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<int:year>/<str:month>',views.home, name='home'),
    path('events',views.all_events, name='list-events'),
    path('venue',views.add_venue, name='venue'),
    path('list_venue',views.list_venues, name='list_venue'),
    path('show_venue/<venue_id>',views.show_venues, name='show_venue'),
]