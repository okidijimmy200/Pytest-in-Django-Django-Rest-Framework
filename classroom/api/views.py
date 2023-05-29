from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from classroom.models import Student, ClassRoom
from classroom.api.serializers import StudentSerializer, ClassroomSerializer

'''Class to list students'''
class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

'''Class to create students'''
class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

'''Class to get detail of students'''
class StudentDetailAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

'''Class to get detail of students'''
class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

# view to return classrooms with certain number of students
class ClassroomNumberAPIView(APIView):
    serializer_class = ClassroomSerializer
    model = ClassRoom
    queryset = ClassRoom.objects.all()

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, *args, **kwargs):
        url_number = self.kwargs.get('student_capacity')

        classroom_qs = ClassRoom.objects.filter(student_capacity__gte= url_number)

        # serialize the data
        serialized_data = ClassroomSerializer(classroom_qs, many=True)

        if serialized_data.is_valid:
            print(serialized_data.data)
            # to return data, we need to serialize it
            return Response({'data': serialized_data.data}, status= status.HTTP_200_OK)
        return Response({'Error': 'Could not serialize data'}, status= status.HTTP_403_FORBIDDEN)
