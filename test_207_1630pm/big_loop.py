import wx
import os
class Mywin_xx(wx.Frame):
   global src_staging
   global ff_1
   def __init__(self, parent, title):
      super(Mywin_xx, self).__init__(parent, title=title)
      self.InitUI()
   def InitUI(self):
      self.count = 0
      pnl = wx.Panel(self)
      vbox = wx.BoxSizer(wx.VERTICAL)
      hbox1 = wx.BoxSizer(wx.HORIZONTAL)
      hbox2 = wx.BoxSizer(wx.HORIZONTAL)
      self.text = wx.TextCtrl(pnl, size=(-1,200),style=wx.TE_MULTILINE)
      self.btn1 = wx.Button(pnl, label="Open a File")
      self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn1)
      hbox1.Add(self.text, proportion=1, flag=wx.ALIGN_CENTRE)
      hbox2.Add(self.btn1, proportion=1, flag=wx.RIGHT, border=10)
      vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)
      vbox.Add(hbox1, proportion=1,flag=wx.EXPAND|wx.ALIGN_CENTRE)
      pnl.SetSizer(vbox)
      self.Centre()
      self.Show(True)
   def OnClick(self, e):
     wildcard="zip and tar(gz) file |*.zip;*.ZIP;*.tar.gz;*.tar"
     dlg = wx.FileDialog(self, "Choose a file", src_staging, "", wildcard,wx.FD_OPEN)
     if dlg.ShowModal() == wx.ID_OK:
        ff_1 = dlg.GetPath()
        print(ff_1)
        self.text.SetValue(ff_1)
     dlg.Destroy()

	 
ex1=wx.App
Mywin_xx(None,'Extracting file ')
ex1.MainLoop()