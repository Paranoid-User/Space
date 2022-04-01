from django.urls import path
from Universe import views

urlpatterns = [
    path('', views.start, name='start'),
    path('centre/', views.centre, name='centre'),
    path('end/', views.end, name='end')
]
