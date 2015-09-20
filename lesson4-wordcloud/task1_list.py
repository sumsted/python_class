import tweepy

consumer_key='WGgMJ45kp75aE1AFwKmtdz02X'
consumer_secret='4JLDBL6LWtHAuaEAEWcvGQdv0rA38XyWdESt7mt54mOCRwAKb4'
access_token='3718506375-NjC2n870SayUqGC7dK3Pp7CvLH1o5zTBOkjtCSf'
access_token_secret='YiDmYxNcmu55cn044BifipbGVfocsf9boUmWLELxhHtWD'

# get mah tweets
def download_tweets():
    username = "marvel"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # authenticate to the twitter api with your credentials
    api = tweepy.API(auth)

    # how many tweets to get (limit 200)
    num_tweets = 100

    # access your timeline
    tweets = api.user_timeline(screen_name = username, count = num_tweets)

    # start a list to hold your tweet info
    my_tweets = []

    for tweet in tweets:
        my_tweets.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])
        print("tweet: ", tweet.text)

if __name__ == '__main__':
    download_tweets()