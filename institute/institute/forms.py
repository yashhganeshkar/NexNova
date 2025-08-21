
from django import forms
from .models import Trainer, Subject

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ["empId", "name", "email", "phone", "subjects"]
        label = {
            "empId" : "Employee ID",
            "name" : "Trainer Name",
            "email" : "Email",
            "phone" : "Contact Number",
            "subject" : "Subject Taught"
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "description"]

        label = {
            "name" : "Subject Name = ",
            "description" : "Description = "
        }