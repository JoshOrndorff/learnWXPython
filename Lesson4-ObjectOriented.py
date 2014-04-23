#!/usr/bin/env python
import wx

# So far we have been creating GUIs (Graphical User Interfaces) with a procedural approach.
# That means we just write a bunch of commands in the main program to create our GUI.
# A more common method is an object-oriented approach. That means we will create classes
# to represent our GUIs with classes. This program is the same as Lesson 2 but object oriented.

# We define a class called CoolerFrame because it is cooler than the original wx.Frame
# Because we put wx.Frame is parentheses on line 12 instead of object, this class "inherits" from wx.Frame
# Inherits means that the CoolerFrame has everything a wx.Frame has, plus the stuff we add.
class CoolerFrame(wx.Frame):
	# Remember __init__ is the constructor function. It sets up or "initializes" the new CoolerFrame
	def __init__(self, parent):
	
		# We still want to do all stuff that the original wx.Frame constructor does, so we call it first.
		# Always do this.
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Our Title")
		
		# Create a new panel that is a member of the frame
		panel = wx.Panel(self) #Notice I put self in parentheses this time.

		# Create a button, and put it in my panel
		btnClickMe = wx.Button(self, label="Click Me", pos=(20,20))

		# Make the button do something!
		# Call self.OnClickMe instead of just OnClickMe
		btnClickMe.Bind(wx.EVT_BUTTON, self.OnClickMe)

	# Now the event handler is part of the class.
	# That means it has to have self as the first argument.
	def OnClickMe(self, e):
		print "Yay! You clicked it."
	



# ----------- Main Program Below -----------------

# We still define the app in the main program
app = wx.App(False)

# Instead of creating a normal wx.Frame we create an instance of our new class
# It is named after me because I created it.
joshsFrame = CoolerFrame(None) 

# Still show the frame in the main program
joshsFrame.Show()




# Still make the app listen for clicks, and other events in the main program
app.MainLoop()



# ----------- Exercises Below -----------------

#1. Add a wx.StaticText somewhere on the panel.
#   This is similar to before, but now it is object oriented. (That means the word self will be involved)

#2. After I show my frame, create a second CoolerFrame and name it after yourself. Then show it.
#   Do you see the advantage of the object oriented approach? We can easily create many of the same frames now.
#   This will be useful for panels as well later on.