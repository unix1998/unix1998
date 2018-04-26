#! /usr/local/bin/python3
import os
import sys
import socket

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # this is check ipv4
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # test for IP v4
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # ipv6
        return False
    return True

with open("./input_file.txt") as f:
    for line1 in f:
        #print (line)
        #addr="'"+line+"'"
        #print (addr) 
        line=line1.rstrip()  
        a_ipv4=is_valid_ipv4_address(line)
        a_ipv6=is_valid_ipv6_address(line)
        if a_ipv4: 
          print (line+" is ipv4")
        elif a_ipv6:
          print (line+" is ipv6")
        else:
          print (line+" is not ipv6 , not ipv4")
