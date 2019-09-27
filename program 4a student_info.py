class school:
    def __init__(self):
        self.student_id=0
        self.age=0
        self.marks=0
    def validate_marks(self):
        if self.marks>=0 and self.marks<=100:
            return True
        else:
            return False

    def validate_age(self):
        if self.age>20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.marks>65:
                return True
            else:
                return False
        else:
            return False

    def set_data(self):
        self.student_id=int(input("enter student id:"))
        self.age=int(input("enter age:"))
        self.marks=int(input("enter marks:"))

                       
    def get_data(self):
        print("student_id:",self.student_id)
        print("age:",self.age)
        print("marks:",self.marks)
x=school()
x.set_data()
if x.check_qualification():
     x.get_data()
else:
     print("no admission")
