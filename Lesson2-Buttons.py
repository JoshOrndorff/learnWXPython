#!/usr/bin/env python
import wx

#You will experiment with this file by changing it and adding to it.
#But first just run it and see what it does.

#Now that you have run the file, skip down to the main program.


#This function is an event handler. It will run when a certain even occurs.
def OnClickMe(e):
	print "Yay! You clicked it."

#----Main Program Below-----

#In wx we always sart by creating a wx.App. I like to call it "app".
app = wx.App(False)

#Create a new frame.
frame = wx.Frame(None, wx.ID_ANY, "Josh's Title")

#Create a new panel
#A panel is not a whole frame, it is just a smaller collection of things inside the frame.
panel = wx.Panel(frame)

#Create a button, and put it in my panel
btnClickMe = wx.Button(panel, label="Click Me", pos=(20,20), size=(200,20))

#Make the button do something!
#btnClickMe.Bind(wx.EVT_BUTTON, OnClickMe)

#Show the frame
frame.Show()

#Make the app listen for clicks, and other events
app.MainLoop()


# ----------- Exercises Below -----------------

#0. Read through the main program and get a rough understanding of what it does.

#1. Change the position of the frame. (You've done this before, but I want you to stay sharp.)

#2. Change the text on the button, and make the button taller.
#   You may also play with the button size and location.

#3. The button doesn't do anything. Uncomment line 30 to *Bind* the button to an event handler.
#   An event handler is just a function that runs when an event happens.
#   In this case the event handler is called OnClickMe, and the event is clicking btnClickMe.
#   It is good style to start event handlers with "OnSomething"
#   Do you see the text "Yay! You clicked it" in your terminal? Great!

#4. Create another button and add it to my panel. Make it print some other text to the terminal.