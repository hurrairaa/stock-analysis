import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.settings import PROJECT_ROOT
from api.util.SentimentData import SentimentData
import pandas as pd
import pickle

@api_view(['GET'])
def get_sentiment_analysis(request):
    with open(os.path.join(PROJECT_ROOT + '/FinBert.pkl'), 'rb') as f:
        finbert = pickle.load(f)
        analysis_text = SentimentData.get_raddit_data('AAPL')
        result = finbert(analysis_text)
        return Response(result[0])
    # finbert = pickle.load(open(os.path.join(PROJECT_ROOT+'/FinBert.pkl')))

