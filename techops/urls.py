from django.urls import path
from .import views
from .views add_marks, home, login_view, logout_view, dashboard, enroll_subject, upload_assignment,Create_assignment


urlpatterns = [
    path('', views.home, name = 'home'),
    path('add_marks/', add_marks, name='add_marks'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('dashboard/', dashboard, name='dashboard'),
    path('enroll_subject/<int;subject_id>/', enroll_subject, name='enroll-subject'),
     path('upload_assignment/', upload_assignment, name='upload-assignment'),

]