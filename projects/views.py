from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import  Project
from .forms  import ProjectForm
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}

    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id = pk)
    tags = projectObj.tags.all()
    return render(request,'projects/single-project.html',{'project':projectObj,'tags':tags})

def CreateProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)