#! /usr/bin/evn python

#import the graphical library
#import the time module

class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Title Here")
		
		#Make a new Panel
		
		#Make the start button
		#Make the other ten buttons
		#Hide the other ten buttons
		
		#Bind all the buttons to their event handlers
		
	# Event handler for the start button
	def OnStart(self, e):
		#Make the start button disappear
		self.startTime = time.time()
		#Make Button One appear
		
	#Other event handlers here
	
	#Remember the last event handler needs to print the final time.
	
	
# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()