# Python-Visualizations
Data visualizations using python's matplotlib library

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
## Installing pip 
1. <code>curl -O https://bootstrap.pypa.io/get-pip.py</code>
2. <code>python3 get-pip.py</code>
or if you are using python2 
<code>python get-pip.py</code>
## Installing matlib with all dependencies
<code>python3 -mpip install matplotlib</code>
or 
<code>python -mpip install matplotlib</code>
## Matplot Lib & virtual environment errors
1. Navigate to <code>~/.matplotlib.</code>
2. Create a file called <code>~/.matplotlib/matplotlibrc</code>
3. Then add the following inside of that file <code>backend: TkAgg</code>

## Running visual_walk.py
 <code>python ./visual_walk.py</code>
  <br><br>
  <img src="https://github.com/Ahmed760/Python-Visualizations/blob/master/curve.png" width="40%">
## Running Sinusoid example : sinusoid.py
 <code>python ./sinusoid.py</code>
 <br><br>
  <img src="https://github.com/Ahmed760/Python-Visualizations/blob/master/sinusoid.png" width="40%">

 
