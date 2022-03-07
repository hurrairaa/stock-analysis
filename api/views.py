import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.settings import PROJECT_ROOT
from api.util.SentimentData import SentimentData
import pandas as pd
from api.serialziers import Dictionary, DictionarySerializer
import pickle
from rest_framework import serializers


@api_view(['GET'])
def get_sentiment_analysis(request):
    with open(os.path.join(PROJECT_ROOT + '/FinBert.pkl'), 'rb') as f:
        finbert = pickle.load(f)
        hot_posts = SentimentData.get_raddit_data('AAPL')
        hot_tweets = SentimentData.get_stock_twit_data('AAPL')
        data = []
        analysis = 0

        for tweet in hot_tweets:
            if len(tweet['body']) == 0:
                continue
            result = finbert(tweet['body'])

            score = calculateScore(result[0]["score"], result[0]['label'])
            analysis = analysis + score
            data.append({
                "analysis": score,
                "label": result[0]['label'],
                "post": tweet['body'],
            })

        for post in hot_posts:
            if len(post.selftext) == 0:
                continue
            result = finbert(post.selftext)
            score = calculateScore(result[0]["score"], result[0]['label'])
            analysis = analysis + score
            data.append({
                "analysis": score,
                "label": result[0]['label'],
                "post": post.selftext
            })
        # analysis = analysis/

        analysis = analysis / (len(data))
        # GenericSzl = getGenericSerializer(model)
        dictionary = Dictionary({
            "complete_analysis": analysis,
            "data": data
        })
        return Response(DictionarySerializer(dictionary).data)


def calculateScore(score, label):
    value = 50
    # score = score/100
    if label == 'neutral':
        if score < 0.6:
            value = value - 10 * score
        else:
            value = value + 10 * score
    elif label == 'positive':
        value = value + 30 * score
    elif label == 'negative':
        value = value - 30 * score

    return value
    # result = finbert(analysis_text)
    # return Response(analysis)

# def get_queryset(self):
#     model = self.kwargs.get('model')
#     return getattr(models, model).objects.all()
# def getGenericSerializer(model_arg):
#     class GenericSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = model_arg
#             fields = '__all__'
#
#     return GenericSerializer

# finbert = pickle.load(open(os.path.join(PROJECT_ROOT+'/FinBert.pkl')))
