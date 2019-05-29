from django.urls import path
from . import views

app_name = 'subs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:subUrl>/', views.redirect_url, name='redirect_url'),
]