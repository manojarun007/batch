"""
to explain oops concepts
"""

from m1 import emp


class EmpExtra(emp):
    """
    to maintain emp data
    """
    def __init__(self):
        pass
    @staticmethod
    def sal_cal(emp_name):
        """
        to calculate sal.
        """
        print "this is sal_cal"
        print emp_name
o1 = EmpExtra()
o1.leavecal()
o1.sal_cal(10)
