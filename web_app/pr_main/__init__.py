# payroll/web_app/__init__.py

from flask import Flask
#from .api import api

#from . import api as api
#import api.api as api


#from config module import global config file import app
#from .config.conf import app
from .config import conf

app = conf.app

#Import application Blueprints 
from .api import blueprint_api as bp_api
from .admin import blueprint_admin as bp_admin
from .main import blueprint_main as bp_main


"""
To use a blueprint, 
    1. Define Blueprint locally.
        - Define bluerint locally in '<app-name>.<blueprint-folder>.__init__.py' file
    2. Register the blueprint on the application.
        i.) Register this blueprint to project package's top-level '__init__.py' file 
            - Add relevant script to '<app-name>.__init__.py' file
        ii.) Make sure that the routes are registered on the blueprint now rather than the app object.
            - Add script to '<app-name>.views.py' file
            - Add script to '<app-name>.<blueprint-folder>.views.py' file

"""

# Puts the API blueprint on api.<domain-name>.com.
#app.register_blueprint(api, subdomain='api')

#print app.config['MYSQL_USER']
#print api.k


#Register application Blueprints
app.register_blueprint(bp_admin)
app.register_blueprint(bp_main)
app.register_blueprint(bp_api)

