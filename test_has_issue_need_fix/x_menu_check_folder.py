import datetime
import zipfile
import tarfile
import glob 
import os
import re
import sys
import shutil 
#from tkinter.filedialog import askopenfilename
#import tkinter
#import tkinter.filedialog

################################################################
def get_app_string(full_path_name):
    return  full_path_name.split('\\')[2]
	# the above is for menu version 
############################################################
    #return  full_path_name.split('/')[2]
	# GUI version , need above statement
#################################################################
#####################################################
def clean_folder(folder_name):
 for file_object in os.listdir(folder_name):
    file_object_path = os.path.join(folder_name, file_object)
    if os.path.isfile(file_object_path):
        os.unlink(file_object_path)
    else:
        shutil.rmtree(file_object_path)
		
###########################################################
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
    app_name=get_app_string(ffname)
    path_name_11="D:\\opt\\x_webroot\\"
    folder_zip=False
    if (ffname.endswith(".tar")) or (ffname.endswith(".tar.gz")) :
        print (ffname)
        tar=tarfile.open(ffname)
        for tarinfo in tar:
             print (tarinfo.name)
             aa=tarinfo.name
             if re.search(app_name,aa.split('/')[0],re.IGNORECASE):
                 folder_zip = True
             else:
                 folder_zip = False
                 break
        print (aa)	
        if folder_zip:
             path_name_11="D:\\opt\\x_webroot\\" 
        else:
             path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
        print (folder_zip)
        print (path_name_11)
        os.chdir(path_name_11)
        tar.extractall()
        tar.close()
        print ("Extracted in Current Directory")
    else:
        print ("Not a tar.gz file:") 
		
### extract tar file and tar.gz file #######################		
###############################################################

##############################################################
def unzip_1(zip_f):
  print(zip_f)
  app_name=get_app_string(zip_f)
  path_name_11="D:\\opt\\x_webroot\\"
  #path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
  folder_zip=False
  folder_2_zip=False
  with zipfile.ZipFile(zip_f, "r") as zz:
    for fff1 in zz.namelist():
       print (fff1)
       zz.extractall("D:\\opt\\temp")
       if ((re.search("httpd.ini", fff1,re.IGNORECASE)) or (re.search("web.config", fff1,re.IGNORECASE))):
          print ( " it has httpd.ini and web.conf , removing them  ")
          os.chdir("D:\\opt\\temp")
          os.remove(fff1)
          
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
  print (folder_zip)
  copyTree1(src_path,path_name_11)
  # here need remove every thing in /opt/temp and /opt/temp2
  
  clean_folder("d:\\opt\\temp\\")
	 #shutil.copytree(src_path, path_name_11)
	 
    #zz.extractall(path_name_11)
    #zz.close()
############## unzip a file ot detination######################	  
################################################################
############## unzip a file ot detination######################	  
################################################################

def backup_app(app_name):
    printf ( "app_name")
####################################################################
def extract_file_to_app(ffile_name):
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

def listTo_list(folder_name):
    app_list=os.listdir(folder_name)
    print (app_list)
    a_index=1
	
    print (" Here is list of application name , tell which one need be deployed ")
    for app in app_list:
      print ("["+str(a_index)+"]  :   " + app)
      a_index += 1
    print (" [99]  : Exit ")
    input_number=input  ( " please enter selection [99:]")

def list_archive(app_name1):
  # list all zip/tar file in stage app folder
  this_folder_star="D:\\staging\\"+app_name1+"\\"+"*.*"
  for archive_file in glob.glob(this_folder_star):
    
    print (archive_file)
    #full_path_archive_file=this_folder+archive_file
    #print (full_path_archive_file)
    extract_file_to_app(archive_file)
#def main_loop_1(app_list):
# main loop begin here :
# main loop begin here :
###########################################################################################
app_list=[]
input_number = 299
while True :
  app_list=os.listdir("D:\\staging\\")
  print (app_list)
  a_index=1
	
  print (" Here is list of application name , tell which one need be deployed ")
  for app in app_list:
     print ("["+str(a_index)+"]  :   " + app)
     a_index += 1
  print (" [99][Return]   : Exit ")
  input_number=input  ( " please enter selection [99:]")
  print ("a_index is ")
  print (a_index)
  if input_number == "":       # If it is a blank line...
     break  
  if (int(input_number) >=int(a_index)) or ( int(input_number) < 1 ):
    print (input_number)
    print (" wrong input , input again" )
    continue
  else:
    aapp_name=app_list[int(input_number)-1]
    print (aapp_name)
    print (" begin_working")
    #exit(0)
    list_archive(aapp_name)
########### end of main loop #################################################################
##################################################################################################


 
exit(0)

#  real work
extract_file_to_app(ff_1)
# 
