from Tkinter import *

count_list = 0

class Gui(object):
	def __init__(self):

		global count_list

		
		self.top = Tk()
		self.top.geometry('700x600')
		self.top.resizable(width=FALSE, height=FALSE)

		self.scrollbar = Scrollbar(self.top)
		self.scrollbar.pack( side = RIGHT, fill=Y )

		
		self.list_box = Listbox(self.top, height=5, yscrollcommand = self.scrollbar.set)
		self.scrollbar.config( command = self.list_box.yview )
		self.list_box.pack()
		self.list_box.place(x=300, y=100)	


		self.key_label = Label(self.top, text="Key Words", font = "Verdana 20 bold")
		self.key_label.pack( side = LEFT)
		self.key_label.place(x=100, y=50)

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
		self.search.pack()
		self.search.place(x=300, y=180)

		self.top.mainloop()

	def add_list(self):
		global count_list
		self.entry_text = self.key_entry.get()	
		self.list_box.insert(count_list, self.entry_text)
		self.key_entry.delete(0, END)
		count_list += 1


Gui()
