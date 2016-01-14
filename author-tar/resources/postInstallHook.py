import pycurl
import os
from urllib import urlencode, quote

#
# Script is used to set the replication URI.

#
baseUrl="http://localhost:4502"
password="admin:admin"

#Update Replication Agent
c = pycurl.Curl()
c.setopt(c.URL, baseUrl + "/etc/replication/agents.author/publish/jcr:content")
c.setopt(pycurl.USERPWD, password)
#postfields = ".%2Fsling%3AresourceType=cq%2Freplication%2Fcomponents%2Fagent&.%2Fjcr%3AlastModified=&.%2Fjcr%3AlastModifiedBy=&_charset_=utf-8&%3Astatus=browser&.%2Fjcr%3Atitle=Default%20Agent&.%2Fjcr%3Adescription=Agent%20that%20replicates%20to%20the%20default%20publish%20instance.&.%2Fenabled=true&.%2Fenabled%40Delete=&.%2FserializationType=durbo&.%2FretryDelay=60000&.%2FuserId=&.%2FlogLevel=info&.%2FreverseReplication%40Delete=&.%2FtransportUri=http%3A%2F%2Fpublish%3A4503%2Fbin%2Freceive%3Fsling%3AauthRequestLogin%3D1&.%2FtransportUser=admin&.%2FtransportPassword=admin&.%2FtransportNTLMDomain=&.%2FtransportNTLMHost=&.%2Fssl=&.%2FprotocolHTTPExpired%40Delete=&.%2FproxyHost=&.%2FproxyPort=&.%2FproxyUser=&.%2FproxyPassword=&.%2FproxyNTLMDomain=&.%2FproxyNTLMHost=&.%2FprotocolInterface=&.%2FprotocolHTTPMethod=&.%2FprotocolHTTPHeaders%40Delete=&.%2FprotocolHTTPConnectionClose%40Delete=true&.%2FprotocolConnectTimeout=&.%2FprotocolSocketTimeout=&.%2FprotocolVersion=&.%2FtriggerSpecific%40Delete=&.%2FtriggerModified%40Delete=&.%2FtriggerDistribute%40Delete=&.%2FtriggerOnOffTime%40Delete=&.%2FtriggerReceive%40Delete=&.%2FnoStatusUpdate%40Delete=&.%2FnoVersioning%40Delete=&.%2FqueueBatchMode%40Delete=&.%2FqueueBatchWaitTime=&.%2FqueueBatchMaxSize="
post_data = {"./sling:resourceType":"cq/replication/components/agent","./jcr:lastModified":"","./jcr:lastModifiedBy":"","_charset_":"utf-8",":status":"browser","./jcr:title":"Default Agent","./jcr:description":"Agent that replicates to the default publish instance.","./enabled":"true","./enabled@Delete":"","./serializationType":"durbo","./retryDelay":"60000","./userId":"","./logLevel":"info","./reverseReplication@Delete":"","./transportUri":"http://publish:4503/bin/receive?sling:authRequestLogin=1","./transportUser":"admin","./transportPassword":"admin","./transportNTLMDomain":"","./transportNTLMHost":"","./ssl":"","./protocolHTTPExpired@Delete":"","./proxyHost":"","./proxyPort":"","./proxyUser":"","./proxyPassword":"","./proxyNTLMDomain":"","./proxyNTLMHost":"","./protocolInterface":"","./protocolHTTPMethod":"","./protocolHTTPHeaders@Delete":"","./protocolHTTPConnectionClose@Delete":"true","./protocolConnectTimeout":"","./protocolSocketTimeout":"","./protocolVersion":"","./triggerSpecific@Delete":"","./triggerModified@Delete":"","./triggerDistribute@Delete":"","./triggerOnOffTime@Delete":"","./triggerReceive@Delete":"","./noStatusUpdate@Delete":"","./noVersioning@Delete":"","./queueBatchMode@Delete":"","./queueBatchWaitTime":"","./queueBatchMaxSize":""}
# Form data must be provided already urlencoded.
postfields = urlencode(post_data)
# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
c.setopt(c.POSTFIELDS, postfields)
c.perform()

print "Checking Agent"

#Print Publisher status
c = pycurl.Curl()
c.setopt(c.URL, baseUrl + "/etc/replication/agents.author/publish/jcr:content.json")
c.setopt(pycurl.USERPWD, password)
c.perform()

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



