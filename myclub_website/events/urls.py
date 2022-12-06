from django.urls import path
from . import views

urlpatterns = [
    #int:numbers
    #str: strings
    #path: whole urls /
    #slug: hyphen-  and underscore_
    #UUID: universally unique identifier

    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.all_events,name="list-events"),
    
]
