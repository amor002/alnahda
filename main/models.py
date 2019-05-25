from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    seat_number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.name)


class Subject(models.Model):

    subject_name = models.CharField(max_length=40)
    student_mark = models.FloatField()
    minimum_mark = models.IntegerField()
    full_mark = models.IntegerField()
    in_total_result = models.BooleanField(default=True)
    student_seat_number = models.IntegerField()

    def __str__(self):
        return str(self.student_seat_number)+'-' + self.subject_name