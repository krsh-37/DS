import unittest
from carsales import mcheck,customer
class test_car(unittest.TestCase):
    def setUp(self):
        self.obj=customer('kumar',9548687828)
    def teardown(self):
       pass
    def test_obj(self):
        self.assertEqual(self.obj.cusinfo(),'Customer name:kumar,mobile:9548687828')
    def test_mcheck(self):
        self.assertEqual(mcheck(501,'lego'),True,'Invalid auth')
        self.assertEqual(mcheck(508, 'pass'), False, 'Invalid auth')
    def test_ord(self):
        self.assertEqual(self.obj.order_car(101),True)
        self.assertEqual(self.obj.order_car(108), False)
if __name__=="__main__":
    unittest.main()