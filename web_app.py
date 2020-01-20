"""
    AUTHOR: Sutharsan Rajaratnam
    DATE: January 18, 2020
    APPLICATION: Payroll Web Application
    FILE: payroll/web_app.py
    PURPOSE: The main application file to run the "Payroll Report" web application
    
    NOTE: Explicitly excluded using 'SQLAlchemy' (Python SQLtoolkit & ORM), wanted to maintain non-Python universal readability. 
"""

"""
Import relevant custom modules
"""

#METHOD-01: Direct absolute import of global configuration file (does not rely on '__init__.py' of 'config' module, basically bypass '__init__.py')
#from web_app.config.config import app

#METHOD-02: Module import approach to importing relevant configuration files (relies on '__init__.py' of 'config' module, simpler to rename modules).  
#Import global configurations defined in 'config.py' from module 'config'
from web_app.config import conf

#Get flask 'app' instance
app = conf.app



from flask import Flask, flash, render_template, request, redirect



#ROUTE: Rerouting to '/main' as default (ie.'homepage') for the web application
#@app.route("/")
@app.route("/")
def home():
     return redirect('/main')

#Global 'payroll' application instantiation 
app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)