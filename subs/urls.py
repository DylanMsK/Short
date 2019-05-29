from django.urls import path
from . import views

app_name = 'subs'

urlpatterns = [
    path('<str:subUrl>/', views.redirect_url, name='redirect_url'),
]