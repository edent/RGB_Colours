import tweepy
import numpy as np
import scipy.misc as smp
import os
import sys
from random import randrange
from random import shuffle

#	Set up the square
data = np.zeros( (256,256,3), dtype=np.uint8)

#	Initial colour
start = randrange(255)
#print(start)
order = [0,1,2]
shuffle(order)
#print(order)

colourname = [format(start,"x").upper().zfill(2), "00", "00"]

hashtag = "#" + colourname[order[0]] + colourname[order[1]] + colourname[order[2]]

if (colourname[order[0]] != "00"):
	sum = int(colourname[order[0]],16) + 256 +256
elif (colourname[order[1]] != "00"):
	sum = int(colourname[order[1]],16) +256
else:
	sum = int(colourname[order[2]],16)

id_file = os.path.join(sys.path[0], "towns.txt")

towns = open(id_file)
town = towns.read().splitlines()[sum]

#	Loop through all the pixels
for x in range(256):
	for y in range(256):
		colours = [start, x, y]
		data[x,y] = [ colours[order[0]], colours[order[1]], colours[order[2]] ]

#	Generate and save image
img = smp.toimage(data)
img.save('cube.png')

#	Set up Twitter
consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

#	OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#	Creation of the actual interface, using authentication
api = tweepy.API(auth)

#	Status
status = town + "\nStarting at " + hashtag

#	Upload image & status
media_upload = api.media_upload('cube.png')
api.media_metadata_create(media_upload.media_id_string,"A three-dimentional color square")
api.update_status(status=status, media_ids=[media_upload.media_id_string])
