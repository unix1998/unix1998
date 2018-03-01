import datetime
import zipfile
import tarfile
import glob 
import os
import re
import sys
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
############## unzip a file ot detination######################
def unzip_1(zip_f):
  print(zip_f)
  app_name=get_app_string(zip_f)
  path_name_11="D:\\opt\\x_webroot\\"
  #path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
  folder_zip=False
  with zipfile.ZipFile(zip_f, "r") as zz:
    for fff1 in zz.namelist():
       print (fff1)
       if re.search(app_name,fff1.split('/')[0],re.IGNORECASE):
          folder_zip = True
       else:
          folder_zip = False
          break
	  
    if folder_zip:
      path_name_11="D:\\opt\\x_webroot\\" 
    else:
      path_name_11="D:\\opt\\x_webroot\\" + app_name + "\\"
    print (folder_zip)
    zz.extractall(path_name_11)
    zz.close()
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

#os.chdir("D:\\staging\\")
#listTo_list("D:\\staging\\")
#print (os.listdir("d:\\staging\\"))
#print (glob.glob("d:/staging/*"))
#root = tkinter.Tk()
#filez = tkinter.filedialog.askopenfilenames(parent=root,title='Choose a file')
#print (root.tk.splitlist(filez))
#for ff1 in filez:
 #  print (ff1)
 
exit(0)

ff_1 = tkinter.filedialog.askopenfilename()
print (ff_1)
if ((ff_1.split(':')[0].upper() != "D") or (ff_1.split('/')[1].lower() != "staging")):
   print (ff_1.split(':')[0].upper())
   print (ff_1.split('/')[1].lower())
   print (" wrong files were selected , exit ")
   exit (0)

app_name_1=get_app_string(ff_1)
print (app_name_1)

#  real work
extract_file_to_app(ff_1)
# 
# real work here
# done here 

print

exit (0)
# all below are testing , no need 
#list1 = os.listdir("D:\\work_src\\zip_src\\")
list2=glob.glob("D:\\staging\\*.zip")
#print (list1)
print (list2)
print ( " test here ")
aa=1
for zz1 in list2:
   print (zz1)
   #with zipfile.ZipFile(zz1, "r") as zz:
      #zz.extractall("D:\\opt\\x_webroot")
   aa +=1

#zz=zipfile.ZipFile("D:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip","r")
#for ff in zz.namelist():
#    print (ff)
#for zz in list2:
  
#with zipfile.ZipFile("C:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip", "r") as z:
#    z.extractall("D:\\work_dest\\doc_root")