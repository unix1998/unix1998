import datetime
import zipfile
import tarfile
import glob 
import os
import re
import sys
import shutil 
#from tkinter.filedialog import askopenfilename
import tkinter
import tkinter.filedialog
import errno
import wx
import logging
from threading import Thread
 
from wx.lib.pubsub import pub
import time
#ex1=wx.App
keepGoing = True
dg_count = 100 
progressMax = 100
src_staging="D:\\staging"
ff_1="D:\\staging\\dcp\\dcp.zip"

################################################################
def get_app_string(full_path_name):
    # wx version change to \\ 
    return  full_path_name.split('\\')[2]
################################################################

################################################################

def backup_app(app_name):
    print ( "app_name")
    today2=datetime.datetime.now().strftime("%Y-%m-%d_%H_%M")
    backup_dir_name="D:\\opt\\backup\\"+app_name+"\\"+app_name+today2
    print (today2)
    doc_root_1="d:\\opt\\x_webroot\\"+app_name
    if len(os.listdir(doc_root_1)) > 0:
       try:
         copyDirectory(doc_root_1, backup_dir_name)#os.makedirs(backup_dir_name)
         print ("test dir")
       except OSError:
         pass  
       
    else:
       print ("no existing content there, so no backup")
	   
####################################################################


################################################################
def clean_folder(folder_name):
 for file_object in os.listdir(folder_name):
    file_object_path = os.path.join(folder_name, file_object)
    if os.path.isfile(file_object_path):
        os.unlink(file_object_path)
    else:
        shutil.rmtree(file_object_path)
		
################################################################

################################################################
def forceMergeFlatDir(srcDir, dstDir):
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)
    for item in os.listdir(srcDir):
        srcFile = os.path.join(srcDir, item)
        dstFile = os.path.join(dstDir, item)
        forceCopyFile(srcFile, dstFile)

def forceCopyFile (sfile, dfile):
    if os.path.isfile(sfile):
        shutil.copy2(sfile, dfile)

def isAFlatDir(sDir):
    for item in os.listdir(sDir):
        sItem = os.path.join(sDir, item)
        if os.path.isdir(sItem):
            return False
    return True


def copyTree1(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isfile(s):
            if not os.path.exists(dst):
                os.makedirs(dst)
            forceCopyFile(s,d)
        if os.path.isdir(s):
            isRecursive = not isAFlatDir(s)
            if isRecursive:
                copyTree1(s, d)
            else:
                forceMergeFlatDir(s, d)
############################################################
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

#################################################################
def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)
############################################
### extract tar file and tar.gz file #######################
def untar(ffname):
    global dg_count
    app_name=get_app_string(ffname)
    path_name_11="D:\\opt\\x_webroot\\"
    folder_zip=False
    ######################################
    folder_2_zip=False
    if (ffname.endswith(".tar")) or (ffname.endswith(".tar.gz")) :
        print (ffname)
		#############################################
        ####################### backup_app####################
        backup_app(app_name)
        #sys.exit(0)
        #############################################
        #############################################
        tar=tarfile.open(ffname)
        tar.extractall("D:\\opt\\temp")
        #sys.exit(0)
		#test extract all 
        for tarinfo in tar:
		     
             print (tarinfo.name)
             aa=tarinfo.name
             print (aa)
             if ((re.search("httpd.ini", aa,re.IGNORECASE)) or (re.search("web.conf", aa,re.IGNORECASE))) :
                 print (aa)
                 print ( " it has httpd.ini and web.conf , exit for safe ")
                 #exit (0), add remove here 
                 os.chdir("D:\\opt\\temp\\")
                 
                 print (aa)
                 
                 try:
                   os.remove(aa)
                 except OSError as e: # name the Exception `e`
                      print ("Failed with:", e.strerror )# look what it says
                      print ("Error code:", e.code)
             #if re.search(app_name,aa.split('/')[0],re.IGNORECASE):
             #   folder_zip = True
             
             #else:
             #  folder_zip = False
             #  break
			 # above are old style code , keep it as reference 
             if (app_name.lower() ==aa.lower()):
               folder_zip = True
               folder_2_zip=False
             elif ((re.search(app_name,aa.split('/')[0],re.IGNORECASE)) and  not (re.search("content",aa.split('/')[1],re.IGNORECASE))):
               folder_zip = True
               folder_2_zip=False
             elif ((re.search(app_name,aa.split('/')[0],re.IGNORECASE)) and  (re.search("content",aa.split('/')[1],re.IGNORECASE))):
               folder_2_zip = True 
               folder_zip = False
             else:
               folder_zip = False
               folder_2_zip = False
               break 
				 
             #print (aa)	
		
        #if folder_zip:
        #    path_name_11="D:\\opt\\x_webroot\\" 
        #else:
        #    path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
        #print (folder_zip)
        #print (path_name_11)
        #os.chdir(path_name_11)
        #tar.extractall()
        tar.close()
        dg_count=80
        #Mywin_xx.gauge.SetValue(30)
        if (folder_zip and not folder_2_zip):
           path_name_11="D:\\opt\\x_webroot\\"+ app_name + "\\"
           src_path="D:\\opt\\temp\\"+app_name+"\\"
	  
        elif ( folder_2_zip and not folder_zip):
           path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
           src_path="d:\\opt\\temp\\"+app_name+"\\"+"content"+"\\"
        else :
           path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
           src_path="d:\\opt\\temp\\"
	  
      
        #print (folder_zip)
        copyTree1(src_path,path_name_11)
  
        clean_folder("d:\\opt\\temp\\")
        print ("Extracted to webroot")
		
    else:
        print ("Not a tar.gz file:") 
		
