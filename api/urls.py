from django.urls import path
from . import views



urlpatterns =[
    path('analysis', views.get_sentiment_analysis, name='routes')
]