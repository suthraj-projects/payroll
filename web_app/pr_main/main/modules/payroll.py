"""
    AUTHOR: Sutharsan Rajaratnam
    DATE: November 17, 2019
    APPLICATION: Payroll Web Application
    PURPOSE:Payroll computation
"""

from . import dbMySQL as db
#from config import app
#from payroll.web_app.main.config import app
#from payroll.web_app.main import config
#from payroll.web_app.main.config import app
#import payroll.web_app.main.config.app as app


#FUNCTION: The 'main' function called externally to compute payroll
def compute_payroll(app, mysql, report_id):
#    print "Compute Payroll-----------"
    
    db_tb_uniqueIDs = db.db_op.get_ts_eid(mysql, app.config['DB_TABLE_TIMESHEET_HISTORY'])
    for id in db_tb_uniqueIDs:
        db_tr_eid_data = db.db_op.get_ts_eid_data(mysql, app.config['DB_TABLE_TIME_REPORT'], id['employee_id'])
        compute_payroll_eid(app, mysql, id['employee_id'], report_id, db_tr_eid_data)


#FUNCTION: Compute payroll for a given employee id
def compute_payroll_eid(app, mysql, eid, report_id, db_tr_eid_data):
    #print "Compute Payroll eid -----------"
    
    pay_period_threshold = app.config['PAY_PERIOD_THRESHOLD']

    payPeriod_dict = {}
    tmp_date_dict = {}
    for row in db_tr_eid_data:
        str = row["date"].strip()
        day, month, year = str.split('/')
        tmp_date_dict["day"] = int(day)
        tmp_date_dict["month"] = int(month)
        tmp_date_dict["year"] = int(year)
        
        #print "GET PAYROLL STRING -----"
        if (tmp_date_dict["day"] < pay_period_threshold):
            str_payPeriod = getPayPeriod(1, tmp_date_dict["month"], tmp_date_dict["year"])
            eid_pay = compute_pay(app, float(row["hours_worked"]), row["job_group"])
            payPeriod_dict = update_payPeriod_dict(payPeriod_dict, eid, str_payPeriod, eid_pay)
        else:
            str_payPeriod = getPayPeriod(2, tmp_date_dict["month"], tmp_date_dict["year"])
            eid_pay = compute_pay(app, float(row["hours_worked"]), row["job_group"])
            payPeriod_dict = update_payPeriod_dict(payPeriod_dict, eid, str_payPeriod, eid_pay)
            
    #print "===== POPULATE PAYROLL HISTORY TABLE ======"
    tb_name = 'payroll_history'
    db.db_op.db_tb_payroll_history_insert(mysql, eid, report_id, payPeriod_dict, tb_name)
    
    #print "===== POPULATE PAYROLL REPORT TABLE ====="
    db.db_op.db_tb_payroll_report_insert(mysql, eid, app.config['DB_TABLE_PAYROLL_HISTORY'], app.config['DB_TABLE_PAYROLL_REPORT'])
    

#FUNCTION: Tracks and updates total employee pay per pay period
def update_payPeriod_dict(payPeriod_dict, eid, str_payPeriod, eid_pay):

    key = str_payPeriod    
    if (len(payPeriod_dict) == 0):
        payPeriod_dict[key] = eid_pay
        return payPeriod_dict
        
    if (key in payPeriod_dict.keys()):
        payPeriod_dict[key] = payPeriod_dict[key] + eid_pay
        return payPeriod_dict
    else:
        payPeriod_dict[key] = eid_pay
        return payPeriod_dict


#FUNCTION: Returns correct 'pay_period' string for a given pay period
def getPayPeriod(pay_period, month, year):
     
    if (pay_period == 1):
        strDateMin_p1 = "%s/%s/%s" %(1,month,year)
        strDateMax_p1 = "%s/%s/%s" %(15,month,year)
        return "%s - %s" %(strDateMin_p1, strDateMax_p1)

    elif (pay_period == 2):
        strDateMin_p2 = "%s/%s/%s" %(16,month,year)
        strDateMax_p2 = "%s/%s/%s" %(30,month,year)
        return "%s - %s" %(strDateMin_p2, strDateMax_p2)
    else:
        print ("FAIL - Incorrect pay period value!")


#FUNCTION: Calculates employee actual pay based on hours worked & associated job group id        
def compute_pay(app, eid_hours, eid_group):
    if (eid_group == 'A'):
        eid_pay = app.config['PAY_RATE_GROUP_A'] * eid_hours
        return eid_pay
        
    elif (eid_group == 'B'):
        eid_pay = app.config['PAY_RATE_GROUP_B'] * eid_hours
        return eid_pay
    else:
        print ("FAIL - Unexpected value for 'eid_group'")
        return 0
