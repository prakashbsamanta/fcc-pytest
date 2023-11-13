# test_classroom.py
import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents


@pytest.fixture
def empty_classroom():
    teacher = Teacher("Professor McGonagall")
    return Classroom(teacher, [], "Transfiguration")


@pytest.fixture
def classroom_with_students():
    teacher = Teacher("Professor Snape")
    students = [Student("Draco Malfoy"), Student("Hermione Granger")]
    return Classroom(teacher, students, "Potions")


def test_add_student(empty_classroom):
    student = Student("Harry Potter")

    empty_classroom.add_student(student)
    assert len(empty_classroom.students) == 1


def test_remove_student(classroom_with_students):
    classroom_with_students.remove_student("Draco Malfoy")
    assert len(classroom_with_students.students) == 1
    assert any(student.name == "Draco Malfoy" for student in classroom_with_students.students) is False


def test_change_teacher(empty_classroom):
    new_teacher = Teacher("Professor Sprout")

    empty_classroom.change_teacher(new_teacher)
    assert empty_classroom.teacher == new_teacher


@pytest.mark.skip
def test_too_many_students_exception(empty_classroom):
    students = [Student(f"Student_{i}") for i in range(10)]
    empty_classroom.students = students

    with pytest.raises(TooManyStudents, match="Cannot add more than 10 students to the classroom") as excinfo:
        empty_classroom.add_student(Student("Luna Lovegood"))

    assert "Cannot add more than 10 students to the classroom" in str(excinfo.value)


@pytest.mark.parametrize("initial_students, student_to_add, expected_length", [
    ([], Student("Neville Longbottom"), 1),
    ([Student("Student1"), Student("Student2")], Student("Student3"), 3),
])
def test_add_student_parametrized(empty_classroom, initial_students, student_to_add, expected_length):
    empty_classroom.students = initial_students
    empty_classroom.add_student(student_to_add)
    assert len(empty_classroom.students) == expected_length
