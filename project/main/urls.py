from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('reasons', views.whyweloveyou, name='why')
]