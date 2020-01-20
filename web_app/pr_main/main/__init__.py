"""
    AUTHOR: Sutharsan Rajaratnam
    DATE: December 16, 2020
    APPLICATION: Payroll Web Application
    PURPOSE: 
    NOTE: 

    FILE: payroll/main/__init__.py

"""

from flask import Blueprint

#Define blueprint
blueprint_main   = Blueprint('main', __name__, url_prefix='/main',
                            template_folder='templates',
                            static_folder='static')

from . import views