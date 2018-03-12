#!/usr/bin/python
import csv
import re
import sys
def get_para():
  if not (len(sys.argv) == 2 ) :
    print " This script need a file input"

    print "Usage: " +  sys.argv[0]+ " file" 
    sys.exit(0)
    #return

def from_csv_to_yaml(file):
 with open(file, 'rb') as csvfile:
    freader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    # Creates the output file named fixture.yaml
    f = open('new.yaml', 'w')
    f.write("---\n")
    f.write("Server:\n")
    for i, row in enumerate(freader):
        #print (i)
        #print (row)
        csv_content = ' '.join(row)
        #print (csv_content)
        if ( i>0) and (len(csv_content.split(',')[0]) >0 ) and (len(csv_content.split(',')[1]) >0 ):
          print i
          print csv_content.split(',')[0]
          src_server=csv_content.split(',')[0]
          dest_server=csv_content.split(',')[1]
          the_port=csv_content.split(',')[2] 
          f.write(' - Server1: %s\n' % src_server)
          f.write('   Server2: %s\n' % dest_server)
          f.write('   port: %s\n' % the_port)
        elif (len(csv_content.split(',')[0]) == 0 )and (len(csv_content.split(',')[1]) >0 ):
          print (csv_content.split(',')[1])
          #print ("AAAAAAAAAAAAA")    
          dest_server=csv_content.split(',')[1]
          the_port=csv_content.split(',')[2]
          f.write(' - Server1: %s\n' % src_server)
          f.write('   Server2: %s\n' % dest_server)
          f.write('   port: %s\n' % the_port)

          #f.write('        - %s\n' % csv_content.split(',')[2])
          #first_server=csv_content.split(',')[1]
        elif ( i >0 ) and (len(csv_content.split(',')[0]) >0 ) and (len(csv_content.split(',')[1])== 0 ):
          print (" this setting is not so well designed , try improve it  \n")
          
           
        #csv_content = ' '.join(row)
        #csv_content = csv_content.split(',')
        #f.write('p_name.Model_name\n')
        #f.write('  pk: %d\n' % i)
        #f.write('  fields:\n')
        #f.write('    field_1: %s\n' % csv_content[0])
        #f.write('    field_2: %s\n' % csv_content[1])
        #f.write('    field_3: %s\n' % csv_content[2])
    f.close()
get_para()
from_csv_to_yaml(sys.argv[1])
#from_csv_to_yaml('./data1.csv')
