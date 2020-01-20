"""
    AUTHOR: Sutharsan Rajaratnam
    DATE: December 16, 2020
    APPLICATION: Payroll Web Application
    PURPOSE: 
    NOTE: 

    FILE: payroll/admin/__init__.py

"""

from flask import Blueprint

blueprint_admin   = Blueprint('admin', __name__, url_prefix='/admin',
                            template_folder='templates',
                            static_folder='static')

from . import views