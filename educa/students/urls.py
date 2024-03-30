from django.urls import path
from students import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', views.StudentCourseListView.as_view(), name='student_course_list'),
    path('courses/<pk>/',(views.StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('courses/<pk>/<module_id>/',(views.StudentCourseDetailView.as_view()), name='student_course_detail_module'),
]