class Student:
  school_name = "GCK"

  def __init__(self, name, roll_no, marks):
    self.name = name
    self.roll_no = roll_no
    self.__marks = marks 

  
  def get_marks(self):
    return self.__marks

  def calculate_grade(self):
    avg = self.__marks
    if avg >= 90:
      return "A"
    elif avg >= 75:
      return "B"
    elif avg >= 60:
      return "c"
    else:
      return "Fail"

  def passing_marks():
    return 40

class SportsStudent(Student):
  def calculate_grade(self):
    bonus_marks = self.get_marks()+ 5
    if bonus_marks >= 90:
      return "A"
    elif bonus_marks >= 75:
      return  "B"
    elif bonus_marks >= 60:
      return "c"
    else: 
      return "fail"


student1 = Student("Ameen", 101, 78)
student2 = SportsStudent("Safwan", 102, 58)

print("Student 1 Grade:", student1.calculate_grade())
print("Student 2 Grade:", student2.calculate_grade())

print("Passing Marks:", Student.passing_marks())
print("School Name:", Student.school_name)