### extract tar file and tar.gz file #######################		
###############################################################

##############################################################


#####################################################################################################
############## unzip a file to detination###########################################################
def unzip_1(zip_f):
  global dg_count
  print(zip_f)
  app_name=get_app_string(zip_f)
  path_name_11="D:\\opt\\x_webroot\\"
  #path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
  folder_zip=False
  folder_2_zip=False
  
  #############################################
  ####################### backup_app####################
  backup_app(app_name)
  #sys.exit(0)
  #############################################
  #############################################
  with zipfile.ZipFile(zip_f, "r") as zz:
    for fff1 in zz.namelist():
       print (fff1)
       zz.extractall("D:\\opt\\temp")
       if ((re.search("httpd.ini", fff1,re.IGNORECASE)) or (re.search("web.config", fff1,re.IGNORECASE))):
          print ( " it has httpd.ini and web.conf , removing them  ")
          os.chdir("D:\\opt\\temp\\")
          print ("AAAAAAAgain")
          print (fff1)
          #os.unlink(fff1)
          try:
            os.remove(fff1)
          except OSError as e: # name the Exception `e`
            print ("Failed with:", e.strerror )# look what it says
            print ("Error code:", e.code)
          
       if ((re.search(app_name,fff1.split('/')[0],re.IGNORECASE)) and  not (re.search("content",fff1.split('/')[1],re.IGNORECASE))):
          folder_zip = True
       
       elif ((re.search(app_name,fff1.split('/')[0],re.IGNORECASE)) and  (re.search("content",fff1.split('/')[1],re.IGNORECASE))):
          folder_2_zip = True 
          folder_zip = False
       else:
          folder_zip = False
          folder_2_zip = False
          break 
		  
  zz.close() 
  if (folder_zip and not folder_2_zip):
      path_name_11="D:\\opt\\x_webroot\\"+ app_name + "\\"
      src_path="D:\\opt\\temp\\"+app_name+"\\"
	  #shutil.make_archive(test1234.zip, 'zip', "D:\\opt\\tedir_name)
      #shutil.make_archive("D:\\opt\temp2\\test1234.tar",'tar',"D:\\opt\\temp\\",app_name,)
  elif ( folder_2_zip and not folder_zip):
      path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
      src_path="d:\\opt\\temp\\"+app_name+"\\"+"content"+"\\"
  else :
      path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
      src_path="d:\\opt\\temp\\"
	  
      #shutil.make_archive("D:\\opt\temp2\\test1234.tar",'tar',"D:\\opt\\temp\\",".",)
  #print (folder_zip)
  dg_count=79
  #Mywin_xx.gauge.SetValue(30)
  copyTree1(src_path,path_name_11)
  # here need remove every thing in /opt/temp and /opt/temp2
  # clean folder was commented out 
  clean_folder("d:\\opt\\temp\\")
	 #shutil.copytree(src_path, path_name_11)
	 
    #zz.extractall(path_name_11)
    #zz.close()
