#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import json
import sys
track=[]
consumer_key='FamvsN0TZBSWVmztTg5u5qhJZ'
consumer_secret='Y5gjuIRiJEnaBdhrLoWdQNNrRPiDdtiZfGiL0X0aLfAzvQC8pC'
access_token='294589117-stbXfYqWcoX7H14zHxWnooXHcAWwkAr42XA6Q5he'
access_token_secret='2d52qymkwoGJpRuczcM6WNjqRh6GogbzxZo5XsNJeYg9y'


class StdOutListener(tweepy.StreamListener):
	def on_data(self, data):
		try:
			decoded = json.loads(data)
			print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'])
			print ''
			return True
		except KeyboardInterrupt:
			return False

	def on_error(self, status):
		print status

if __name__ == '__main__':
	listener = StdOutListener()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = tweepy.Stream(auth, listener)

	for i in range(3):
		keyword=raw_input('Input a keyword to search')
		stream.filter(track=[keyword.decode('UTF-8')],async=True)