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
    import payroll.web_app.main.modules.payroll as payroll

except ImportError:
    print('ERROR: Import modules not found')


class TC_Payroll(unittest.TestCase):
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

    
    """
        ===== Fixture setup for this test case class =====
    """
    
    def setUp(self):
        """
            Sets up MySQL database connection.
            Gets app configuration parameters.
        """        

        #print ("\nIn setUp() ")
        self.mysql = conf.mysql
        self.app = conf.app
    
    def tearDown(self):
        """
            Closes/Deletes MySQL database connection
        """
        
        #print ("In tearDown()")
        del self.mysql


    """
        ===== Test cases for this class =====
    """
    
    def test_un_conf_01(self):
        """
            Validate app conf. pay period threshold.
            Function/Feature Under Test (FUT):    web_app.main.config.app
        """
        
        test_value = 15
        appConf_val = self.app.config['PAY_PERIOD_THRESHOLD']
        self.assertEqual(appConf_val, test_value, "Validate app conf. pay period threshold")

        
    def test_un_conf_02(self):
        """
            Validate app conf. employee pay rate for group A employees.
            Function/Feature Under Test (FUT):    web_app.main.config.app
        """
        
        test_value = 20
        appConf_val = self.app.config['PAY_RATE_GROUP_A']
        self.assertEqual(appConf_val, test_value, "Validate app conf. employee pay rate for group A employees")

        
    def test_un_conf_03(self):
        """
            Validate app conf. employee pay rate for group B employees.
            Function/Feature Under Test (FUT):    web_app.main.config.app
        """
        
        test_value = 30
        appConf_val = self.app.config['PAY_RATE_GROUP_B']
        self.assertEqual(appConf_val, test_value, "Validate app conf. employee pay rate for group B employees")


    def test_un_cp_01(self):
        """
            Check employee pay calculation when employee worked 5 hours with group pay rate= 'A'
            Function/Feature Under Test (FUT):    web_app.main.config.app
        """
        
        eid_hours = 5
        pay_rate_group = self.app.config['PAY_RATE_GROUP_A']
        test_expected_val = eid_hours * pay_rate_group
        #print ("\n")
        #print (payroll.compute_pay(self.app,eid_hours,'A'))
        #print (test_expected_pay)
        self.assertEqual(payroll.compute_pay(self.app,eid_hours,'A'), test_expected_val, "Function returns incorrect pay value")


    def test_un_cp_02(self):
        """
            Check employee pay calculation when employee worked 5 hours with group pay rate= 'B'
            Function/Feature Under Test (FUT):    payroll.compute_pay(app, eid_hours, eid_group)
        """
        
        eid_hours = 5
        pay_rate_group = self.app.config['PAY_RATE_GROUP_B']
        test_expected_val = eid_hours * pay_rate_group
        self.assertEqual(payroll.compute_pay(self.app,eid_hours,'B'), test_expected_val, "Function returns incorrect pay value")
        

    def test_un_cp_03(self):
        """
            Validate pay period assignment.
            Test case has multiple sub tests to test multiple inputs.
            Function/Feature Under Test (FUT):    payroll.getPayPeriod(pay_period, month, year)
        """
        test_input_tuple = (['1','2019'], ['8', '2019'], ['11', '2019'])
