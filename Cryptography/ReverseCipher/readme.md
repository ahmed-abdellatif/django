# Python Cryptography: The Reverse Cipher
# Running Python Programs (on mac)
## Mac Users
It's probably best to use venv instead of virtualenv if you are running using Python 3. 
On OSX, two different types of Python Builds exist:
a regular build and a framework build. In order to interact correctly with OSX through some GUI frameworks you need a framework build of Python. At the time of writing the macosx, WX and WXAgg backends require a framework build to function correctly. Unfortunately virtualenv creates a non framework build even if created from a framework build of Python
  [Reference](https://matplotlib.org/1.5.3/faq/virtualenv_faq.html)
## Installing venv 
1. <code>python -m venv my-virtualenv</code>
2. <code>source my-virtualenv/bin/activate</code></code>
## creating virtual environment venv 
<code>python3 -m virtualenv env</code>
## Activating virtual environment 
<code>source env/bin/activate</code>