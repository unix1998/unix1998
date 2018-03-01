import datetime
import zipfile
import tarfile 
import glob 
import os
import gzip,binascii
import shutil
import string
import io
def un_gz(file_name):  
    f_name = file_name.replace(".gz", "")  
    # f_name is gunzip file name
    f_in = gzip.open(file_name, 'rb')
    f_out = open(f_name, 'wb')
    file_content = f_in.read()
    f_out.close()  
    f_in.close()  
def un_gz_1(file_name):
  print (file_name)
  f = gzip.open('file_name', 'rb')  
  file_content = f.read()  
  f_out.write(file_content) 
  f.close()  
def copy_from_to(src1, dest1):
#copy file from src1 to dest1
    for filename in glob.glob(os.path.join(src1, '*.gz')):
          shutil.copy(filename, dest1)

def un_gz_folder(folder_1):  
     for filename1 in glob.glob(os.path.join(folder_1, '*.gz')):
        print (filename1)
        un_gz(filename1)

#un_gz('C:\\work_dest\\gzip_root_1\\perl_src.tar.gz')
# begin here 
# copy to doc_root
copy_from_to("C:\\work_src\\gzip_src","C:\\work_dest\\gzip_root_1")
# ungz_them
un_gz_folder("C:\\work_dest\\gzip_root_1")

print ( " test here ")

