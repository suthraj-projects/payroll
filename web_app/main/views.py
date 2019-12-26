##################################################################################
###AUTHOR: Sutharsan Rajaratnam
###DATE: November 17, 2019
###APPLICATION: Payroll Web Application
###PURPOSE: The main application file to run the "Payroll Report" web application
###NOTE: Explicitly excluded using 'SQLAlchemy' (Python SQLtoolkit & ORM), wanted to maintain non-Python universal readability. 
##################################################################################

import os
from datetime import datetime
#from app import app, mysql
from config import app, mysql
from flask import Flask, flash, render_template, request, redirect
from werkzeug.utils import secure_filename

import modules as m

DB_TB_NAMES    = {
                    "tb_timesheet":     app.config['DB_TABLE_TIME_REPORT'], 
                    "tb_payroll":       app.config['DB_TABLE_PAYROLL_REPORT'],
                    "tb_ts_history":    app.config['DB_TABLE_TIMESHEET_HISTORY'],
                    "tb_history":       app.config['DB_TABLE_PAYROLL_HISTORY']
                }


#ROUTE: Default (ie.'homepage') route for web application
@app.route("/")
def home():
    m.db.db_op.db_tb_init(mysql, DB_TB_NAMES)
    tb_data_csv = m.db.db_op.get_tb(mysql, app.config['DB_TABLE_TIME_REPORT'])    
    return render_template("home.html", tb_tr_data=tb_data_csv)

#ROUTE: Provides brief overview of web application.
@app.route("/about")
def about():
    return render_template("about.html")


#ROUTE: Upload timesheet files to server.
@app.route('/', methods=['POST'])
def upload():
#    print "STEP 1:    Upload Data File "
    process_upload()
    return redirect('/')


#ROUTE: Shows processed payroll report based on all uploaded timesheets.
@app.route("/payrollreport")
def payrollReport():    
    db_pr_list = m.db.db_op.get_tb_data_order_01(mysql, app.config['DB_TABLE_PAYROLL_REPORT'])
    return render_template("payrollreport.html", tb_csvData=db_pr_list)


#ROUTE: Shows history of raw timesheet data from all successfully uploaded timesheets.
@app.route("/timesheethistory")
def timesheetHistory(): 
    db_ts_history_list = m.db.db_op.get_tb_data_order_02(mysql, app.config['DB_TABLE_TIMESHEET_HISTORY'])
    return render_template("ts_history.html", tb_data=db_ts_history_list)


#ROUTE: Resets all server side tables listed in 'DB_TB_NAMES' dictionary above.
@app.route("/reset")
def reset():
    m.db.db_op.db_tb_reset(mysql, DB_TB_NAMES)
    return redirect('/')


###########################################################################################
#Local support functions that call relevant custom application functions defined elsewhere 
#in the 'modules' folder    
###########################################################################################

def process_upload():
    filepath        = app.config['UPLOAD_PATH']
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and m.upload.allowed_file(file.filename, app.config['ALLOWED_EXTENSIONS']):
            m.upload.upload_file(app.config['UPLOAD_PATH'], file)
            flash('File successfully uploaded', 'success')
            csvData_list, report_id = process_csv(filepath, file.filename)
            db_update_database(csvData_list, report_id)
            process_payroll(report_id) 
        else:
            flash('Allowed file types only: .csv')
            return redirect(request.url)

               
def process_csv(filepath, filename):
    
#    print "STEP 2:    Process CSV "
    csvData_list, csvData_footer = m.csvReader.importCSVUpload_dict(filepath, filename)
    report_id = int(csvData_footer[0]["hours worked"])
    return csvData_list, report_id


def db_update_database(csvData_list, report_id):    
    
#    print "STEP 3:    Update Table "
    
    #NOTE - PRODUCTION RELEASE: Remove 'tb_payroll' from the dictionary after testing 
    tb_names_drop = {
                "tb_timesheet":     app.config['DB_TABLE_TIME_REPORT'], 
                "tb_payroll":       app.config['DB_TABLE_PAYROLL_REPORT']
                } 
    
    code, str = m.db.db_op.db_update_database(mysql, csvData_list, report_id, DB_TB_NAMES, tb_names_drop)
    if (code == 111):
        msg = "New report successfully added to database"
        flash(msg, 'success')
    elif (code == 333):
        msg = "ERROR: Report ID '%s' already exists - Timesheet rejected!" %(str)
        flash(msg, 'error')
    elif (code == 000):
        msg = "ERROR: Failed to insert data into table: '%s'" %(str)
        flash(msg, 'error')
    else:
        msg = "ERROR - DATABASE UPDATE: Unknown code!"
        flash(msg, 'error')
    
    
def process_payroll(report_id):
#    print "===== PROCESS PAYROLL ====="
    m.pay.compute_payroll(app, mysql, report_id)


    
if __name__ == "__main__":
    app.run(debug=True)