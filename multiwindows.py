#!python

from tkinter import *
from tkinter import scrolledtext

textList = ["Poem-a-Day is the original and only daily digital poetry series featuring over 250 new, previously unpublished poems by today’s talented poets each year. On weekdays, poems are accompanied by exclusive commentary and audio by the poets. ", "The series highlights classic poems on weekends. Launched in 2006, Poem-a-Day is distributed via email, web, and social media to 500,000+ readers free of charge. The series is curated by twelve poets from across the country who have wide-ranging expertise and editorial perspectives. Learn more about the 2019 guest editors and revisit the 2018 guest editors and the poems they curated.","I hoard dirt in my ears; months later, I pull out a summer dress. The dress is not a dress to be worn but to be hung, like a flag on a wobbly pole that is noticed only when crowded in the mouths of those near it. The dress is not a dress to be worn but to be hung, like an NDN condemned to death by the judiciary of historical ignorance, an enactment of white fellowship and care. We all bear the dress, not as an article of clothing, but as an ontological imprint. To bear is not to wear, of course. To bear and to birth, however, are from the same neighborhood of experience. It is there, in the neighborhood of experience, that my childhood home is nowhere to be found. And so, my childhood home could be anything, even a dress made out of dirt."]

class mainWin(Frame):

	def __init__(self, root, textList):

		Frame.__init__(self,root,pady = 10)
		self.root = root
		self.grid(row = 0,column = 0)
		self.createWidget()
		self.textList = textList
		
	def createWidget(self):
	
		self.updateButton = Button(self, width = 24, text = 'Details', command = lambda : self.ecpConfig(self.root))
		self.updateButton.grid(row = 0, column = 0 , padx = 6, pady = 3, sticky = 'e')
		
	def ecpConfig(self,base):
	
		for entry in self.textList:
		
			ecpWindow(base,entry)
		

class ecpWindow:

	def __init__(self, root, line):
	
		self.reportWindow = Toplevel(root)
		self.reportWindow.title("Test Window")
		self.reportWindow.transient(root)
		
		self.reportResults = scrolledtext.ScrolledText(self.reportWindow,width = 40, wrap = WORD,state = "normal")
		self.reportResults.grid(row = 0, column = 0, columnspan = 2)
		
		self.keyword = StringVar()
		self.entry = Entry(self.reportWindow, textvariable = self.keyword)
		self.entry.grid(row = 1, column = 0)
		
		self.button = Button(self.reportWindow, text = "Search", command = self.show)
		self.button.grid(row = 1, column = 1)
		
		self.line = line
		self.reportResults.insert(END,self.line)
		self.reportResults.tag_config('match', foreground = 'red')

		
	def show(self):
	
		print(self.keyword.get())
		
		startPoint = '1.0'
		
		while True:
		
			index = self.reportResults.search(self.keyword.get(), startPoint, END)
			
			if not index:
			
				break
				
			startPoint = '{}+{}c'.format(index, len(self.keyword.get()))
			self.reportResults.tag_add('match', index, startPoint)

			
if __name__ == "__main__":

	root=Tk()
	root.title("MuliWindows")
	mainWin(root,textList)
	root.mainloop()