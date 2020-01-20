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
blueprint_client   = Blueprint('client', __name__, url_prefix='/client',
                            template_folder='templates',
                            static_folder='static')

from . import views