#!/usr/bin/env python

#You will experiment with this file by changing it and adding to it.
#But first just run it and see what it does.

#Now that you have run the file, read through it and look at the exercises below.

#We always have to import wx before we can use it.
import wx


#In wx we always sart by creating a wx.App. I like to call it "app".
app = wx.App(False) #False means error messages will print in the normal way.

# Create a new frame (A frame is often casually called a window).
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
	# None means it is top level. It has no parent frame.
	# wx.ID_ANY is always the second argument. It is just a variable that = -1.
	# The third argument is the window's title.

# Show the frame.
frame.Show(True)

# MainLoop makes the app listen for clicks, and other events.
# This is always the last line of a wxPython app.
app.MainLoop()

# ----------- Exercises Below -----------------

#1. Change the title of your Frame to something new.

#2. Rename the variable bound to your frame to something like JoshsFrame.

#3. Add the argument size = (400,100) to the frame constructor on line 16.
#   What does it do?

#4. Add the argument pos=(1000,300) to the frame constructor on line 16.
#   What does it do?

#5. I've claimed that wx.ID_ANY is just a variable that equals -1.
#   Confirm that this is true. (Hint: This is not hard; don't overthink it.)
