import pytest
from classroom.models import Student, ClassRoom
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

pytestmarker = pytest.mark.django_db

'''test for views'''
class TestStudentAPIView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_student_list(self):
        # create client
        student = mixer.blend(Student, first_name="Jimmy")

        '''call the url'''
        url = reverse("student_list_api")

        # call the url
        response = self.client.get(url)

        assert response.json != None
        assert len(response.json()) > 0
        assert response.status_code == 200

    '''test create student works'''
    def test_create_student(self):
        data_required = {
            "first_name": "Jimmy",
            "last_name": 'okidi',
            "usernma": "",
            "admission_number": 2023,
            "is_qualified": True,
            "average_score": 100
        }

        # reverse url
        url = reverse('student_create_api')

        # call
        response = self.client.post(url, data=data_required)

        # assertions
        assert response.json != None
        assert response.status_code == 201
        # to count all elements in the query set
        assert Student.objects.count() == 1

        '''test create student works'''
    def test_detail_student(self):

        student = mixer.blend(Student, first_name="Jimmy")

        # reverse url, to get detail url
        url = reverse('student_detail_api', kwargs={"pk":1})

        # call
        response = self.client.get(url)

        # assertions
        assert response.json != None
        assert response.status_code == 200
        assert response.json()['first_name'] == 'Jimmy'
        assert response.json()['usernmae'] == 'jimmy'

    '''test create student works'''
    def test_detail_student(self):

        student = mixer.blend(Student, first_name="Jimmy")

        # reverse url, to get detail url
        url = reverse('student_delete_api', kwargs={"pk":1})

        # call
        response = self.client.delete(url)

        # assertions
        assert Student.objects.count() == 0
        assert response.status_code == 204

'''test for views'''
class TestClassroomAPIView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        User = get_user_model()
        self.user = User.objects.create(username='Jimmy', password='abcd')
        self.token = Token.objects.create(user=self.user)

        # append token to client
        self.client.credentials(HTTP_AUTHORIZATION="Token "+ self.token.key)

    def test_classroom_qs_works(self):
        classroom = mixer.blend(ClassRoom, student_capacity=20)
        classroom2 = mixer.blend(ClassRoom, student_capacity=27)

        url = reverse('class_qs_api', kwargs={'student_capacity': 15})

        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data['data'] != []