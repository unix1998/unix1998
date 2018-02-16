import datetime
import zipfile
import tarfile 
import glob 
import os
import gzip 

with open("C:\\work_src\\Logs_src\\Application.evtx", 'rb') as plain_file:  
    with gzip.open("C:\\work_src\\Logs_gzip\\Application.evtx.gzip", 'wb') as zip_file:  
        zip_file.writelines(plain_file)  

#list2=glob.glob("C:\\work_src\\zip_src\\*.zip")
#print (list2)
print ( " test here ")
#aa=1
#for zz1 in list2:
#  print (zz1)
   
#zz=zipfile.ZipFile("C:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip","r")
#for ff in zz.namelist():
#    print (ff)
#for zz in list2:
  
#with zipfile.ZipFile("C:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip", "r") as z:
#    z.extractall("C:\\work_dest\\doc_root")