#!/usr/bin/env python3
import sys
import collections
from collections import Counter
class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year,grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = Counter(grade)

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
    def get_grade(self):
        num = sum(self.grade.values())
        numD = self.grade['D']
        return "Pass: {}, Fail: {}".format(num-numD, numD)

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers,grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = Counter(grade).most_common()

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))
    
    def get_grade(self):
        s = ''
        for k, v in self.grade:
            s += k + ': ' + str(v) + ', '
        return s[:-2]

if __name__ == '__main__':
    if len(sys.argv) > 2:
        if sys.argv[1] == 'teacher':
            teacher1 = Teacher('harbin', ['c'], sys.argv[2])
            print(teacher1.get_grade())
        elif sys.argv[1] == 'student':
            student1 = Student('student','cse',2005, sys.argv[2])
            print(student1.get_grade())
    else:
        print(len(sys.argv))
