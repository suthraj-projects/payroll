#########################################
###AUTHOR: Sutharsan Rajaratnam
###DATE: December, 24, 2019
###PURPOSE: Unit test cases to test payroll compute functions
### tests/.../classesTC_in/ComputePayroll.py
#########################################

#NOTE: The unittest methods 'failUnless**' is deprecated and not supported when using pytest, thus avoid its usage in test cases. 

import unittest

#from ... config import app
from payroll.web_app.config import conf
from payroll.web_app.modules import pay
#from payroll.web_app.app import app, mysql
#from payroll.web_app.app import app, mysql

try:
    pass
    #from payroll.web_app.modules import pay
    #from ... modules import pay
    #from conf import app
    #from payroll.web_app.app import app, mysql
except ImportError:
    print('ERROR: Import modules not found')


class CalculatePay(unittest.TestCase):
    def setUp(self):
#        print 'In setUp()'
        print "Hey------1"
        self.mysql = conf.mysql
        self.app = conf.app

    def tearDown(self):
#        print 'In tearDown()'
        del self.mysql

    def test_un_cp_01(self):
        #NOTE: The unittest methods 'failUnless**' is deprecated and not supported when using pytest, thus avoid its usage in test cases. 
        #self.failUnlessEqual(self.fixture, range(0, 10), "List range should be from 0 to 9")
        self.assertEqual(self.app.config['PAY_PERIOD_THRESHOLD'], 15, "Pay period threshold value should be = 15")
        
#    def test_un_cp_02(self):
#        self.assertEqual(len(self.fixture), 10, "Length of list should be 10")
#        #self.failUnlessEqual(len(self.fixture), 10, "Length of list should be 10")
        
#    def test_un_cp_03(self):
#        self.assertEqual(len(self.fixture), 10, "Length of list should be 10")
#        #self.failUnlessEqual(len(self.fixture), 10, "Length of list should be 10")


def suite_all():
    suite_lst = []
    suite_lst.append(unittest.TestLoader().loadTestsFromTestCase(CalculatePay))
    #suite_lst.append(unittest.TestLoader().loadTestsFromTestCase(FixtureTest_Fail))
    return suite_lst


if __name__ == "__main__":

    unittest.main()
    #a = CalculatePay()
    #a.setUp()
    #a.test_un_cp_01()
    #a.tearDown()
#    print("Everything passed")