############## unzip a file ot detination######################	  
################################################################

####################################################################
def extract_file_to_app(ffile_name):
    global keepGoing
    app_name1=get_app_string(ffile_name)
    destination_path="D:\\opt\\x_webroot\\"
	#destination_path="D:\\opt\\x_webroot\\"+app_name1+"||"
    if (ffile_name.endswith(".tar")) or (ffile_name.endswith(".tar.gz")) :
        #os.chdir(destination_path), this was inside "untar"
        untar(ffile_name)
    elif (ffile_name.endswith(".zip")) or (ffile_name.endswith(".ZIP")) :
	    unzip_1(ffile_name)
    else:
        print (" do noting , not a proper file")
    keepGoing=False
################################################################################################
##############################need by WX##################################################
def onButton(event):
    print ("Button pressed.")	    
######################################################################
#######################################################################
#os.chdir("D:\\staging\\")

#ff_1 = tkinter.filedialog.askopenfilename()

#############################################################################
###########################################################################
##############################################################################
# logging system were added here for better operation#########################

class StreamToLogger(object):
   
   #Fake file-like stream object that redirects writes to a logger instance.
   
   def __init__(self, logger, log_level=logging.INFO):
      self.logger = logger
      self.log_level = log_level
      self.linebuf = ''

   def write(self, buf):
      for line in buf.rstrip().splitlines():
         self.logger.log(self.log_level, line.rstrip())
today1=datetime.datetime.now().strftime("%Y-%m-%d")
out_file_name="D:\\opt\\CIHS_Admin\\logs\\"+"\\out"+today1
logging.basicConfig(
   level=logging.DEBUG,
   format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
   filename=out_file_name,
   filemode='a'
)


