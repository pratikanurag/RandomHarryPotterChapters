import tweepy
from time import sleep
import random
import requests
auth = tweepy.OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
auth.set_access_token('ACCESS_TOKEN', 'ACCESS_SECRET')
api = tweepy.API(auth)

my_file=open('chapters.txt','r')
file_lines=my_file.readlines()
my_file.close()

for line in file_lines:
# Add try ... except block to catch and output errors
    try:
        print(line)
        if line != '\n':
            t_line = 'Harry Potter Chapter of the day:- ' + line
            api.update_with_media('scar.jpg',t_line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(86400)