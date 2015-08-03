from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from database.models import Book
from django.core.mail import send_mail
from django.template import RequestContext 
from app.forms import ContactForm

# Create your views here.

def display_some(request, template_name):
    keys = []
    values = []
    for key  in request.META.keys():
        keys.append(key)

    for value in request.META.values():
        values.append(value)


    values = request.META

    return render_to_response(template_name, locals())

def search(request):
    errors = []
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            errors.append("Please enter a search term.")
        elif len(query)> 20:
            errors.append("Please enter at most 20 characters.")
        else:
            books = Book.objects.filter(title__icontains = query)
            return render_to_response("search_results.html", locals())

    return render_to_response("search_form.html", locals())
        
def thanks(request):
    return render_to_response("contact_thanks.html", locals())

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                )

            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(initial={"subject" : "I love your site!"})

    return render_to_response("contact_form.html", locals(), context_instance = RequestContext(request))
