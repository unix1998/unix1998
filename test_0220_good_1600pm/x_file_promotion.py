import datetime
import zipfile
import tarfile
import glob 
import os
#from tkinter.filedialog import askopenfilename
import tkinter
import tkinter.filedialog

################################################################
def get_app_string(full_path_name):
    return  full_path_name.split('/')[2]
############################################################

#################################################################
### extract tar file and tar.gz file #######################
def untar(ffname):
    if (ffname.endswith(".tar")) or (ffname.endswith(".tar.gz")) :
        print (ffname)
        tar=tarfile.open(ffname)
        for tarinfo in tar:
             print (tarinfo.name)
        #tar.extractall()
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
  with zipfile.ZipFile(zip_f, "r") as zz:
      #zz.extractall(path_name_11)
	  print ("test1")
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
        os.chdir(destination_path)
        untar(ffile_name)
    elif (ffile_name.endswith(".zip")) or (ffile_name.endswith(".ZIP")) :
	    unzip_1(ffile_name)
    else:
        print (" do noting , not a proper file")

	    

os.chdir("D:\\staging\\")
#root = tkinter.Tk()
#filez = tkinter.filedialog.askopenfilenames(parent=root,title='Choose a file')
#print (root.tk.splitlist(filez))
#for ff1 in filez:
 #  print (ff1)
ff_1 = tkinter.filedialog.askopenfilename()
print (ff_1)
app_name_1=get_app_string(ff_1)
print (app_name_1)
#  real work
extract_file_to_app(ff_1)
# 
# real work here
# done here 

print

exit (0)

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