import time
import os
import requests
import json
import sys

# Edit the follow line to set your API key.
API_KEY = "<apikey>"

# DO NOT EDIT BELOW THIS LINE
POD = "http://%s.avapi.co/" % API_KEY.split("-")[0]

print " - Fetching Token"
response = requests.post("%sv1/token" % POD, data=json.dumps({'api_key':API_KEY}), verify=False)
response = json.loads(response.text)
token = response['token']

print " - Checking Hash"
hash = os.popen("sha512sum '%s' | awk {'print $1'}" % sys.argv[1]).read().rstrip()
response = requests.get("%sv1/file/%s" % (POD, hash), headers={'X-Auth-Token':token})

if response.status_code == 200:
    response = json.loads(response.text)
    if response['result'] == "clean":
        print " *** %s is safe" % sys.argv[1]
    else:
        print " *** %s is infected: %s" % (sys.argv[1], response['malware_name'])
elif response.status_code == 404:
    print "*** No intelligence about file, submitting for analysis ***"
    os.popen("curl -X POST -H 'X-Auth-Token: %s' -H 'Content-Type: multipart/form-data' -F 'data=@%s' %sv1/file/new" % (token, sys.argv[1], POD)).read()
    lookup = True
    while (lookup):
        response = requests.get("%sv1/file/%s" % (POD, hash), headers={'X-Auth-Token':token})
        if response.status_code == 200:
            response = json.loads(response.text)
            if response['result'] == "clean":
                print " *** %s is safe" % sys.argv[1]
            else:
                print " *** %s is infected: %s" % (sys.argv[1], response['malware_name'])
            lookup = False
        elif response.status_code == 404:
            print " -  Waiting for scan result"
        else:
            print " - Something went wrong, exiting"
            lookup = False
        time.sleep(2)

else:
    print " - Something went wrong, exiting"

