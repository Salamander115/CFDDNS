# CFDDNS  (v0.2)
Cloudflare Dynamic DNS

To start using CFDDNS, simply download CFDDNS.py and edit the `Global Vars` as follows:

```Python
cfURL = 'https://www.cloudflare.com/api_json.html'  # No need to change this
cfTKN = 'abcdefghijklmnopqrstuvwxyz1234567890'      # Get this from  https://www.cloudflare.com/my-account.html
email = 'Youremail@website.tld'                     # The e-mail assosciated with your account, double check at https://www.cloudflare.com/my-account.html
URLs = []                                           # List of domains that should be included in the Dynamic updates, These should be connected to your account. In a future update, I will add an option to update all URL's at once
updateInterval = 10                                 # In seconds, the amount of time between each update, suggested to keep above 5
```

When you have completed that, simply run the application, and watch the magic begin.


===========

Future plans:
- Add support for sub-domains (CNAME's)
- Improve speed, by reducing amount of requests made
- Compress script by reducing repeated code
- Add more options, and functions
- One day, make a GUI version (User interface)
