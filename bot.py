import tweepy, random, time

CONSUMER_KEY = 'QmhEbzsdv5aJHtM2CBHT1nvWP'
CONSUMER_SECRET = 'HmkvdQIqOHC0NW5x0DWW9TKLVWvkY95cJS2XPUvkAazNzUIMqR' # Make sure access level is Read And Write in the Settings tab
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
