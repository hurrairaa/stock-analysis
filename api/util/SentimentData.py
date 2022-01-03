import praw
from cleantext import clean


class SentimentData:

    @staticmethod
    def get_raddit_data(query):
        reddit = praw.Reddit(client_id='XWI3ykxxVjhkZd-L8I56qw', client_secret='kiPnpA2NNDevbL69_JWUYHyu32JaxQ',
                             user_agent='Sentiment Analysis')
        hot_posts = reddit.subreddit(query).hot(limit=4)
        data = ""
        for post in hot_posts:
            data = data + " " + post.selftext

        return SentimentData.clean_data(data)

    @staticmethod
    def clean_data(data):
        # return clean(data)
        return data
