from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pregunta_id>/vote/', views.vote, name='vote'),
]
