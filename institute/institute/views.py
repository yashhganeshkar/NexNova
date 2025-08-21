
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainer, Subject
from .forms import TrainerForm, SubjectForm

def TrainerList(request):
    trainers = Trainer.objects.all()
    return render(request, "trainersList.html", {"trainers":trainers})

def AddTrainer(request):
    if(request.method == "POST"):
        form = TrainerForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("trainers")
    else:
        form = TrainerForm()
    return render(request, "addtrainer.html", {"form":form})

def TrainerDetails(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk = trainer_id)
    return render(request, "trainerDetails.html", {"trainer": trainer})

def RemoveTrainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    if(request.method == "POST"):
        trainer.delete()
        return redirect("trainers")
    return render(request, "removetrainer.html")

# Subject routes

def SubjectList(request):
    subjects = Subject.objects.all()
    return render(request, "subjectList.html", {"subjects":subjects})

def SubjectDetails(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, "subjectDetails.html", {"subject":subject})

def AddSubject(request):
    if(request.method == "POST"):
        form = SubjectForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("subjectlist")
    else:
        form = SubjectForm()
    return render(request, "addSubject.html", {"form":form})