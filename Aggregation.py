class Teacher:
  def _init_(self, name: str):
    self.name = name

class Department:
  def _init_(self, teachers_list: list):

t1 = Teacher("Prof. Steven")
t2 = Teacher("Prof. Mia")

math_dept = Department([t1, tr])

del math_dept
print(f"Still active in memory: {t1.name}")
