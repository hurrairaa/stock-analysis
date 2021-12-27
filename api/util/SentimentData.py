import praw
from cleantext import clean


class SentimentData:

    @staticmethod
    def get_raddit_data(query):
        reddit = praw.Reddit(client_id='XWI3ykxxVjhkZd-L8I56qw', client_secret='kiPnpA2NNDevbL69_JWUYHyu32JaxQ',
                             user_agent='Sentiment Analysis')
        hot_posts = reddit.subreddit(query).hot(limit=10)
        data = ""
        for post in hot_posts:
            data = data + " " + post.selftext

        return SentimentData.clean_data(data)

    @staticmethod
    def clean_data(data):
        return clean(data,
                     fix_unicode=True,  # fix various unicode errors
                     to_ascii=True,  # transliterate to closest ASCII representation
                     lower=True,  # lowercase text
                     no_urls=False,  # replace all URLs with a special token
                     no_emails=False,  # replace all email addresses with a special token
                     no_phone_numbers=False,  # replace all phone numbers with a special token
                     no_digits=False,  # replace all digits with a special token
                     no_punct=False,  # remove punctuations
                     replace_with_punct="",  # instead of removing punctuations you may replace them
                     replace_with_url="<URL>",
                     )
