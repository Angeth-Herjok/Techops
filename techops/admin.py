from django.contrib import admin
from .models import Student, Attendance, Marks,Notice, Subject, Enrollment, Teacher, Assignment, Notification, AttendanceHistory

# Register your models here.

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Marks)
admin.site.register(Notice)
admin.site.register(Subject)
admin.site.register(Enrollment)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(Notification)
admin.site.register(AttendanceHistory)
