import datetime
import zipfile
import os
#import glob 
path1='C:\\work_src\\zip_src\\*.zip'
list1=os.listdir("C:\\work_src\\zip_src\\")
print (list1)

print ( " test here ")
for zz1 in list1:
   print (zz1)

#zz=zipfile.ZipFile("C:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip","r")
#for ff in zz.namelist():
#    print (ff)

#with zipfile.ZipFile("C:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip", "r") as z:
#    z.extractall("C:\\work_dest\\doc_root")