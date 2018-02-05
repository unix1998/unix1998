import datetime
import zipfile
import glob 
import os
import sys
def unzip_1(zip_f):
  print(zip_f)
  with zipfile.ZipFile(zip_f, "r") as zz:
      zz.extractall("D:\\opt\\x_webroot")


#list1 = os.listdir("C:\\work_src\\zip_src\\")
list2=glob.glob("D:\\staging\\*.zip")
today1=datetime.datetime.now().strftime("%Y-%m-%d")
print (list2)
print ( " test here ")

aa=1
out_file_name="D:\\opt\\CIHS_Admin\\logs\\"+"out"+today1
error_file_name="D:\\opt\\CIHS_Admin\\logs\\"+"error"+today1
print (out_file_name)
print (error_file_name)
sys.stdout=open(out_file_name,"w")
sys.stderr=open(error_file_name,"w")
for zz1 in list2:
   print (zz1)
   #unzip_1(zz1)

print ("finish , bye")
sys.stdout.close()
sys.stderr.close()
#zz=zipfile.ZipFile("D:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip","r")
#for ff in zz.namelist():
#    print (ff)
#for zz in list2:
  
#with zipfile.ZipFile("C:\work_src\zip_src\heapdump-YYZSRC5001-27804-20161005_113357_Leak_Suspects.zip", "r") as z:
#    z.extractall("D:\\work_dest\\doc_root")
