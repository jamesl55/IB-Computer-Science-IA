class Student:
  #Create 2 instance variables for name and grades.
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  #Create a function that will find and return the average of the grades.
  def average(self):
    temp_total = 0
    for i in self.grades:
      temp_total += i
    return temp_total / len(self.grades)

#Create another class that will inherit the properties of the first class.
class ClassAverage(Student):
  #Create an instance variable for student
  def __init__(self, students):
    self.students = students
  #Create a function that will use a for loop to loop through the list to find and print each student's average and total average of both students. Initialize total average to be 0.0
  def calculate_class_average(self):
    total_average = 0
    for student in self.students:
      print(f"{student.name} has an average of {student.average():.1f}.")
      total_average += student.average()
    total_average = total_average / len(self.students)
    print(f"Total average of all students is {total_average:.1f}.")

# Example usage
student1 = Student("Kid Cudi", [85, 95, 88, 92, 88])
student2 = Student("Drake", [92, 98, 95, 87, 87])

# Create a ClassAverage object with a list of students
class_average = ClassAverage([student1, student2])

# Calculate and print the class average
class_average.calculate_class_average()