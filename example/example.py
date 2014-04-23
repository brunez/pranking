#!/usr/bin/env

from __future__ import print_function
import urllib2
import ftplib
import subprocess

msgContent = subprocess.check_output("python ../src/rank.py -t 7 -p", shell=True)

# Write the ranking to a file
print("Writing...")
f = open('rank.txt','w')
print(msgContent, file=f)
f.close();
print("Done Writing")

# Send the file over FTP
print("FTPing...")
server = "www.yourserver.com"
username = "username"
password = "password"
session = ftplib.FTP(server, username, password)
file = open('rank.txt','rb')                  # file to send
session.storbinary('STOR rank.txt', file)     # send the file
file.close()                                  # close file
session.quit()                                # close FTP session
print("Done FTPing")

# Perform an HTTP GET of the php script
print("GETting...")
response = urllib2.urlopen("http://www.yourserver.com/sendmail.php").read()
print(response)
print("Done GETting")
