#########################################
###AUTHOR: Sutharsan Rajaratnam
###DATE: December, 24, 2019
###PURPOSE: Test suite (TS) 'runner' file
### tests/.../classesTC_un/run_un_ts_main.py
#########################################

import unittest

# Import test case module: 'TC_ComputePayroll
from classesTC_un import ComputePayroll


print "Executing Test Suite - START..."

# Get test suites from specific test classes 
suite_lst = ComputePayroll.suite_all()

try:
    # initialize select test suite(s)
    loadSuites = unittest.TestSuite(suite_lst)

    
    ###----- RUNNER -----###
    # initialize a runner, pass in your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(loadSuites)

except:
    print "ERROR: Something went wrong with test suite execution"

finally:
    print "Executing Test Suite - DONE."

