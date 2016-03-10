#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tweepy
import json
import sys


consumer_key='FamvsN0TZBSWVmztTg5u5qhJZ'
consumer_secret='Y5gjuIRiJEnaBdhrLoWdQNNrRPiDdtiZfGiL0X0aLfAzvQC8pC'
access_token='294589117-stbXfYqWcoX7H14zHxWnooXHcAWwkAr42XA6Q5he'
access_token_secret='2d52qymkwoGJpRuczcM6WNjqRh6GogbzxZo5XsNJeYg9y'

count_list = 0
track=[]

class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget

    def write(self,string):
        self.text_space.insert('end', string)
        self.text_space.see('end')

class StdOutListener(tweepy.StreamListener):
	def on_data(self, data):
		decoded = json.loads(data)
		print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'])
		print ''
		return True
		return False

	def on_error(self, status):
		print status

listener = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = tweepy.Stream(auth, listener)

class Gui(object):
	def __init__(self):

		global count_list

		
		self.top = Tk()
		self.top.geometry('700x900')
		self.top.resizable(width=FALSE, height=FALSE)

		self.scrollbar = Scrollbar(self.top)
		self.scrollbar.pack( side = RIGHT, fill=Y )

		
		self.list_box = Listbox(self.top, height=5, yscrollcommand = self.scrollbar.set)
		self.scrollbar.config( command = self.list_box.yview )
		self.list_box.pack()
		self.list_box.place(x=300, y=100)	

		self.list_tweets = Listbox(self.top, width=80, height=38, yscrollcommand = self.scrollbar.set)
		self.scrollbar.config( command = self.list_tweets.yview )
		self.list_tweets.pack()
		self.list_tweets.place(x=20, y=300)	


		self.key_label = Label(self.top, text="Key Words", font = "Verdana 20 bold")
		self.key_label.pack( side = LEFT)
		self.key_label.place(x=100, y=50)

		self.tweets_label = Label(self.top, text="Tweets", font = "Verdana 22 bold")
		self.tweets_label.pack( side = TOP)
		self.tweets_label.place(x=300, y=250)

		self.list_label = Label(self.top, text="Selected Words", font = "Verdana 15 bold")
		self.list_label.pack( side = LEFT)
		self.list_label.place(x=100, y=100)

		self.key_entry = Entry(self.top, bd =5, width=30)
		self.key_entry.pack(side = RIGHT)
		self.key_entry.place(x=300, y=50)
		self.add = Button (self.top, text="Add Word", command=self.add_list)
		self.add.pack()
		self.add.place(x=570, y=50)
		self.search = Button (self.top, text="Search", width=17)
		self.search.place(x=300, y=180)
		try:
			self.top.mainloop()
		except KeyboardInterrupt:
			exit()

	def add_list(self):
		global count_list
		self.entry_text = self.key_entry.get()
		stream.filter(track=[self.entry_text.decode('UTF-8')],async=True)
		sys.stdout = StdoutRedirector(self.list_tweets)
		self.list_box.insert(count_list, self.entry_text)
		self.key_entry.delete(0, END)
		count_list += 1

Gui()