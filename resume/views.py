from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
        return render (request,"home.html")

def about(request):
        return render (request,"about.html")

def project(request):
        project_show=[
                { "title": "Robo Speaker",
                   "path" :"images/r'speaker.jpg"},
                
                { "title": "Registration Page",
                   "path" :"images/signup page.jpg"},

                { "title": "WeatherApp",
                   "path" :"images/weather.jpg"}
        ]
        return render (request,"project.html",{"project_show": project_show})

def experience(request):
        experience=[
                {"company":"XYZ College",
                 "position":"1st year student" }     
        ]
        return render (request,"experience.html",{"experience":experience})

def certification(request):
        return render (request,"certification.html")

def contact(request):
        return render (request,"contact.html")

def resume(request):
        resume_path="myapp/resume.pdf"
        resume_path=staticfiles_storage.path(resume_path)
        if staticfiles_storage.exists(resume_path):
                with open(resume_path,"rb") as resume_file:
                        response=HttpResponse(resume_file.read(),content_type="application/pdf")
                        response['Content-Disposition']='attachment';filename="resume.pdf"
                        return response
        else:
                return HttpResponse("resume not found",status=404)
                