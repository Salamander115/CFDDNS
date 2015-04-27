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

When you have completed that, If you haven't already, you will need to [install texttables](https://pypi.python.org/pypi/texttable) which can also be done using the command: `pip install texttable`.

Now all you have to do is run the program, and enjoy your new DDNS.


===========

Future plans:
- Implement an error handling system  -- High Priority
- Add support for sub-domains (CNAME's)  -- High Priority 
- Improve speed, by reducing amount of requests made -- Medium Priority
- Compress script by reducing repeated code  -- Low Priority
- Add more options, and functions -- Just Sorta Happens
- One day, make a GUI version (User interface) -- I need to learn some more stuff first.
- Remove `texttables.py` Dependency -- Medium-High-Priority
- Add to PyPI and allow PIP install
