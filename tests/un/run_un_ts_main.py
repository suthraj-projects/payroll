#########################################
###AUTHOR: Sutharsan Rajaratnam
###DATE: December, 24, 2019
###PURPOSE: Test suite (TS) 'runner' file
### tests/.../classesTC_un/run_un_ts_main.py
#########################################

import unittest

# Import test case module: 'TC_ComputePayroll
# from classesTC_un import ComputePayroll
from payroll.tests.un.classesTC_un import test_tc_payroll


#Used to print in terminal using different color text
#Used for status log message outputs such as WARNS, SUCCESS etc
class bcolors:
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKGREEN     = '\033[92m'
    
    #WARNING     = '\033[93m' #CYELLOW2
    WARNING     = '\033[33m' #CYELLOW
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'
    
    #S_CUSTOM
    NOTEA       = '\033[7m'
    NOTEB       = '\033[42m'
    NOTEC       = '\033[43m'
    NOTED       = '\033[44m'
    
    BLINK       = '\033[5m'


#print ("Executing Test Suite - START...")
print (bcolors.OKBLUE + "OK: Executing Test Suite - START..." + bcolors.ENDC)

# Get test suites from specific test classes 
suite_lst = test_tc_payroll.suite_all()

try:
    # initialize select test suite(s)
    loadSuites = unittest.TestSuite(suite_lst)

    
    ###----- RUNNER -----###
    # initialize a runner, pass in your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(loadSuites)

except:
    #print ("ERROR: Something went wrong with test suite execution")
    print (bcolors.FAIL + "ERROR: Something went wrong with test suite execution" + bcolors.ENDC)

finally:
    #print ("Executing Test Suite - DONE.")
    print (bcolors.OKBLUE + "OK: Executing Test Suite - DONE." + bcolors.ENDC)

