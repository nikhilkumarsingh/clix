from os import path
from functools import partial
try:
	from Tkinter import *
except ImportError:
	from tkinter import *
try:
	from ScrolledText import ScrolledText
except:
	from tkinter.scrolledtext import ScrolledText
import xerox


class clipboard():
	def __init__(self, clips):
		"""
		initialization function
		"""
		# root (top level element) config
		H, W = 250, 300
		self.root = Tk()
		self.root.title("clix")
		self.root.minsize(width = W, height = H)
		self.position_window()

		img = PhotoImage(file = "icon.png")
		self.root.tk.call('wm', 'iconphoto', self.root._w, img)

		# canvas to hold main scrollbar
		self.canvas = Canvas(self.root, height = H - 10, width = W - 20)
		self.canvas.pack(side = RIGHT, expand = True)

		# scrollbar config
		scrollbar = Scrollbar(self.root, command = self.canvas.yview)
		scrollbar.pack(side = RIGHT, fill = 'y')
		self.canvas.configure(yscrollcommand = scrollbar.set)
		self.canvas.bind('<Configure>', self.on_configure)

		# main frame (inside root) config
		self.mainFrame = Frame(self.root, padx = 5, pady = 5, bg = "white")
		self.mainFrame.pack(fill = BOTH, expand = True, side = TOP)

		# canvas window over mainFrame
		self.canvas.create_window((0,0), window = self.mainFrame, anchor = 'nw')

		# clipboard frames inside main frame
		colors = ['orange', 'tomato', 'gold']*2

		if clips is None:
			clips = ["","","","","",""]
		elif len(clips) < 6:
			clips = clips[::-1] + [""]*(6-len(clips))
		else:
			clips = clips[::-1]

		self.frames = []
		self.textBoxes = []
		for i in range(6):
			frame = Frame(self.mainFrame, padx = 5, pady = 5, bg = colors[i])

			Button(frame, text = "clip it", font = "Helvetica 12 bold",  
				    command = partial(self.copy_to_clipboard, i), relief = RAISED, 
				    padx = 5, pady = 5, bg = 'dark violet', fg = 'white').grid(row = 0, column = 0, ipady = 10)

			textBox = ScrolledText(frame, height = 3, width = 20,font = "Helvetica 12 bold")
			textBox.insert(END, clips[i])
			textBox.grid(row = 0, column = 1, sticky = E, padx = 5)
			self.textBoxes.append(textBox)

			frame.pack(fill = 'both', expand = True, pady = 5)
			self.frames.append(frame)

		# call mainloop of Tk object
		self.root.mainloop()
		self.root.quit()


	def copy_to_clipboard(self, idx):
		"""
		function to copy text of frame no. idx to clipboard
		"""
		text = self.textBoxes[idx].get("1.0", END)
		xerox.copy(text)


	def on_configure(self, event):
		"""
		utility function to enable scrolling over canvas window
		"""
		self.canvas.configure(scrollregion = self.canvas.bbox('all'))


	def position_window(self):
		"""
		function to position window to current mouse position
		"""
		x, y = self.root.winfo_pointerxy()
		self.root.geometry('+%d+%d' % (x, y))	


if __name__ == "__main__":
	example_clips = ["hello", "copy it"]
	clipboard(example_clips)
