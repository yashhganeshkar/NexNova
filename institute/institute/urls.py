
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    #Trainer URLS

    path('admin/', admin.site.urls),
    path('trainers/', views.TrainerList, name="trainers"),
    path('addtrainer/', views.AddTrainer, name="add_trainer"),
    path('details/<int:trainer_id>/', views.TrainerDetails, name="trainerdetails"),
    path('removetrainer/<int:trainer_id>/', views.RemoveTrainer, name="removetrainer"),

    #Subject URLS

    path('subjects/', views.SubjectList, name="subjectlist"),
    path('addsubject/', views.AddSubject, name="addsubject"),
    path('subject/<int:subject_id>/', views.SubjectDetails, name="subjectdetails"),
]
