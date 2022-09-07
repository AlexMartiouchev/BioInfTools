from django.urls import path

from . import views

urlpatterns = [
    # ex /pricheck/
    path('', views.index, name='index'),
    # ex /pricheck/results/
    path('results/', views.results, name='results')
]
