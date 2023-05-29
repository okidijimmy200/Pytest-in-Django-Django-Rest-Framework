from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def my_func_val(val):
    if val < 0:
        raise ValidationError(
            _("%(val)s is not a positive number"),
            params={"value": val},
        )


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admission_number = models.IntegerField(unique=True)

    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(blank=True, null=True, validators=[my_func_val])
    usernmae = models.SlugField(blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name

    def get_grade(self):
        if 0 <= self.average_score < 40:
            return "Fail"
        elif 40 <= self.average_score < 70:
            return "Pass"
        elif 70 < self.average_score < 100:
            return "Excellent"
        else:
            return "Error"

    def save(self, *args, **kwargs):
        self.usernmae = slugify(self.first_name)
        # to return student class
        super(Student, self).save(*args, **kwargs)


# classroom model
class ClassRoom(models.Model):
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField("classroom.Student")

    def __str__(self) -> str:
        return self.name
