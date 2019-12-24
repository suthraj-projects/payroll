####################################
###AUTHOR: Sutharsan Rajaratnam
###DATE: November 17, 2019
###APPLICATION: Payroll Web Application
###PURPOSE: Database Schema/Models
###NOTE: Explicitly excluded using 'SQLAlchemy' (Python SQLtoolkit & ORM), wanted to maintain non-Python universal SQL readability. 
####################################

#FUNCTION: Returns MySQL string to create database table that stores uploaded timesheet data
def db_model_time_report(tb_name):
        
    sql = """CREATE TABLE %s 
    (    
        date VARCHAR(25) NOT NULL,
        hours_worked DECIMAL(7,2) DEFAULT '0.00' NOT NULL,
        employee_id INT NOT NULL,
        job_group CHAR(1) NOT NULL,
        report_id INT NOT NULL
    )""" %(tb_name) 
    
    return sql


#FUNCTION: Returns MySQL string to create database table that stores final Payroll report data
def db_model_payroll_report(tb_name):
    #CONSTRAINT prime UNIQUE(num, employee_id)

    sql = """CREATE TABLE %s (    
                    employee_id INT NOT NULL,
                    pay_period VARCHAR(51) NOT NULL,
                    amount_paid DECIMAL(15,2) DEFAULT '0.00' NOT NULL
                )""" %(tb_name) 
    return sql


#FUNCTION: Returns MySQL string to create database table that stores history of uploaded timesheet data for all successfully 
#uploaded timehseets
def db_model_timesheet_history(tb_name):
        
    sql = """CREATE TABLE %s 
    (    
        date VARCHAR(25) NOT NULL,
        hours_worked DECIMAL(7,2) DEFAULT '0.00' NOT NULL,
        employee_id INT NOT NULL,
        job_group CHAR(1) NOT NULL,
        report_id INT NOT NULL
    )""" %(tb_name) 
    
    return sql


#FUNCTION: Returns MySQL string to create database table that stores payroll history of successfully uploaded timesheets
def db_model_payroll_history(tb_name):
    
    sql = """CREATE TABLE %s 
    (    
        employee_id INT NOT NULL,
        report_id INT NOT NULL,
        pay_date_id DATE NOT NULL,
        pay_period CHAR(51) NOT NULL,
        amount_paid DECIMAL(15,2) DEFAULT '0.00' NOT NULL,
        PRIMARY KEY(employee_id, pay_date_id, pay_period, report_id)
    )""" %(tb_name) 
    
    return sql

