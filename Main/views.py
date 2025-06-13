from django.shortcuts import render

# Create your views here.


# Home page view
def IndexView(request):
    return render(request, 'main/index.html')

def csProjectsView(request):
    return render(request, 'main/csProjects.html')

def pthProjectsView(request):
    return render(request, 'main/pthProjects.html')

def aboutView(request):
    return render(request, 'main/about.html')

def skillsView(request):
    return render(request, 'main/skills.html')

def contactView(request):
    return render(request, 'main/contact.html')

def resumeView(request):
    return render(request, 'main/resume.html')