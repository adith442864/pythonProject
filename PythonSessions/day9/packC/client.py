import sys

from pythonProject.PythonSessions.day9.packA.emp import employee

sys.path.append("/Users/adithbala/PycharmProjects/pythonProject/PythonSessions/day9/packA")
sys.path.append("/Users/adithbala/PycharmProjects/pythonProject/PythonSessions/day9/packB")

# import emp
# empobj = emp.employee(101,"John",1000)
# empobj.displayemp()
#
# import stu
# stuobj=stu.student(100,"Nick","A")
# stuobj.displaystu()

#Approach:
from emp import *
empobj=employee(101,"John",1000)
empobj.displayemp()

from stu import *
stuobj=student(101,"Scott","A")
stuobj.displaystu()
