from rest_framework.serializers import ModelSerializer
from classroom.models import Student, ClassRoom



'''student serializer class'''
class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "first_name",
            "last_name",
            "admission_number",
            "is_qualified",
            "average_score",
            "usernmae",
        )

'''student serializer class'''
class ClassroomSerializer(ModelSerializer):
    class Meta:
        model = ClassRoom 
        fields = (
            "name",
            "student_capacity",
            "students",
        )