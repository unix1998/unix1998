import datetime
import zipfile
import glob 
import os
#list1 = os.listdir("C:\\work_src\\zip_src\\")
list2=glob.glob("D:\\staging\\*.zip")
#print (list1)
print (list2)
print ( " test here ")
aa=1
for zz1 in list2:
   print (zz1)
   with zipfile.ZipFile(zz1, "r") as zz:
      zz.extractall("D:\\opt\\x_webroot")
   aa +=1

#zz=zipfile.ZipFile("D:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip","r")
#for ff in zz.namelist():
#    print (ff)
#for zz in list2:
  
#with zipfile.ZipFile("C:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip", "r") as z:
#    z.extractall("D:\\work_dest\\doc_root")