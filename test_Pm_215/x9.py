import datetime
import zipfile
import glob 
import os
import sys
#list1=glob.glob("C:\\work_src\\zip_src\\*.zip")
#print (list1)
#list2=os.listdir("c:/work_dest/doc_root1/")
#print (list2)
print ( " test here ")
aa=1
string1=sys.argv[1]
string2=sys.argv[2]
print (string1)
print (string2)
while aa < 4:
   print (aa)
   path_name="C:\\work_dest\\doc_root"+str(aa)+"\\"
   print (path_name)
   #list1=os.listdir(path_name)
   #print (list1)
   aa +=1
