from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_id = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=50)

    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_lectures = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    
class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True)
    teacher_name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)
        
        
        #  subject enrollment
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignment/')

    


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    due_date = models.DateField()



class AttendanceHistory(models.Model):
    Attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    date_modified = models.DateField()
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
     






   