###############################################################################
class Logger(object):
    today1=datetime.datetime.now().strftime("%Y-%m-%d")
    #out_file_name="D:\\opt\\CIHS_Admin\\logs\\"++"out"+today1
	#out_file_name="D:\\opt\\CIHS_Admin\\logs\\"+app_name1+"\\out"+today1
    def __init__(self,app_name_01):
        out_file_name="D:\\opt\\CIHS_Admin\\logs\\"+app_name_01+"\\out"+today1
        self.terminal = sys.stdout
        self.log = open(out_file_name, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
##########################################################################################################################
class Mywin_xx(wx.Frame):
   global src_staging
   global ff_1
   global dg_count
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
      self.btn1 = wx.Button(pnl, label="Select a Zip or tar,tar.gz")
      self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn1)
      hbox1.Add(self.text, proportion=1, flag=wx.ALIGN_CENTRE)
      hbox2.Add(self.btn1, proportion=1, flag=wx.RIGHT, border=10)
      vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)
      vbox.Add(hbox1, proportion=1,flag=wx.EXPAND|wx.ALIGN_CENTRE)
      self.gauge = wx.Gauge(pnl, range=80,pos=(20,190),size=(338, 20), style = wx.GA_HORIZONTAL)
      hbox1.Add(self.gauge, proportion=5, flag=wx.ALIGN_CENTRE, border=10)
      pnl.SetSizer(vbox)
      self.Centre()
      self.Show(True)
	  # create a pubsub receiver
      pub.subscribe(self.updateGauge, "update")
   def OnClick(self, event1):
     global ff_1
     self.text.SetValue(" extracting going , please waiting") 
     wildcard="zip and tar(gz) file |*.zip;*.ZIP;*.tar.gz;*.tar"
     dlg = wx.FileDialog(self, "Choose a file", src_staging, "", wildcard,wx.FD_OPEN)
     #self.text.SetValue(" extracting going , please waiting") 
     if dlg.ShowModal() == wx.ID_OK:
        ff_1 = dlg.GetPath()
        self.gauge.SetValue(0)
        if ((ff_1.split(':')[0].upper() != "D") or (ff_1.split('\\')[1].lower() != "staging")):
           print (ff_1.split(':')[0].upper())
           print (ff_1.split('/')[1].lower())
           print (" wrong files were selected , exit ")
           sys.exit (0)
		   
        app_name_1=get_app_string(ff_1)
        put_string = ff_1 + " is being extracting to webroot, please waiting , Thanks " 
        self.text.SetValue(put_string)
        print (app_name_1)
        
        self.text.SetValue(app_name_1)
        sys.stdout = Logger(app_name_1)
        sys.stderr = Logger(app_name_1)
        TestThread()
        put_string = ff_1 + " extracted to webroot, please verify  Thanks " 
        self.text.SetValue(put_string)
        TestThread()
		
        extract_file_to_app(ff_1)
	
        #if self.count <= 95:
        # self.count += 2
        self.gauge.SetValue(dg_count) 
        #self.text.SetValue(ff_1)
     dlg.Destroy
   def updateGauge(self, msg):
        
        #if self.count <= 23:
        self.count += 5
 
        if self.count >= 20:
            self.gauge.SetValue(80)
 
        #self.progress.SetValue(self.count)
        self.gauge.SetValue(self.count)
		
   
	 
############################################################################
########### class definition#######################################

########################################################################
############# new gauger definition#######################
class TestThread(Thread):
    """Test Worker Thread Class."""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.start()    # start the thread
 
    #----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        for i in range(15):
            time.sleep(0.5)
            wx.CallAfter(pub.sendMessage, "update", msg="")
 
########################################################################
class MyProgressDialog(wx.Dialog):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Progress")
        self.count = 0
 
        self.progress = wx.Gauge(self, range=20)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.progress, 0, wx.EXPAND)
        self.SetSizer(sizer)
 
        # create a pubsub receiver
        pub.subscribe(self.updateProgress, "update")
 
    #----------------------------------------------------------------------
    def updateProgress(self, msg):
        """"""
        self.count += 1
 
        if self.count >= 20:
            self.Destroy()
 
        self.progress.SetValue(self.count)
 
 
########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.btn = btn = wx.Button(panel, label="Start Thread")
        btn.Bind(wx.EVT_BUTTON, self.onButton_1)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def onButton_1(self, event):
        """
        Runs the thread
        """
        btn = event.GetEventObject()
        btn.Disable()
 
        TestThread()
        dlg = MyProgressDialog()
        dlg.ShowModal()
 
        btn.Enable()
 
#----------------------------------------------------------------------


########### class definition#######################################
#######################################################################
#####################  Main loop begin here #########################
ex1 = wx.App()
Mywin_xx(None,'Extracting file ')
#ex1.MainLoop()



print (ff_1)



# changed "/" to "\\" , this is DOS style



#################################################################################

################################################################################
################  change log to different folder here###########################
############    merge 1 and 2 #################
#sys.stdout = Logger(app_name_1)
#sys.stderr = Logger(app_name_1)
############# Merge std out and err ##########################

#################################################################################
#################################################################################
## progress bar here############################################################
#app1 = wx.PySimpleApp() 


#extract_file_to_app(ff_1)




# big Loop end here 
ex1.MainLoop()

####################################
####################################################################################
# all below are testing , no need 
