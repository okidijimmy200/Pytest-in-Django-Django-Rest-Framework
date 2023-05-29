import pytest
from django.test import TestCase
from classroom.models import Student, ClassRoom
from mixer.backend.django import mixer
from hypothesis import strategies as st, given

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


@given(st.floats(min_value=0, max_value=39.99))
def test_grade_fail(fail_score):
    print(fail_score)
    mixer.blend(Student, average_score=fail_score)
    student_result = Student.objects.last()
    assert student_result.get_grade() == "Fail"


@given(st.floats(min_value=40, max_value=70))
def test_grade_pass(pass_grade):
    mixer.blend(Student, average_score=pass_grade)
    student_result = Student.objects.last()
    assert student_result.get_grade(), "Excellent"


# @given(st.characters())
# def test_slugify(name):
#     print(name)
#     student_1 = mixer.blend(Student, first_name=name)
#     student_1.save()
#     student_result = Student.objects.last()
#     assert len(str(student_result.usernmae)) == len(name)


class TestClassroomModel:
    def test_classrom_create(self):
        mixer.blend(ClassRoom, name="physics")
        classroom_result = ClassRoom.objects.last()
        assert str(classroom_result) == "physics"
