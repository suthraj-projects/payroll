"""
    AUTHOR: Sutharsan Rajaratnam
    DATE: November 17, 2019
    APPLICATION: Payroll Web Application
    PURPOSE: Database operations
    NOTE: Explicitly excluded using 'SQLAlchemy' (Python SQLtoolkit & ORM), wanted to maintain non-Python universal SQL readability. 
"""


import dbModels as db_models
from datetime import datetime


#FUNCTION: Check if table exists in database
def db_tb_existsCheck(mysql, tb_name):
    cursor = mysql.connection.cursor()
    sql = "SHOW TABLES LIKE '%s'" %(tb_name)
    try:
        cursor.execute(sql);
        flag_tb_exists = cursor.fetchall()
        #print "SUCCESS - Table exists: '" + tb_name
        return flag_tb_exists  
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print "ERROR: Table '" + tb_name + "' does not exist in database "
    finally:
        cursor.close() 


#FUNCTION: Create new table in database.
def db_tb_create(mysql, sql, tb_name):
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    mysql.connection.commit()
    cursor.close()   


#FUNCTION: Drop specific database table.
def db_tb_drop(mysql, drop_tableName):
    #print "DROP - Dropping table"    

    cursor = mysql.connection.cursor()
    sql = "DROP TABLE %s" %(drop_tableName)
    try:
        cursor.execute(sql);
        mysql.connection.commit()
        #print "SUCCESS: Table '" + drop_tableName + "' dropped successfully "
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print "ERROR: Table '" + drop_tableName + "' does not exist in database "
    finally:
        cursor.close() 


#FUNCTION: Retrieve all data from a specific database table.
def get_tb(mysql, tb_name):
    #print "GET - Uploaded 'timesheet_report' data" 

    cursor = mysql.connection.cursor()
    sql    = "SELECT * FROM %s" %(tb_name)
    try:
        cursor.execute(sql);
        tb_data = cursor.fetchall()
        #print "SUCCESS: Table '" + tb_name + "' read successfully "
        return tb_data
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print "ERROR: Table '" + tb_name + "' does not exist in database "
    finally:
        cursor.close()


#FUNCTION: Get all data from table by ascending employee id order (ie. 'payroll_report' ).
def get_tb_data_order_01(mysql, tb_name):

    cursor = mysql.connection.cursor()
    sql    = "SELECT * FROM %s ORDER BY employee_id ASC" %(tb_name)
    try:
        cursor.execute(sql);
        db_pr_list = cursor.fetchall()
#        print "SUCCESS: Table '" + tb_name + "' read successfully "
        return db_pr_list
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print "ERROR: Table '" + tb_name + "' does not exist in database "
        return
    finally:
        cursor.close() 


#FUNCTION: Retrieve all data from table in ascending report ID order (ie. 'timesheet_history' ).
def get_tb_data_order_02(mysql, tb_name):
    #print "GET - Uploaded 'timesheet_report' data" 

    cursor = mysql.connection.cursor()
    sql    = "SELECT * FROM %s ORDER BY employee_id, report_id ASC" %(tb_name)
    try:
        cursor.execute(sql);
        tb_data = cursor.fetchall()
        #print "SUCCESS: Table '" + tb_name + "' read successfully "
        return tb_data
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print "ERROR: Table '" + tb_name + "' does not exist in database "
    finally:
        cursor.close()


#FUNCTION: Reset all tables listed
def db_tb_reset(mysql, DB_TB_NAMES):
    for key, val in DB_TB_NAMES.items():
        if (db_tb_existsCheck(mysql, val)):
            db_tb_drop(mysql, val)
            
    db_tb_init(mysql, DB_TB_NAMES)
    return 


#FUNCTION: Initialize all tables listed
def db_tb_init(mysql, DB_TB_NAMES):
    
    for key, val in DB_TB_NAMES.items():
        if not (db_tb_existsCheck(mysql, val)):   
            #Create Timesheet table
            if(val == DB_TB_NAMES["tb_timesheet"]):
                sql = db_models.db_model_time_report(DB_TB_NAMES["tb_timesheet"])
                db_tb_create(mysql, sql, DB_TB_NAMES["tb_timesheet"])
            
            #Create Payroll Report table
            elif(val == DB_TB_NAMES["tb_payroll"]):
                sql = db_models.db_model_payroll_report(DB_TB_NAMES["tb_payroll"])
                db_tb_create(mysql, sql, DB_TB_NAMES["tb_payroll"])
                
            #Create Timesheets history table
            elif(val == DB_TB_NAMES["tb_ts_history"]):
                sql = db_models.db_model_timesheet_history(DB_TB_NAMES["tb_ts_history"])
                db_tb_create(mysql, sql, DB_TB_NAMES["tb_ts_history"])
                
            #Create Payroll History table
            elif(val == DB_TB_NAMES["tb_history"]):
                sql = db_models.db_model_payroll_history(DB_TB_NAMES["tb_history"])
                db_tb_create(mysql, sql, DB_TB_NAMES["tb_history"])
            else:
                print "ERROR - Unknown table name"
    return


#FUNCTION: Update tables 'time_report' & 'timesheet_history' with uploaded new timesheet data
def db_update_database(mysql, csvData_list, report_id, DB_TB_NAMES, tb_names_drop):
    
    #Drop tables
    for key, val in tb_names_drop.items():
        if (db_tb_existsCheck(mysql, val)):
            db_tb_drop(mysql, val)
            
    db_tb_init(mysql, DB_TB_NAMES)    
    
    #Insert CSV data into payroll report table
    code, str = db_model_time_report_insert(mysql, csvData_list, report_id, DB_TB_NAMES["tb_timesheet"], DB_TB_NAMES["tb_ts_history"], DB_TB_NAMES["tb_history"])
    return code, str  


