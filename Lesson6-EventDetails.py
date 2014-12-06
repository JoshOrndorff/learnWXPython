#!/usr/bin/env python
import wx

# By now you're good at binding event handler classes to events. But so far we
# have bound a new event handler function to each button. In this lesson we'll
# discover another way to do it.

# It doesn't have to be called CoolerFrame. Since this is an example, I'll
# choose a name that reflects that. In general, you should give your classes
# meaningful names that reflect what they do.
class ExampleFrame(wx.Frame):
	# Remember __init__ is the constructor function.
	def __init__(self, parent):
	
		# As usual, we call the original wx.Frame constructor.
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Adding Numbers", size=(300, 120))
		
		# Create a new panel that is a member of the frame
		self.panel = wx.Panel(self)

		# Create the static text and buttons
		self.question = wx.StaticText(self.panel, label="How many should I add to the total?", pos=(20, 20))
		self.result = wx.StaticText(self.panel, label="Total is: 0", pos=(40, 90))
		self.btn1 = wx.Button(self.panel, label="1", pos=(20,50))
		self.btn3 = wx.Button(self.panel, label="3", pos=(120, 50))


		# Bind the buttons to the event handler
		self.btn1.Bind(wx.EVT_BUTTON, self.OnClick)
		self.btn3.Bind(wx.EVT_BUTTON, self.OnClick)


		# We will need a variable to keep track of the total.
		# This does not have anything to do with wxPython, it is just normal OOP.
		self.total = 0

	# The event handler function
	def OnClick(self, e):
		buttonClicked = e.GetEventObject()
		numToAdd = int(buttonClicked.GetLabel())

		self.total += numToAdd

		self.result.SetLabel("Total is: {}".format(self.total))



# ----------- Main Program Below -----------------

app = wx.App(False)

frame = ExampleFrame(None) 

frame.Show()

app.MainLoop()



# ----------- Exercises Below -----------------

#1. Add another button to add 5 to the total.
#   Note, you don't need to add another event handler function. Isn't that nice?

#2. Add a button that allows the user to reset the total.
#   Is it best to make a new event handler in this case?

#3. It is not ideal to take the number we are adding from  the button's label.
#   It would be better to write our own button class that extends wx.Button.
#   Our class will be almost identical, but it will have a variable that stores
#   An int representing how much we should increase the total by. This allows
#   us to change the label on the button to something like "Add Three" too.
#   Write that button class and change the program to use it.
