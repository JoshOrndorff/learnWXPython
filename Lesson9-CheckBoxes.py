#!/usr/bin/env python
import wx

# Here is a simple demonstration of how a checkbox can be used.
# This lesson is based on a zetcode tutorial. (http://zetcode.com/wxpython/widgets/#checkbox)

class CheckBoxFrame(wx.Frame):

	def __init__(self, parent):

		
		
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Let's learn about checkboxes.")
		
		self.panel = wx.Panel(self)

		# Create our checkbox. I always prefix my checkbox variable names them with cb.
		# It is up to you whether you do this or not.
		self.cbShowTitle = wx.CheckBox(self.panel, label='Show title', pos=(20, 20))
        
		# By default our box will be checked. I bet you can guess how to change that.
		self.cbShowTitle.SetValue(True)

		# We will bind out checkbox to an event handler.
		# Before we have only bound buttons and EVT_BUTTON.
		# Now we see that most widgets have some events.
		# The EVT_CHECKBOX event occurs whenever a checkbox changes state
		self.cbShowTitle.Bind(wx.EVT_CHECKBOX, self.OnToggleShowTitle)

		# Here is a useful line to know. (It has nothing to do with checkboxes.)
		# Calling the Centre() method (note the British spelling) on a frame
		# automatically places it in the centre of your window.
		self.Centre()
   
	# Here is the event handler for whenever the checkbox is checked or unchecked.
	# What is that 'e' again? What does it do?
	def OnToggleShowTitle(self, e):
        
		# Earlier we learned about setValue() now we'll use getValue()
		# these methods are called getters and setters. They often come in pairs.
		isChecked = self.cbShowTitle.GetValue()
		
		if isChecked:
			self.SetTitle("Let's learn about checkboxes.")            
		else: 
			self.SetTitle('')  


# ----------- Main Program Below -----------------

# Define the app
app = wx.App(False)

# Create a regular old wx.Frame
frame = CheckBoxFrame(None)

# Show the frame
frame.Show()

# Make the app listen for clicks and other events
app.MainLoop()




# ----------- Exercises Below -----------------

#0. Remember to read through all the code and comments to get the basic idea before starting the exercises.

#1. What is the purpose of the 'e' in line 37?
#   Write you answer below. Writing helps clearly identify answers.

#2. Change the default value of the check box so it is unchecked when the program starts.
#   Is there anything else you need to change so the program is consistent?

#3. I've typed the sentence "Let's learn about checkboxes." twice in this program (lines 13 and 44).
#   That means if I want to change that string later I would have to change it in two different places.
#   It would be better to make a variable to hold the string. Create a variable on line 11
#   to hold the sentence and then change lines 13 and 44 to use the variable instead.

#4. Okay, this program works well, but some users might not notice the title changing.
#   Add a wx.StaticText to the panel, and when the checkbox changes, also update the wx.StaticText
#   to say "The box is checked." or "The box is not checked."