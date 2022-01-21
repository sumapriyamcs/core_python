'''

# P63. REQ : remove leading zeros from an IP address
"""
1. CRUD       -->  delete
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  =    | for
"""

# 0. Mathematics
"""
ip = "216.08.094.196"

o/p  "216.8.94.196"

"""
Ste1: Input the IP address.
Ste2. Splits the ip by ".".
Ste3: Then convert the string to an integer we can use int (parameter) function.
Ste4: Removes the leading zeroes.
Ste5: Then convert it back to string by str (parameter) and then join them back by using join function.

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

ip = "100.020.003.400"
print ('.'.join(str(int(part)) for part in ip.split('.')))

import ipaddress
print(str(ipaddress.ip_address("127.000.000.1")))

# 2. Algorithm

print("--------2 Algorithm              ----------")
ip = "0216.08.094.01960"
print("IP Address :", ip)
new_ip = ".".join([str(int(i)) for i in ip.split(".")])
print("IP Address without leading zero : ", new_ip)

#2nd method:

import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)


# Python program to remove leading zeros an IP address and print #the IP
# function to remove leading zeros
def IP(ip):
   zeroip = ".".join([str(int(i)) for i in ip.split(".")])
   return zeroip ;
   # Driver code
   ip =input("Enter the IP address ::>")
print("New Ip Address ::>",IP(ip))
'''
