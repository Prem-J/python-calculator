from __future__ import division
from Tkinter import *


personal_pink = '#8B89FF'
personal_grey = '#C4C4C4'

numbersListFrame = []
symbolsListFrame = []

symbols = ['+', '-', 'x', u'\u00F7', '=', u'\u232B']
calculateList = []
symbolCalculateList = []

class Calculator:
  def __init__(self, master):
    self.master = master
    master.title("Calculator")
    

    self.createDisplay(master) #Creates Display at Top Which will contain numbers
    self.createNumberTiles(master)
    self.createSymbolTiles(master)
    
  
  ###SYMBOLS
  def createSymbolTiles(self, frame):
    #Create Symbols Frame and Populate
    symbolsFrame = Frame(frame, height=463, width=75, bg=personal_pink)
    symbolsFrame.place(x=433, y=287)

    for box in range(6):
      frame = Frame(symbolsFrame, height=76, width=76, bg=personal_grey)
      frame.grid(row=box, column=0, pady=(0, 10))
      symbolsListFrame.append(frame)

    self.createSymbolLabels()

  def createSymbolLabels(self):    
    for i in symbolsListFrame:
      i.bind('<Button-1>', self.symbolClicked)
      label = Label(i, text=symbols[symbolsListFrame.index(i)], bg=personal_grey, font="Arial 36")
      label.place(x=38, y=38, anchor='center')
      label.bind('<Button-1>', self.symbolClicked)

  def symbolClicked(self, event):
    symbol = ''
    
    try:
      symbol = event.widget.cget('text')
    except Exception as ex:
      symbol = symbols[symbolsListFrame.index(event.widget)]

    print(symbol)

    if symbol == u'\u232B':
      self.deletePressed()
    elif symbol == '=':
      self.equalsPressed()
    else:
      self.operatorPressed(symbol)


  def deletePressed(self):
    output = outputString.get()
    outputString.set(output[0:(len(output)-1)])

  def equalsPressed(self):
    output = outputString.get()
    if output != "":
      calculateList.append(output)    
      self.clearOutput()
    stuff = []

    for i in range(len(calculateList)):
      stuff.append(calculateList[i])
      if i < len(symbolCalculateList):
        stuff.append(symbolCalculateList[i])

    calculateString = eval(''.join(stuff))

    outputString.set(calculateString)
    calculateList[:] = []
    symbolCalculateList[:] = []

  def operatorPressed(self, symbol):
    output = outputString.get()
    calculateList.append(output)
    if symbol == 'x':
      symbolCalculateList.append('*')
    elif symbol == u'\xf7':
      symbolCalculateList.append('/')
    else:
      symbolCalculateList.append(symbol)
    self.clearOutput()

  ###DISPLAY
  def createDisplay(self, masterFrame):
    display = Frame(masterFrame, height=92, width=500, bg="white", bd=5, relief="solid")
    display.pack_propagate(0)
    display.pack(pady=(20, 0))
    #Outer Frame for display

    displayText = Label(display, textvariable=outputString, font="Arial 64", width=13)
    displayText.place(x=250, y=41, anchor="center")

  ###NUMBERS
  def configureRowColumnSizes(self, frame):
    for row in range(4):
      if row % 2 == 0:
        frame.rowconfigure(index=row, minsize=100, pad=35)
        frame.columnconfigure(index=row, minsize=100, pad=35)
      else:
        frame.rowconfigure(index=row, minsize=100)
        frame.columnconfigure(index=row, minsize=100)

  def createNumberTiles(self, frame):
    #Create Numbers Frame and Populate
    numbersFrame = Frame(frame, height=516, width=358, bg=personal_pink)
    numbersFrame.place(x=20, y=287)
    self.configureRowColumnSizes(numbersFrame)
  
    for row in range(4):
      for column in range(3):
        frameBox = Frame(numbersFrame, height=100, width=100, bg=personal_grey)
        frameBox.grid(row=row, column=column)
        numbersListFrame.append(frameBox)

    self.createNumberLabels()
    
  def createNumberLabels(self): #Add Labels to Tiles
	list = numbersListFrame
	k = 0
	extras = ['C', '0', '.']
	frames = [9, 10, 11]
	for i in list:
		print list.index(i)
		i.bind('<Button-1>', self.numberClicked)
		if list.index(i) in frames:
  			label = Label(i, text = extras[k], font = "Arial 48", bg = personal_grey)
			label.place(x = 50, y = 50, anchor = "center")
			label.bind('<Button-1>', self.numberClicked)
			k+=1
		else :
  			label = Label(i, text = str((list.index(i)) + 1), font = "Arial 48", bg = personal_grey)
			label.place(x = 50, y = 50, anchor = "center")
			label.bind('<Button-1>', self.numberClicked)

  def numberClicked(self, event):
    try:
        if event.widget.cget('text')=='C':
        	self.clearOutput()
        else:
        	self.addNumber(event.widget.cget('text'))
    except Exception as ex:
    	if numbersListFrame.index(event.widget)==9:
    		self.clearOutput()
      	elif numbersListFrame.index(event.widget)==10:
        	print(0)
        	self.addNumber('0')
      	elif numbersListFrame.index(event.widget)==11:
        	print('.')
        	self.addNumber('.')
      	else:
        	print(numbersListFrame.index(event.widget) + 1)
        	self.addNumber((numbersListFrame.index(event.widget) + 1))

  def addNumber(self, num):
    outputString.set(outputString.get()+ str(num))

  def clearOutput(self):
  	outputString.set('')


root = Tk()

outputString = StringVar()

root.geometry("540x900")
root.configure(background=personal_pink)
root.resizable(False, False)
my_calculator = Calculator(root)
root.mainloop()
