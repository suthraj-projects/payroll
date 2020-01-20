"""
    AUTHOR: Sutharsan Rajaratnam
    DATE: December 14, 2020
    APPLICATION: Payroll Web Application
    PURPOSE: 
    NOTE: 

    FILE: payroll/api/__init__.py

"""

from flask import Blueprint

blueprint_api   = Blueprint('api', __name__, url_prefix='/api',
                            template_folder='templates',
                            static_folder='static')

from . import views



