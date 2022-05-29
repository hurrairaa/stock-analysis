import praw
import requests
import json
from cleantext import clean


class SentimentData:

    @staticmethod
    def get_raddit_data(query):
        reddit = praw.Reddit(client_id='XWI3ykxxVjhkZd-L8I56qw', client_secret='kiPnpA2NNDevbL69_JWUYHyu32JaxQ',
                             user_agent='Sentiment Analysis')
        # hot_posts = reddit.subreddit(query).hot(limit=100)
        hot_posts = reddit.subreddit("StockMarket+wallstreetbet+business").search(query)

        return hot_posts
        data = ""
        for post in hot_posts:
            data = data + " " + post.title

        return SentimentData.clean_data(data)

    @staticmethod
    def clean_data(data):
        # return clean(data)
        return data

    @staticmethod
    def get_stock_twit_data(ticker):
        url = "https://api.stocktwits.com/api/2/streams/symbol/"+ticker+".json"

        response = requests.request("GET", url)

        return json.loads(response.text)['messages']

