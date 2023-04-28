from django.db import models

# Create your models here.
class City(models.Model):
    cityname = models.CharField(max_length=30)

    def __str__(self):
        return self.cityname


class Course(models.Model):
    coursename = models.CharField(max_length=30)

    def __str__(self):
        return self.coursename


class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=30)
    cityname = models.ForeignKey(City, on_delete=models.CASCADE)
    coursename = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname

