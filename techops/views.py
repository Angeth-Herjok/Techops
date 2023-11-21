from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import Authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, AttendanceForm, MarksForm, AssignmentForm, NoticeForm
from .models import Student, Attendance, Marks, Notice, Notification, Subject, Enrollment

# Create your views here.

def home(request):
    return HttpResponse('welcome to this page')

@login_required
def add_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form. is_valid():
            form.save()
            messages.success(request, 'Marks added successfully.')
            return redirect('add_marks')
    else:
        form = MarksForm()
    return render(render, 'add_marks.html', {'form':form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']   
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'logged out successfully')
    return redirect('home')


@login_required
def dashboard(request):
    user_role= request.user.role
    if user_role == 'Teacher':
        return render(request, 'teacher_dashboard.html')
    else:
        return render(request, 'student_dashboard.html')

@login_required
def enroll_subject(request, subject_id):
    student = Student.objects.get(user=request.user)
    subjects = Subject.objects.get(id=subject-id)
    Enrollment.objects.create(student, subject=subject, date_enrollment= date.today())
    return redirect('dashboard')


@login_required
def upload_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form. is_valid():
            form.save()
            return redirect('teacher_dashboard')
    else:
        form = AssignmentForm()
    return render(request, 'upload_assignment.html', {'form':form})


@@login_required
def Create_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            new_notice=form.save()

            student = Student.objects.all()
            for students in students:
                Notification.objects.create(user=student.user, content=f"New notice published:{new_notice.title}")
            return redirect('dashboard')
        else:
            form = NoticeForm()
        return render(request, 'create_notice.html', {'form': form})


