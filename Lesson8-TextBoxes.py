#!/usr/bin/env python
import wx

# In this lesson you will learn about the wx.TextCtrl, and simple message boxes.
# You are familiar with both of these widgets, and you will likely find them very useful.

class HelloFrame(wx.Frame):

	def __init__(self, parent):
	
		# Do you remember why include the next line?
		wx.Frame.__init__(self, parent, wx.ID_ANY, "I'd like to meet you")
		
		# We will create a panel here because it is good practice not to put widgets directly in a frame.
		self.panel = wx.Panel(self)
		
		# A simple wx.StaticText label just like we've used before
		self.prompt = wx.StaticText(self.panel, label="Enter your name:", pos=(40, 10))
		
		# Another wx.StaticText. This one does not have a label yet. We will set it later.
		self.response = wx.StaticText(self.panel, pos=(40, 100))
		
		
		# Now, this lesson's main feature. A wx.TextCtrl
		# TextCtrl can also take a size=(width, height) argument.
		self.nameBox = wx.TextCtrl(self.panel, pos=(200, 10))

		# A wx.Button just like before
		self.btnSubmit = wx.Button(self.panel, label="Submit", pos=(150, 50))
		self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmitSimple)
		
		
		
		
	def OnSubmitSimple(self, e):
		# This event handler is called when the submit button is clicked.
		# The purpose is to greet the user by name. It is the fancy version of: print "Hello", name
		
		# First we get whatever text the user entered in the text box
		name = self.nameBox.GetLineText()
		
		# Now we finally greet the user by displaying a message in our response wx.StaticText
		self.response.SetLabel("Nice to meet you, " + name)
		
	def OnSubmitComplex(self, e):
		# This event handler is used instead after you change the binding on line 30.
		# This one makes sure the user entered a name.
		
		# Again, we get whatever text the user entered in the text box
		name = self.nameBox.GetValue()
		
		# This time we make sure the user entered something before greeting them.
		if len(name) > 0:
			self.response.SetLabel("Nice to meet you, " + name)
		else:
			# If they didn't enter a name, we display a message telling them so.
			# The dialog box that we create here is called a Modal Dialog. With modal dialogs
			# you can't interact with the main window until you close the modal dialog.
			# There are lots of modal dialogs like open and save windows, or error messages.
			wx.MessageBox("Hey, you didn't enter a name!", "Info", wx.OK)



# ----------- Main Program Below -----------------

# Define the app
app = wx.App(False)

# Create a regular old wx.Frame
frame = HelloFrame(None)

# Show the frame
frame.Show()

# Make the app listen for clicks and other events
app.MainLoop()




# ----------- Exercises Below -----------------

#0. Remember to read through all the code and comments to at least get the basic idea before starting the exercises.

#1. What is the purpose of line 12? Write you answer below. Writing helps clearly identify answers.

#2. The submit button is currently bound to a simple even handler called OnSubmitSimple.
#   But there is also a fancier event handler called OnSubmitComplex.
#   Change the binding on line 30 to use the fancier event handler and then run the program again.

#3. The last argument on line 58 is wx.OK That tells the program to include an "OK" button.
#   Change it from wx.OK to wx.CANCEL and see what happens.
#   Now change it to wx.OK | wx.CANCEL and see what happens.
#   We could handle the two button clicks differently if we wanted to (but we don't yet).

#4. This one is not related to text boxes or message boxes, but it is interesting.
#   We always call frame.Show() from our main program.
#   But really almost every frame should be shown as soon as it is created.
#   So we can move the show call to inside the constructor. Remove the frame.Show() from the main program
#   And put it inside the constructor. (Maybe somewhere near line 32)
#
#   Hint:
#   If you got an error it is probably because you just put the *exact* same line inside the constructor.
#   Ask your-SELF if the line needs to be modified at all.

#5. If the user doesn't enter a name, we can give them a default name.
#   Change the info message to "Hey, you didn't enter a name! I'll call you Dave."

#6. Good job on #5. It was a little easy. Now we need to actually call the user Dave.
#   wx.TextCtrl widgets have a method .SetValue("text here")
#   Use this message in the complex event handler to call the anonymous user Dave.

#7. It would be nice it Dave didn't have to click the submit button after we named him.
#   Even though OnSubmitComplex is an event handler, it can still be called just like any other function.
#   After we name him Dave, call self.OnSubmitComplex(None)