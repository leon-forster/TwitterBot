
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, random

CONSUMER_KEY = 'key'
CONSUMER_SECRET = 'secret'
ACCESS_KEY = 'key'
ACCESS_SECRET = 'secret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open('spaz_man_do.txt','r') as filename:
    file_lines = filename.readlines()
random.shuffle(file_lines)
for line in file_lines:
     print line
     api.update_status(status=line)
     time.sleep(28800)