#FUNCTION: Insert new data into tables 'time_report' & 'timesheet_history'
def db_model_time_report_insert(mysql, csvData_list, report_id, tb_name_01, tb_name_02, tb_name_03):
    #Get list of unique report IDs already in database
    cursor = mysql.connection.cursor()
    try:
        sql1 = "SELECT DISTINCT(report_id) FROM %s ORDER BY report_id ASC" %(tb_name_03)
        cursor.execute(sql1);
        unique_reportIDs = cursor.fetchall()
#        print "SUCCESS: Table '" + tb_name_03 + "' read successfully "
        
        report_ids_list = []
        for row in unique_reportIDs:
            report_ids_list.append(row['report_id'])
        
        if not(report_id in report_ids_list):
            i = 0
            for row in csvData_list:
                sql1 = "INSERT INTO %s VALUES ('%s', '%f', '%d', '%s', '%d')" %(tb_name_01, row['date'], float(row['hours worked']), int(row['employee id']), row['job group'], report_id)    
                cursor.execute(sql1)
                mysql.connection.commit()
                
                sql2 = "INSERT INTO %s VALUES ('%s', '%f', '%d', '%s', '%d')" %(tb_name_02, row['date'], float(row['hours worked']), int(row['employee id']), row['job group'], report_id)    
                cursor.execute(sql2)
                mysql.connection.commit()
                
            print "New report successfully added to database"
            return 111, ""
        
        else:
            print "ERROR: Report ID '%s' already exists - Timesheet rejected!" %(report_id)
            return 333, str(report_id)
            
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print "ERROR: Failed to insert data into table: '%s'" %(tb_name_01)
        return 000, tb_name_01
    finally:
        cursor.close() 


#FUNCTION: Insert data into table 'payroll_report' 
def db_tb_payroll_report_insert(mysql, eid, tb_name_src, tb_name_dest):

    cursor = mysql.connection.cursor()
        
    #Get all unique timesheet entries from 'payroll history' table per unique employee_id and pay_period
    sql1 = "SELECT DISTINCT(pay_date_id), employee_id FROM %s WHERE employee_id=%d" %(tb_name_src,eid)
    
    unique_payDateIDs_list = ()
    try:
        cursor.execute(sql1);
        unique_payDateIDs_list = cursor.fetchall()
        #print "SUCCESS: Table '" + tb_name_src + "' read successfully "
        
        for row_dict in unique_payDateIDs_list:
            try:
                sql2 = "INSERT INTO %s (SELECT employee_id, pay_period, SUM(amount_paid) FROM %s WHERE employee_id='%d' AND pay_date_id='%s' GROUP BY pay_period)" %(tb_name_dest, tb_name_src, eid, row_dict["pay_date_id"])
                cursor.execute(sql2)
                mysql.connection.commit()
                #print "SUCCESS: Writing to '%s' table successful" %(tb_name_dest)
            except:
                print "ERROR: Writing to '%s' table failed" %(tb_name_dest)   
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print "ERROR: Table '" + tb_name_src + "' does not exist in database "
        return
    
    finally:
        cursor.close()
        

#FUNCTION: Insert data into table 'payroll_history'        
def db_tb_payroll_history_insert(mysql, eid, report_id, eid_payPeriod_dict, tb_name):
    
    cursor = mysql.connection.cursor()
    for key, val in eid_payPeriod_dict.items():
        str = key.strip()
        period_id = str.split('-')[0].strip()
        date_object = datetime.strptime(period_id, '%d/%m/%Y')
        
        sql = "INSERT INTO %s VALUES ('%d', '%d', '%s', '%s', '%f')" %(tb_name, eid, report_id, date_object, key, val)
        cursor.execute(sql)
        mysql.connection.commit()
        
    cursor.close()


#FUNCTION: Get unique employee IDs.
def get_ts_eid(mysql, tb_name):
    #print "GET - Unique employee IDs from table: 'timesheet_report'" 

    cursor = mysql.connection.cursor()
    sql = "SELECT DISTINCT(employee_id) FROM %s ORDER BY employee_id ASC" %(tb_name)
    try:
        cursor.execute(sql);
        db_tb_uniqueIDs = cursor.fetchall()
#        print "SUCCESS: Table '" + tb_name + "' read successfully "
        return db_tb_uniqueIDs
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print "ERROR: Table '" + tb_name + "' does not exist in database "
        return
    finally:
        cursor.close() 


#FUNCTION: Get all data for a specific employee id.
def get_ts_eid_data(mysql, tb_name, eid):
    #print "GET - Retrieve employee id specific data from table: 'timesheet_report' table"
    
    cursor = mysql.connection.cursor()
    sql    = "SELECT * FROM %s WHERE employee_id = %d ORDER BY employee_id ASC" %(tb_name, eid)

    try:        
        cursor.execute(sql);
        db_tr_eid_data = cursor.fetchall()
#        print "SUCCESS: Table '" + tb_name + "' read successfully "
        return db_tr_eid_data
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print "ERROR: Table '" + tb_name + "' does not exist in database "
        return
    finally:
        cursor.close() 
        
