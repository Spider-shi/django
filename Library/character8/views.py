from django.shortcuts import render
from django.shortcuts import render_to_response
from database.models import Author, Publisher

# Create your views here.

def foo(request, template_name):
    m_list = Author.objects.all()
    return render_to_response(template_name, locals())


def bar(request, template_name):
    m_list = Publisher.objects.all()
    return render_to_response(template_name, locals())
