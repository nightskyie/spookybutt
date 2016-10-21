import tweepy, random, time

CONSUMER_KEY = '9x9cmpOwKKxoyNi8u0GgRP4Q5'
CONSUMER_SECRET = 'HMrnh1Xm0ZeYejhHO4cjXfl6ADEanAUje1UYNF6iB97e0etk1z' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = '704447793578905600-CPxgLv1WwondScXViz16GYhPiJINym4'
ACCESS_SECRET = 'SRgDLWXVKlK5324HGnQBgHRnICFE4rPBwmU4XLFrbTuSP'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('lines.txt','r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    print line
    time.sleep(360)
