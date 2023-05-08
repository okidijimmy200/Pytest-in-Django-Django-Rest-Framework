import pytest
from django.test import TestCase
from classroom.models import Student, ClassRoom
from mixer.backend.django import mixer


pytestmark = pytest.mark.django_db


# test the student model
class TestStudentModel(TestCase):
    def setUp(self) -> None:
        self.student_1 = Student.objects.create(
            first_name="jimmy", last_name="okidi", admission_number=123456
        )

    # test to check that student can be created
    def test_student_can_be_created(self):
        mixer.blend(Student, first_name="jimmy")
        student_result = Student.objects.last()
        assert student_result.first_name == "jimmy"

    def test_str_return(self):
        # mixer to auto-generate model values
        mixer.blend(Student, first_name="jimmy")
        student_result = Student.objects.last()
        assert str(student_result) == "jimmy"

    def test_grade_fail(self):
        mixer.blend(Student, average_score=10)
        student_result = Student.objects.last()
        assert student_result.get_grade() == "Fail"

    def test_grade_pass(self):
        mixer.blend(Student, average_score=80)
        student_result = Student.objects.last()
        assert student_result.get_grade(), "Excellent"


class TestClassroomModel:
    def test_classrom_create(self):
        mixer.blend(ClassRoom, name="physics")
        classroom_result = ClassRoom.objects.last()
        assert str(classroom_result) == "physics"
