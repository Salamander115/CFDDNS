from requests import get     # Used to get the current Ext IP
from requests import post    # Used for CF API
import texttable as tt       # Nicely formatted output
import time, json, urllib    # General modules

cls = lambda: print("\n"*50) # Used to "Clear" sreen

###########  GLOBAL VARS  ###########

global badUrls

cfURL = 'https://www.cloudflare.com/api_json.html'
cfTKN = ''                        # Get your token from   https://www.cloudflare.com/my-account.html
email = ''                        # The E-Mail used to access your Cloudflare account
URLs = ['abc.com', 'example.com'] # A list of the URLs that you want included in the DDNS, They must be asscosciated with your account
updateInterval = 10               # How many seconds between each check for new IP
badUrls = 0                       # Just initiates a Variable to be used later

##########  VAR FUNCTIONS  ##########

def echo(x):  # I am used to PHP's echo function, so I use this to feel more familiar
    print(x)

def wait(x):
    time.sleep(x)

def getCurrentIP():
    return get('http://api.ipify.org').text

def A_Record(url):
    params = {'a': 'rec_load_all',
              'tkn': cfTKN,
              'email': email,
              'z': url
              }
    query = post(cfURL,params)
    data = json.loads(query.content.decode('utf-8'))
    a = data['response']['recs']['objs'][0]
    return a

def getAID(url):
    return  A_Record(url)['rec_id']

def checkDNS(url):
    correctIP = getCurrentIP()
    setIP = A_Record(url)['content']
    if correctIP == setIP:
        return True
    else:
        return False

def changeDNS(url, newIP=getCurrentIP()):
    aid = getAID(url)
    p = {'a': 'rec_edit',
         'tkn': cfTKN,
         'id': aid,
         'email': email,
         'z': url,
         'type': 'A',
         'name': url,
         'content': newIP,
         'service_mode': '1',
         'ttl': '1'
         }
    q = post(cfURL, p)
    data = json.loads(q.content.decode('utf-8'))
    return data

def main():
    cls()
    echo("Gathering DNS information from CloudFlare\n\nPlease Wait...")
    
    while True:
        
        res = [ ['URL', 'RESULT', 'IP'] ]
        table = tt.Texttable()
        table.set_cols_align(['c','l','c'])
        table.set_cols_valign(['m','m','m'])
        
        for x in URLs:
            if checkDNS(x) != True:
                res += [ [x, 'Incorrectly Configured', A_Record(x)['content']] ]
                changeDNS(x)
                wait(2)
            else:
                res += [ [x, 'Correctly Configured', A_Record(x)['content']] ]
                
        table.add_rows(res)
        cls()
        print(table.draw())
        
        wait(updateInterval)

def startup():
    cls()
    
    note  = 'Thanks for downloading CFDDNS \u00a9, \n'
    note += 'This project is in alpha stages, and so '
    note += 'may contain bugs. \nPlease notify me of '
    note += 'bugs and errors via \'mick2000@sky.com\''
    echo(note)
    
    x = input('\n\nPress enter to continue  ->')
    
    main()

startup()    # To start the service immediately, replace this 'startup()', with 'main()'   (Without quotes)
