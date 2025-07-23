from django.urls import path
from .views.main_view import add_student, get_student, update_student, delete_student, get_student_by


urlpatterns = [
    path('add/', add_student, name='add'),
    path('get/', get_student, name='get'),
    path('update/<int:id>', update_student, name='update'),
    path('delete/<int:id>', delete_student, name='delete'), 
    path('get_by/<int:id>', get_student_by, name="get_by")


]
