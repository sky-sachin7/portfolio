from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def project(request):
    # List of projects
    projects_show = [
        {
            "title": "Whatsapp Chat Analysis",
            "link": "https://github.com/sky-sachin7/whatsapp_chat",
            "description": "A tool to analyze WhatsApp chat data and provide meaningful insights."
        },
        {
            "title": "Portfolio Website",
            "link": "https://github.com/sky-sachin7/portfolio_website",
            "description": "A personal portfolio website showcasing skills and projects."
        },
         {
            "title": "Music Recommendation System",
            "link": "https://github.com/sky-sachin7/music-recommendation-system",
            "description": "A machine learning project that provides music recommendation."
        },
        {
            "title": "Email spam",
            "link": "https://github.com/sky-sachin7/OIBSIP",
            "description": "A machine learning project that shows given mail is spam or not."
        }
    ]
    return render(request, "projects.html", {"projects_show": projects_show})


def experience(request):
    experience = [
        {
            "company":"ABC",
            "position":"Python Developer"},
        {
            "company":"XYZ",
            "position":"Software Developer"},
    ]
    return render(request, "experience.html", {"experience":experience})

def education(request):
    education = [
        {
            "college": "IIT Patna",
            "class": "MTech in Computer Science Engineering",
            "cpi": ""
        },
        {
            "college": "Gurukul Kangri University, Haridwar",
            "class": "BTech in Computer Science",
            "cpi": "8.87"
        },
        {
            "college": "Delhi Public School International Garhan, Muzaffarpur",
            "class": "Senior Secondary",
            "cpi": "86%"
        },
        {
            "college": "D.A.V Public School RunniSaidpur, Sitamarhi",
            "class": "Secondary",
            "cpi": "10 CGPA"
        }
    ]
    return render(request, "education.html", {"education": education})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = f"New Contact Form Submission from {name}"
        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        try:
            send_mail(
                subject,
                body,
                'sachingg948@gmail.com',  # Replace with your email
                ['sachingg948@gmail.com'],  # Replace with your email
                fail_silently=False,
            )
            return HttpResponse("Thank you for your message!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

    return render(request, 'contact.html')  # Replace with your template name


def resume(request):
    resume_path = "myapp/resume.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment';filename="resume.pdf"
            return response
        
    else:
        return HttpResponse("resume not fount", status=404)
