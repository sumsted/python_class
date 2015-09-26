'''
Created by @musegarden Al
Presented at https://github.com/nelsonam/meetup-sept15
'''
import tweepy
from wordcloud import WordCloud

# from command prompt
# pip install wordcloud
# pip install numpy
# pip install pil

consumer_key = 'WGgMJ45kp75aE1AFwKmtdz02X'
consumer_secret = '4JLDBL6LWtHAuaEAEWcvGQdv0rA38XyWdESt7mt54mOCRwAKb4'
access_token = '3718506375-NjC2n870SayUqGC7dK3Pp7CvLH1o5zTBOkjtCSf'
access_token_secret = 'YiDmYxNcmu55cn044BifipbGVfocsf9boUmWLELxhHtWD'

stops = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as",
         "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
         "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each",
         "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd",
         "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i",
         "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me",
         "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or",
         "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll",
         "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs",
         "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've",
         "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd",
         "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which",
         "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd",
         "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]


def download_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # authenticate to the twitter api with your credentials
    api = tweepy.API(auth)

    # how many tweets to get (limit 200)
    num_tweets = 100

    # access your timeline
    tweets = api.user_timeline(screen_name=username, count=num_tweets)

    # start a string to hold your tweet info
    my_tweets = ''

    for tweet in tweets:
        my_tweets += tweet.text#.encode("utf-8")

    return my_tweets


def genWordCloud(filename):
    text = download_tweets('numsted')

    words = WordCloud(width=500, height=500,
                      font_path='./DejaVuSans.ttf',
                      stopwords=stops)

    words.generate(text)
    words.to_file(filename)


if __name__ == '__main__':
    filename = 'mycloud.png'
    genWordCloud(filename)
