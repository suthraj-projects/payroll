"""
    AUTHOR: Sutharsan Rajaratnam
    DATE: November 17, 2019
    APPLICATION: Payroll Web Application
    PURPOSE: Global Application Configurations
    NOTE: Explicitly excluded using 'SQLAlchemy' (Python SQLtoolkit & ORM), wanted to maintain non-Python universal readability. 
"""

import os
from flask import Flask
from flask_mysqldb import MySQL


########################################################################
###############===== CONSTANTS: GENERAL APPLICATION =====###############
########################################################################
BASE_DIR        = os.path.abspath(os.path.dirname(__file__)) 
UPLOAD_FOLDER   = '/data/uploads/'
UPLOAD_PATH     = BASE_DIR + UPLOAD_FOLDER

app = Flask(__name__)
app.secret_key = "secret key"

app.config['BASE_DIR'] = BASE_DIR
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PATH'] = UPLOAD_PATH
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])
#app.config['APP_ROOT_PATH'] = APP_PATH_ROOT

########################################################################
##########===== CONSTANTS: DATABASE CONFIGURATION =====##########
########################################################################
app.config['DB_TABLE_TIME_REPORT']          = "time_report"
app.config['DB_TABLE_PAYROLL_REPORT']       = "payroll_report"
app.config['DB_TABLE_TIMESHEET_HISTORY']    = "timesheet_history"   
app.config['DB_TABLE_PAYROLL_HISTORY']      = "payroll_history"

# MySQL configurations
app.config['MYSQL_HOST']          = 'localhost'
app.config['MYSQL_USER']          = 'srpub'
app.config['MYSQL_PASSWORD']      = 'mysql111'
app.config['MYSQL_DB']            = 'payroll'
app.config['MYSQL_CURSORCLASS']   = 'DictCursor'

mysql = MySQL(app)

########################################################################
##########====== CONSTANTS: PAYROLL APPLICATION specific =====##########
########################################################################
app.config['PAY_PERIOD_THRESHOLD'] = 15
app.config['PAY_RATE_GROUP_A'] = 20.0
app.config['PAY_RATE_GROUP_B'] = 30.0


