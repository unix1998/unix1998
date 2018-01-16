import datetime
import zipfile
import tarfile 
import glob 
import os
import gzip,binascii
import shutil
import string
import io
def untar(ffname):
    if (ffname.endswith(".tar")) or (ffname.endswith(".tar.gz")) :
        print (ffname)
        tar=tarfile.open(ffname)
        for tarinfo in tar:
             print (tarinfo.name)
        tar.extractall()
        tar.close()
        print ("Extracted in Current Directory")
    else:
        print ("Not a tar.gz file:") 

def untar2(ffname):
       tar=tarfile.open(ffname)
        
       tar.extractall()
       tar.close()

def untar_folder(folder_22):
    for filename2 in glob.glob(os.path.join(folder_22, '*.tar')):
        print (filename2)
        untar(filename2)
def make_tarfile(source_dir):
    output_filename=os.path.basename(source_dir)+".tar.gz"
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

#os.chdir("C:/path/to/location")
make_tarfile("D:\\opt\\python_src\\test")

# untar_them
#untar_folder("C:\\work_dest\\gzip_root_1")
#untar("C:\\work_dest\\gzip_root_1\\yaml.tar.gz")
#untar2("C:\\work_dest\\gzip_root_1\\yaml.tar.gz")
#untar("C:\work_src\gzip_src\perl_src.tar.gz")
print ( "test here ")

