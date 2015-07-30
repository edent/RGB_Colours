#!/usr/bin/env python2.7
import tweepy
from PIL import Image
import numpy
import random

# Open the file containing all the things.
fid = open('colors.csv', 'r')
names = fid.readlines()

# Pick one at random
thing = random.sample(names, 1)[0]
colourName = thing.split(",")[1]
colourRGB = thing.split(",")[2]
fileName = "temp.png"

colourString = "0xFF"
colourString += format(int(thing.split(",")[5]),'X').zfill(2) + format(int(thing.split(",")[4]),'X').zfill(2) + format(int(thing.split(",")[3]),'X').zfill(2)

w,h=1024,768
img = numpy.empty((w,h),numpy.uint32)
img.shape=h,w

img[0:768,0:1024]=format(int(colourString,16))

pilImage = Image.frombuffer('RGBA',(w,h),img,'raw','RGBA',0,1)
pilImage.save(fileName)

#print "SAVED!"
# Send the tweet with photo
# Consumer keys and access tokens, used for OAuth
consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
status = colourName + "\n" + colourRGB + "\n"
api.update_with_media(fileName, status=status)
