from django.shortcuts import render
from django.shortcuts import render_to_response
from BlogDatabase.models import BlogPost

# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()
    return render_to_response("archive.html", locals())
