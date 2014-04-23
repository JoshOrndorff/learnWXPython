#!/usr/bin/env python
import wx

# The CoolerFrame in this lesson is similar to the last lesson with a few additions.
# But the main program is different.
# Be sure you run the program to see what it does

class CoolerFrame(wx.Frame):
	# Remember __init__ is the constructor function. It sets up or "initializes" the new CoolerFrame
	def __init__(self, parent):
	
		# We still want to do all stuff that the original wx.Frame constructor does, so we call it first.
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Our Title")
		
		self.panel = wx.Panel(self)

		self.btnClickMe = wx.Button(self.panel, label="Click Me", pos=(20, 20))
		self.btnMeToo   = wx.Button(self.panel, label="Me Too", pos=(20, 40))
		
		# The following line is commented out for now. We'll investigate it in Exercise 1.
		#self.btnMeToo.Show(False)
		
		self.heading = wx.StaticText(self.panel, label="Let's Click Some Buttons", pos=(10, 5))

		# We want the buttons to do something when we click them. So let's bind them to event handler functions.
		self.btnClickMe.Bind(wx.EVT_BUTTON, self.OnClickMe)
		self.btnMeToo.Bind(wx.EVT_BUTTON, self.OnMeToo)

	# And Now we write the event handlers to determine *what* happens when the buttons are clicked.
	def OnClickMe(self, e):
		print "Yay! You clicked it."

	
	def OnMeToo(self, e):
		print "You clicked the second one."


# ----------- Main Program Below -----------------

# Define the app
app = wx.App(False)

# Create an instance of our class
frame = CoolerFrame(None) 

# Show the frame
frame.Show()

# Make the app listen for clicks and other events
app.MainLoop()




# ----------- Exercises Below -----------------

#1. Uncomment Line 21 and run the program again. What does that line do?

#2. Since btnMeToo is no longer visible right away, it is up to us to make it visible.
#   Let's make btnMeToo visible when btnClickMe is clicked.
#   To make something happen when a button is clicked, we add code to the event handler.
#   Add some code in line 32 to make btnMeToo appear.

#3. We're getting pretty good at GUI programming, but we're still printing to the terminal.
#   Let's change it so our messages go to the GUI window instead of the terminal.
#   replace the print command on line 31 with self.heading.SetLabel("Yay! You clicked it.")

#4. Do the same for btnMeToo

#5. Your final task is to make btnClickMe disappear when it is clicked.

# A final Note ---
#
# In this lesson we used SetLabel to change wx.StaticText widgets and Show to show and hide wx.Buttons.
# But either method can be used for any widget.
# For example, we could have used
#    self.btnClickMe.SetLabel("Don't click me")
# or 
#    self.heading.Show(False)