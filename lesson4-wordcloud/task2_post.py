'''
Created by @musegarden Al
Presented at https://github.com/nelsonam/meetup-sept15


'''
import tweepy

consumer_key='WGgMJ45kp75aE1AFwKmtdz02X'
consumer_secret='4JLDBL6LWtHAuaEAEWcvGQdv0rA38XyWdESt7mt54mOCRwAKb4'
access_token='3718506375-NjC2n870SayUqGC7dK3Pp7CvLH1o5zTBOkjtCSf'
access_token_secret='YiDmYxNcmu55cn044BifipbGVfocsf9boUmWLELxhHtWD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(status="Learning python at Memphis Chinese School!")
