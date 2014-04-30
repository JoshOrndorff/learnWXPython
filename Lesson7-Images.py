#!/usr/bin/env python
import wx

# Here is a fairly simple lesson that demonstrates a fun and very useful feature of wx python.
# We will display some pictures in your programs.
# As usual, you may run the program to see what it does.

class ImagePanel(wx.Panel):

	def __init__(self, parent):
	
		# Remember, we need to run the __init__ from the normal wx.Panel.
		wx.Panel.__init__(self, parent)

		# This line creates a wx.Image object that contains our picture
		self.leftPictureFile = wx.Image("programmer.jpg", wx.BITMAP_TYPE_ANY)
		
		# Next we convert the wx.Image to wx.Bitmap
		# Only wx.Bitmap objects can be displayed by this method.
		self.leftPictureBitmap = self.leftPictureFile.ConvertToBitmap()
		
		# Finally we display a wx.StaticBitmap which is a lot like a wx.StaticText
		self.leftPicture = wx.StaticBitmap(self, wx.ID_ANY, self.leftPictureBitmap, pos=(5, 5))



# ----------- Main Program Below -----------------

# Define the app
app = wx.App(False)

# Create a regular old wx.Frame
frame = wx.Frame(None, wx.ID_ANY, "Let's look at some images")

# Create a copy of our new custom Imagepanel and give it frame as a parent
panel = ImagePanel(frame)

# Show the frame
frame.Show()

# Make the app listen for clicks and other events
app.MainLoop()




# ----------- Exercises Below -----------------

#1. Having that programmer.jpg file in the LearnWxPython directory makes the folder look disorganized.
#   There is another copy of the same file in the assets directory.
#   Change the program to use the version in the assets directory instead.
#   Then delete the one in the root directory to make it look nicer and be sure your code works.

#2. Because images must always be converted to bitmaps, these staps are frequently combined into a single line.
#   To do this *move* the .ConvertToBitmap() method from line 20 to the end of line 16.
#   If you like, delete my comments from lines 17-19. Your choice.
#
#   Note: Combining these is similar to what we did when we asked for number input.
#   Original Way
#   	num = raw_input("Enter a number")
#   	num = int(num)
#
#   Combined Way
#   	num = int(raw_input("Enter a number"))

#3. Add a second picture from your own documents to the panel and display it beside the awesome baby.
#   Resize the frame as necessary to make sure both pictures fit properly.
#
#   Hint: If you don't remember how to resize a frame, it goes on the line that starts with frame = wx.Frame