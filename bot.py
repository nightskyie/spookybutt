import tweepy, random, time

CONSUMER_KEY = '6hPodTrmF9YNevjgEwTzAxK9s'
CONSUMER_SECRET = 'wYi6WTB1VI2QqOLboPGsDqiCMfbgxBp2RRjwmfHxaaOPDyhEQu' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = '704447793578905600-rdeAO1LKfzOmBsmDJWMcQIPkhr6DY6B'
ACCESS_SECRET = 'WjmSUQ754chnxlbhNhWCOfG495yzASD9yezAz2RVPeqUw'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('lines.txt','r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    print line
    time.sleep(5)