#        test_input_tuple_01 = (['16','1','2019'], ['21', '7', '2019'], ['30', '8', '2019'])
#        test_input_tuple_02 = (['1','1','2019'], ['7', '7', '2019'], ['15', '8', '2019'])

        #SUB-TEST-01:    Test pay dates < 15 of every month (ie. pay_period_mode = 1)
        with self.subTest("Testing when the pay_period_mode = 1"):
            pay_period_mode=1
            for data in test_input_tuple:
                
                month, year = data[0], data[1]
                strDateMin_p1 = "%s/%s/%s" %(1,month,year)
                strDateMax_p1 = "%s/%s/%s" %(15,month,year)
            
                test_expected_val = "%s - %s" %(strDateMin_p1, strDateMax_p1)    
                self.assertEqual(payroll.getPayPeriod(pay_period_mode, month, year), test_expected_val, "Validate pay period assignment")
            
        #SUB-TEST-02:    Test pay dates > 15 of every month (ie. pay_period_mode = 2)
        with self.subTest("Testing when the pay_period_mode = 2"):
            pay_period_mode=2
            for data in test_input_tuple:
                
                month, year = data[0], data[1]
                strDateMin_p1 = "%s/%s/%s" %(16,month,year)
                strDateMax_p1 = "%s/%s/%s" %(30,month,year)
            
                test_expected_val = "%s - %s" %(strDateMin_p1, strDateMax_p1)    
                self.assertEqual(payroll.getPayPeriod(pay_period_mode, month, year), test_expected_val, "Validate pay period assignment")

        
    def test_un_cp_04(self):
        """
            Validate pay period pay assignment.
            Test case has multiple sub tests to test multiple inputs.
            Function/Feature Under Test (FUT):    payroll.update_payPeriod_dict(payPeriod_dict, eid, str_payPeriod, eid_pay)
        """
        
        test_payPeriod_dict_data = {"16/1/2019 - 31/1/2019" : 150, "01/3/2019 - 15/3/2019" : 250, "16/11/2019 - 31/11/2019": 725}
        
        #SUB-TEST-01: Single test    
        with self.subTest("SUBT-01: Test pay period pay update using stored pay period pay data (Single test)"):
            eid_pay = 1000
            test_str_payPeriod = "16/1/2019 - 31/1/2019"
            
            #The 'copy()' method creates a separate copy of the mutable dictionary test constant 'test_payPeriod_dict_data'
            ##See following article on python mutable and immutable types for further details
            ##https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/
            test_data = test_payPeriod_dict_data.copy()
            
            test_expected_val = eid_pay + test_data[test_str_payPeriod]
            returned_dict = payroll.update_payPeriod_dict(test_data, 1, test_str_payPeriod, eid_pay)
            
            """ --- DEBUG TESTING ---
            print ("\n")
            print (test_payPeriod_dict_data)
            print (test_payPeriod_dict_data[test_str_payPeriod])
            print (test_expected_val)
            print (returned_dict[test_str_payPeriod])
            print (returned_dict)
            """
              
            self.assertEqual(returned_dict[test_str_payPeriod], test_expected_val, "Validate pay period assignment")
            
        #SUB-TEST-02: Multi-test version of 'SUBT-01'.    
        with self.subTest("SUBT-02: Test pay period pay update using stored pay period pay data (Multi-test)"):
            """
                Multi-test version of SUBT-01.
                Tests all pay period sample data stored in 'test_payPeriod_dict_data'
            """
            
            eid_pay = 5000
            test_data = test_payPeriod_dict_data.copy()
            returned_dict = None
            
            for key in test_payPeriod_dict_data:
                test_str_payPeriod = key
                test_expected_val = eid_pay + test_data[test_str_payPeriod]
                returned_dict = payroll.update_payPeriod_dict(test_data, 1, test_str_payPeriod, eid_pay)
                
                """ --- DEBUG TESTING ---
                print ("\n")
                print (key)
                print (test_payPeriod_dict_data[test_str_payPeriod])
                print (returned_dict[test_str_payPeriod])
                print (returned_dict)
                """
                
                self.assertEqual(returned_dict[test_str_payPeriod], test_expected_val, "Validate pay period assignment")
            


def suite_all():
    """
        Test suite acts as an aggregator for specific test classes to execute.
    """ 
    suite_lst = []
    suite_lst.append(unittest.TestLoader().loadTestsFromTestCase(TC_Payroll))
    #suite_lst.append(unittest.TestLoader().loadTestsFromTestCase(FixtureTest_Fail))
    return suite_lst


#Executed when this python test case file is executed directly
if __name__ == "__main__":

    # begin the unittest.main()
    unittest.main()





