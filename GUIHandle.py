#6/10/2015
#Michael Kohlmann
#devCodeCamp - Personal Project

#Note, this is overly commented, because it's a new topic to me. I want to be able to come back to it later and understand it.


#use the Try-Except for the import, because wxPython is not a default Library, if the user doesn't have it installed, it will throw an error.
try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

    
#Start of GUIHandle Class. wxPython has it's own class, that our GUI will inherit. Then we add our own functions for
#building the exact window we want, and how we want to react to buttons.
class GUIHandle(wx.Frame):
    def __init__(self,parent,id,title): # GUI Class Constructor
        wx.Frame.__init__(self,parent,id,title) # wxPython Sub Constructor, inherits the wx Frame
        self.parent = parent # remember to keep track of yours parents
        self.initialize() # Create the window and add buttons and objects

    def initialize(self):
        sizer = wx.GridBagSizer() # Put button objects on Grid Spacing (GridBagSizer is the grid layout manager)
        
        # Typical Process is Create Object, then Add the object to the layout manager (sizer in this case)
        # Add TextBox
        self.entry = wx.TextCtrl(self, -1, value=u"Enter your task comments here.") # Creates the text box
        sizer.Add(self.entry, (0,0), (1,4), wx.EXPAND) # Adds the text box to the sizer manager
        
        # Add Button
        startButton = wx.Button(self, -1, label="START")
        startButton.SetBackgroundColour(wx.GREEN)
        sizer.Add(startButton, (1,1))
        
        pauseButton = wx.Button(self, -1, label="PAUSE")
        pauseButton.SetBackgroundColour(wx.WHITE)
        pauseButton.SetForegroundColour(wx.RED)
        sizer.Add(pauseButton, (1,2))
        
        stopButton = wx.Button(self, -1, label="STOP")
        stopButton.SetBackgroundColour(wx.WHITE)
        stopButton.SetForegroundColour(wx.RED)
        sizer.Add(stopButton, (1,3))
        
        # Add Label
        self.label = wx.StaticText(self,-1,label=u'Time Tracker Status')
        self.label.SetBackgroundColour(wx.BLUE)
        self.label.SetForegroundColour(wx.WHITE)
        sizer.Add( self.label, (2,0),(1,4), wx.EXPAND )
        
        self.SetSizerAndFit(sizer) # This tells our GUI to use the sizer designated above when layout out the buttons.
        self.Show(True) # after the window is constructed, Show it.

        
        
##### Start Main Process Here
if __name__ == "__main__":
    app = wx.App() #First need to construct the from the wxPython Library
    frame = GUIHandle(None,-1,"Time Tracker") #After that, we construct the actual frame.
    app.MainLoop() #The wxPython MainLoop is what scans and looks for event calls.