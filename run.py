import sys
import urllib2
import json
import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ip = sys.argv[1]
response = json.loads(urllib2.urlopen('http://ip-api.com/json/' + ip).read())


print """ 

 _                    _   _               ____          ___ ____  
| |    ___   ___ __ _| |_(_) ___  _ __   | __ ) _   _  |_ _|  _ \ 
| |   / _ \ / __/ _` | __| |/ _ \| '_ \  |  _ \| | | |  | || |_) |
| |__| (_) | (_| (_| | |_| | (_) | | | | | |_) | |_| |  | ||  __/ 
|_____\___/ \___\__,_|\__|_|\___/|_| |_| |____/ \__, | |___|_|    
                                                |___/             
 ____           ____ _____       _     _____ _ 
| __ ) _   _   / ___|___ / _ __ | |__ |___ /(_)
|  _ \| | | | | |     |_ \| '_ \| '_ \  |_ \| |
| |_) | |_| | | |___ ___) | |_) | | | |___) | |
|____/ \__, |  \____|____/| .__/|_| |_|____/|_|
       |___/              |_|                  

_____________________________________________________________________
"""


print bcolors.OKGREEN + "AS: " + bcolors.ENDC + response['as']
print bcolors.OKGREEN + "City: " + bcolors.ENDC  + response['city']
print bcolors.OKGREEN + "Country: " + bcolors.ENDC + response['country']
print bcolors.OKGREEN + "Country Code: " + bcolors.ENDC + response['countryCode']
print bcolors.OKGREEN + "ISP: " + bcolors.ENDC + response['isp']
print bcolors.OKGREEN + "Latitude: " + bcolors.ENDC + str(response['lat'])
print bcolors.OKGREEN + "Longitude: " + bcolors.ENDC + str(response['lon'])
print bcolors.OKGREEN + "Organisation (Provider): " + bcolors.ENDC + response['org']
print bcolors.OKGREEN + "Region Code: " + bcolors.ENDC + response['region']
print bcolors.OKGREEN + "Region Name: " + bcolors.ENDC + response['regionName']
print bcolors.OKGREEN + "Timezone: " + bcolors.ENDC + response['timezone']
print bcolors.OKGREEN + "ZIP: " + bcolors.ENDC + str(response['zip'])
print bcolors.OKGREEN + "Status: " + bcolors.ENDC + response['status']
print bcolors.OKGREEN + "Gmap URL:"  + bcolors.ENDC + " https://www.google.com/maps/@" + str(response['lat']) + "," + str(response['lon']) + ",15z \n"


