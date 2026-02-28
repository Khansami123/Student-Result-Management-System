class Person:
    def __init__(self, name, person_id):
        self._name = name
        self._person_id = person_id

    def get_details(self):
        return f"Name: {self._name}, ID: {self._person_id}"


class Result:
    def __init__(self):
        self._marks = {}

    def add_marks(self, subject, marks):
        if 0 <= marks <= 100:
            self._marks[subject] = marks
        else:
            print("Marks should be between 0 and 100")

    def calculate_total(self):
        return sum(self._marks.values())

    def calculate_percentage(self):
        if len(self._marks) == 0:
            return 0
        return self.calculate_total() / len(self._marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def get_marks(self):
        return self._marks


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.result = Result()

    def add_marks(self, subject, marks):
        self.result.add_marks(subject, marks)

    def get_result_summary(self):
        total = self.result.calculate_total()
        percentage = self.result.calculate_percentage()
        grade = self.result.calculate_grade()
        return total, percentage, grade

    def __str__(self):
        total, percentage, grade = self.get_result_summary()
        return (f"Student: {self._name}\n"
                f"Total Marks: {total}\n"
                f"Percentage: {percentage:.2f}%\n"
                f"Grade: {grade}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all_results(self):
        for student in self.students:
            print(student)
            print("-" * 30)

    def __len__(self):
        return len(self.students)


# ==============================
# Live Execution Example
# ==============================

if __name__ == "__main__":
    sms = StudentManagementSystem()

    student1 = Student("Alice", 101)
    student1.add_marks("Math", 85)
    student1.add_marks("Science", 78)
    student1.add_marks("English", 90)

    student2 = Student("Bob", 102)
    student2.add_marks("Math", 60)
    student2.add_marks("Science", 55)
    student2.add_marks("English", 65)

    sms.add_student(student1)
    sms.add_student(student2)

    sms.show_all_results()

    print("Total Students:", len(sms))
