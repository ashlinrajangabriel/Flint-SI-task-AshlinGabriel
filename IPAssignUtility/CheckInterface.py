#!/usr/bin/python
# -*- coding: utf-8 -*-
import psutil
import re
import ipaddress
import os
from random import randint, randrange
import socket
import fcntl
import struct
import netifaces as ni


_addrs = psutil.net_if_addrs()
_Interfaces = list(_addrs.keys()) #Get all Interface address as dictionary keys
REGEX_InterfaceFilter = re.compile(r"[a-zA-Z]+[0-9]+-") #Regular expression filters the Interface by 
_Interfaces = list(filter(REGEX_InterfaceFilter.search, _Interfaces)) #Allocate the filtered value of the list in the same list


def GenerateIp(_Interfaces):

    l_ip_addr = [str(ip) for ip in ipaddress.IPv4Network("192.168.1.0/24")] #Have chosen ipclass C
    return l_ip_addr[2 : len(_Interfaces) + 2] #Skipping the first two items of the list(Gateway and .0)

#End of Generate IP Function

def AllocateInterfaces(_Interfaces):

    if _Interfaces:  #Checking if the Interfaces is not empty or missing
        
        l_IP = GenerateIp(_Interfaces) #Function call to generate the IP
        for i in range(len(l_IP)): #Looping with range of IP or this could be interface length too

            _IpString = "sudo ip addr add {}/24 brd + dev {}".format(
                l_IP[i], _Interfaces[i], _Interfaces[i]
            ) #preparing the linux command to configure the IP
            os.system(_IpString) #Executing the command with OS library
           
            print(
                _Interfaces[i],
                "IP address is ",
                ni.ifaddresses(_Interfaces[i])[ni.AF_INET][0]["addr"],
            ) #Just printing values

    else:

        l_Interfaces = ["ens160-A", "ens160-B", "ens160-C"] #Defining missing interfaces as mock
        for Interface in l_Interfaces:
            _linkadd = "sudo ip link add {} type dummy".format(str(Interface))
            _Macadd = "sudo ifconfig {} hw ether {}:{}:{}:ff:ff:ff".format(
                Interface, (randint(11, 99)), (randint(50, 85)), (randint(25, 53))
            ) #creating interfaces and Mac address

            os.system(_linkadd) #execution of commands
            os.system(_Macadd)
            addrs = psutil.net_if_addrs()
            REGEX_InterfaceFilter = re.compile(r"[a-zA-Z]+[0-9]+-")
            _Interfaces = list(filter(REGEX_InterfaceFilter.search, _Interfaces))
 
        print("Your interfaces are now  created and configured")
        AllocateInterfaces(l_Interfaces)    #Calling the allocation function to assign IP 

        

def main():
  AllocateInterfaces(_Interfaces)
 

main()

