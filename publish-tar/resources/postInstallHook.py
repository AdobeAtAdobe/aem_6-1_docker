import pycurl
import os
from urllib import urlencode, quote

#
# Script is used to set the replication URI.

#
baseUrl="http://localhost:4503"
password="admin:admin"

packageList = "packagelist.txt"
current_dir = os.getcwd()
print "Current directory " + current_dir
if os.path.isfile(packageList):
    with open(packageList) as fp:
        for package in fp:
            print "Package is: @\"" + current_dir + "/packages/" + package + "\""
            c1 = pycurl.Curl()
            c1.setopt(c1.URL, baseUrl + "/crx/packmgr/service.jsp")
            c1.setopt(c1.POST, 1)
            c1.setopt(pycurl.USERPWD, password)
            file_name = current_dir + "/packages/" + package
            #print file_name
            c1.setopt(c1.HTTPPOST, [('file', (c1.FORM_FILE, file_name)), ('force', 'true'), ('install', 'true')])
            c1.perform()
            print "Installed package " + package
            c1.close();
else:
    print "No package list found"



