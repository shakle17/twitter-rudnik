#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tweepy
import json
import sys
sys.stdout.flush()


consumer_key='FamvsN0TZBSWVmztTg5u5qhJZ'
consumer_secret='Y5gjuIRiJEnaBdhrLoWdQNNrRPiDdtiZfGiL0X0aLfAzvQC8pC'
access_token='294589117-stbXfYqWcoX7H14zHxWnooXHcAWwkAr42XA6Q5he'
access_token_secret='2d52qymkwoGJpRuczcM6WNjqRh6GogbzxZo5XsNJeYg9y'

count_list = 0
track=[]
stream=None
class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget

    def write(self,string):
		try:
			self.text_space.insert('end', string)
			self.text_space.see('end')
		except:
			pass

class StdOutListener(tweepy.StreamListener):
	def on_data(self, data):
		decoded = json.loads(data)
		print '@%s: ' % (decoded['user']['screen_name'])
		return True
		

	def on_status(self, status):
		return status

	def on_error(self, status):
		return False

listener = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class Gui(object):
	def __init__(self):
	
		global count_list

		self.word_list=[]
		self.top = Tk()
		self.top.geometry('700x900')
		self.top.resizable(width=FALSE, height=FALSE)
		self.top.configure(background="#62ACFF")

		self.scrollbar = Scrollbar(self.top)
		self.scrollbar.pack( side = RIGHT, fill=Y )

		
		self.list_box = Listbox(self.top, height=5, yscrollcommand = self.scrollbar.set, bg="#C0DEFF")
		self.scrollbar.config( command = self.list_box.yview )
		self.list_box.pack()
		self.list_box.place(x=300, y=100)	

		self.list_tweets = Listbox(self.top, width=80, height=38, yscrollcommand = self.scrollbar.set , xscrollcommand= self.scrollbar.set, bg="#C0DEFF", relief=GROOVE)
		self.scrollbar.config( command = self.list_tweets.yview )
		self.list_tweets.pack()
		self.list_tweets.place(x=20, y=300)	


		self.key_label = Label(self.top, text="Key Words", font = "Verdana 20 bold", bg="#62ACFF")
		self.key_label.pack( side = LEFT)
		self.key_label.place(x=100, y=50)

		self.tweets_label = Label(self.top, text="Tweets", font = "Verdana 22 bold", bg="#62ACFF")
		self.tweets_label.pack( side = TOP)
		self.tweets_label.place(x=300, y=250)

		self.list_label = Label(self.top, text="Selected Words", font = "Verdana 15 bold", bg="#62ACFF")
		self.list_label.pack( side = LEFT)
		self.list_label.place(x=100, y=100)

		self.key_entry = Entry(self.top, bd =5, width=30, bg = "#C0DEFF")
		self.key_entry.pack(side = RIGHT)
		self.key_entry.place(x=300, y=50)

		self.add = Button (self.top, text="Add Word", command=self.add_list, activebackground="#8DC3FF", bg='#C0DEFF')
		self.add.pack()
		self.add.place(x=570, y=50)

		self.stop = Button (self.top, text="Stop", width=17 , command=self.stop, activebackground="#8DC3FF", bg='#C0DEFF')
		self.stop.place(x=300, y=180)
		try:
			self.top.mainloop()
		except KeyboardInterrupt:
			exit()

	def add_list(self):
		global stream
		if stream:
			stream.disconnect()
		stream = tweepy.Stream(auth, listener,timeout=10)
		global count_list
		self.entry_text = self.key_entry.get()
		self.word_list.append(self.entry_text)
		try :
			stream.filter(track=self.word_list,async=True)
			sys.stdout = (StdoutRedirector(self.list_tweets))
		except:
			sys.exit()		
		self.list_box.insert(count_list, self.entry_text)
		self.key_entry.delete(0, END)
		count_list += 1

	def stop(self):
		global stream
		stream.disconnect()

Gui()
