"""

    AUTHOR: Sutharsan Rajaratnam
    DATE: December, 24, 2019
    PURPOSE: Unit test cases to test payroll compute functions
    tests/.../classesTC_in/TC_ComputePayroll.py
    
    TODO:
    
    NOTE-01:    This file must be executed one-level above the project folder so that the project python packages dependencies can be imported
                as follows.
                    -Direct test class call
                        python -m unittest -v payroll.tests.un.classesTC_un.TC_ComputePayroll
                    - Indirect call via test suite file
                        python -m unittest -v payroll.tests.un.run_un_ts_main
    
    NOTE-02:    For test case purposes, do not use 'def __init__' as class constructor to initialize object for test case execution, use 'setUp()'
                instead to initialize class parameters.
    
    NOTE-03:    The unittest methods 'failUnless**' is deprecated and not supported when using pytest, thus avoid its usage in test cases. 
    
    NOTE-04:    To show docstrings, navigate one-level above project folder and execute the following
                    Run python interpretor from command line, then
                    >>> import payroll.tests.un.classesTC_un.TC_ComputePayroll as A
                    >>> help(A.CalculatePay)


"""


import unittest

import payroll.web_app.main.config as conf

try:
    import payroll.web_app.main.modules.payroll as pay 

except ImportError:
    print('ERROR: Import modules not found')


class CalculatePay(unittest.TestCase):
    """ 
        Class 'ComputePay' contains unit test cases to validate employee specific payroll computation'.
        
        
        ATTRIBUTES:
        ---------------
        None
        
        
        METHODS:
        ---------------
        setUp()
            Sets up MySQL database connection
            Gets app configuration parameters
        
        tearDown()
            Closes/Deletes MySQL database connection
        
        test_un_cp_01()
            Test case checks if app conf value for 'PAY_PERIOD_THRESHOLD' = 15
            
        test_un_cp_02()
            Check employee pay calculation when employee worked 5 hours with group pay rate= 'A'
        
        test_un_cp_03()
         
    """
    
    
    def setUp(self):
        """
            Sets up MySQL database connection.
            Gets app configuration parameters.
        """        

        print '\nIn setUp() '
        self.mysql = conf.mysql
        self.app = conf.app

    
    def tearDown(self):
        """
            Closes/Deletes MySQL database connection
        """
        
        print 'In tearDown()'
        del self.mysql

    
    def test_un_cp_01(self):
        """
            Test case checks if app conf value for 'PAY_PERIOD_THRESHOLD' = 15 
        """
        
        #self.failUnlessEqual(self.fixture, range(0, 10), "List range should be from 0 to 9")
        self.assertEqual(self.app.config['PAY_PERIOD_THRESHOLD'], 15, "Pay period threshold value should be = 15")
        
   
    def test_un_cp_02(self):
        """
            Check employee pay calculation when employee worked 5 hours with group pay rate= 'A'
        """
        
        eid_hours = 5
        pay_rate_group = self.app.config['PAY_RATE_GROUP_A']
        test_expected_pay = eid_hours * pay_rate_group
        print pay.compute_pay(self.app,eid_hours,'A')
        print test_expected_pay
        self.assertEqual(pay.compute_pay(self.app,eid_hours,'A'), test_expected_pay, "Function 'payroll.compute_pay' should match 'test_expected_pay'")

        
#    def test_un_cp_03(self):
#        self.assertEqual(len(self.fixture), 10, "Length of list should be 10")

  

def suite_all():
    suite_lst = []
    suite_lst.append(unittest.TestLoader().loadTestsFromTestCase(CalculatePay))
    #suite_lst.append(unittest.TestLoader().loadTestsFromTestCase(FixtureTest_Fail))
    return suite_lst


#Executed when this python test case file is executed directly
if __name__ == "__main__":

    # begin the unittest.main()
    unittest.main()
    
    
    #a = CalculatePay()
    #a.setUp()
    #a.test_un_cp_01()
    #a.tearDown()
#    print("Everything passed")




