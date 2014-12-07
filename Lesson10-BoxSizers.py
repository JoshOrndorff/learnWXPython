#! /usr/bin/env python

# By now you've probably been frustrated trying to get your buttons, static text
# labels and other controls (or "windows" as they're known in wx) to line up
# properly. Luckily wx has a native solution to that problem called sizers.
# There are several kinds of sizers, but this lesson will focus on BoxSizers
# because I find them to be the most useful and commonly used. (And I'm not good at using the other kinds :-/ )

import wx

class SizerFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(200, 150))

		self.panel = wx.Panel(self)

		# I'll create a few buttons and static texts.
		# These lines should be familiar to you by now.
		# Notice I am NOT specifying positions with pos=(x, y)
		self.question  = wx.StaticText(self.panel, label = "Choose a fruit?")
		self.btnApple  = wx.Button(self.panel, label = "Apple")
		self.btnOrange = wx.Button(self.panel, label = "Orange")


		# Now we create the BoxSizer object that will layout our windows
		self.sizer = wx.BoxSizer(wx.VERTICAL)

		# We'll add each of the windows to the sizer
		self.sizer.Add(self.question,  1, wx.ALL | wx.EXPAND, 3)
		self.sizer.Add(self.btnApple,  2, wx.ALL | wx.EXPAND, 3)
		self.sizer.Add(self.btnOrange, 2, wx.ALL | wx.EXPAND, 3)
			# The first argument is clearly the window that you want to add.
			# Next is the relative amount of space each window will occupy.
			# Currently, the StaticText takes 1/5 of the vertical space and each Button takes 2/5 of the vertical space.
			# The third argument is a series of flags that affect display. These are discussed in the exercises.
			# Finally, we specify the border space in pixels for the window.


		# And finally make the sizer work for our panel
		self.panel.SetSizerAndFit(self.sizer)

		self.Show()


# ----------- Main Program Below ---------------
app = wx.App(False)
# This time I'm passing parent and title to my new SizerFrame.
frame = SizerFrame(None, "Our first sizer")
app.MainLoop()

# ----------- Exercises Below -----------------

#0. Remember that these exercises are meant to guide you, but do not necessarily
#   Cover everything. You are encouraged to change anything and everything you
#   are curious about even if it is not mentioned in the exercises.

#1. Create another Button or StaticText and add it to the sizer.

#2. Change wx.VERTICAL to wx.HORIZONTAL when you make the sizer on line 26.

#3. Change the order in which you create the buttons. Does it affect the order
#   in which they are shown?

#4. The flags I've used are wx.ALL and wx.EXPAND.
#   Remove wx.EXPAND from one of the buttons and see what happens. Be sure to
#   resize the frame to really explore this. Now replace wx.EXPAND with
#   wx.SHAPED and see what happens.More information aobut these flags is at:
#   http://www.wxpython.org/docs/api/wx.Sizer-class.html

#5. This example uses only one vertical sizer. But it is common to nest one
#   sizers inside of each other. Create a second sizer to arrange the buttons
#   horizontally and insert it inside the first sizer.
#   |--------------------------|
#   | Choose a fruit           |
#   |                          |
#   |  |-------|   |--------|  |
#   |  | Apple |   | Orange |  |
#   |  |-------|   |--------|  |
#   |--------------------------|

#6. We can also SHOW the box around the BoxSizer like we did with StaticBox.
#   Create a StaticBox before your second sizer.
#   Change BoxSizer to StaticBoxSizer for your second sizer.
#   Then insert your StaticBox as the first argument.


