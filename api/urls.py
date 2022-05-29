from django.urls import path
from . import views



urlpatterns =[
    path('sentiment', views.get_sentiment_analysis, name='routes')
]