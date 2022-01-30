
class Human:
    """
    Создайте класс, описывающий человека (создайте метод, выводящий
информацию о человеке).
    """

    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

    def __str__(self):
        return "name : {}, surname : {}, gender : {}, age : {}".format(self.name, self.surname,
                                                                       self.gender, self.age)


class Student(Human):
    """
    На его основе создайте класс Студент (переопределите метод вывода
информации).
    """

    def __init__(self, name, surname, gender, age, department, year):
        super().__init__(name, surname, gender, age)
        self.department = department
        self.year = year

    def __str__(self):
        return "\n" + "Student " + super().__str__() + " , department : {}, year : {}".format(self.department,
                                                                                              self.year)


class StudentGroup:
    """
    Создайте класс Группа, который содержит список из объектов класса
Студент. Реализуйте методы добавления, удаления студента и метод поиска
студента по фамилии. Определите для Группы метод __str__() для
возвращения списка студентов в виде строки.
    """

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, student):
        self.students.remove(student)

    def find_student_by_surname(self, surname, students):
        return [vars(s) for s in students if s.surname == surname]



    def aslist(self):
        return self.students

    def __iter__(self):
        return iter(self.aslist())

    def __str__(self):
        return "Students: " + "\n" + ('[%s]' % ', '.join(map(str, self.students))) + "\n"


human1 = Human("I", "G", "g", "28")
student1 = Student("Ivan", "Ivanov", "m", "28", "physics", "3")
student2 = Student("Karl", "Karlov", "m", "28", "physics", "3")
student3 = Student("Lena", "Lenina", "m", "28", "physics", "3")
group1 = StudentGroup()
group1.add_student(student1)
group1.add_student(student2)
group1.add_student(student3)
group1.delete_student(student1)
print(group1)
print(group1.find_student_by_surname(surname="Karlov", students=group1))
