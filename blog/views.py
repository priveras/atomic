from django.shortcuts import render
from django.views import generic
from .forms import PostForm
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, Project
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

class IndexView(generic.TemplateView):
    template_name = "blog/index2.html"

class SoonView(generic.TemplateView):
    template_name = "blog/soon.html"

class AboutView(generic.TemplateView):
    template_name = "blog/about.html"

class ThanksView(generic.TemplateView):
    template_name = "blog/thanks.html"

class FaqView(generic.TemplateView):
    template_name = "blog/faq.html"

class ProjectListView(generic.ListView):
    template_name = 'blog/work.html'
    context_object_name = 'projects_list'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)

        return context

def hire(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
 
        if form.is_valid():

            post = Post.objects.create(
                project = form.cleaned_data['project'],
                status = form.cleaned_data['status'],
                timeline = form.cleaned_data['timeline'],
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                created_at = timezone.now()
                )
            
            plaintext = get_template('blog/emails/confirmation_email.txt')
            htmly     = get_template('blog/emails/confirmation_email.html')
            subject = 'We received your project info'        

            from_email, to = 'Team Attomik <hello@attomik.ccom>', form.cleaned_data['email']
            text_content = plaintext.render()
            html_content = htmly.render()
            mail = EmailMultiAlternatives(subject, text_content, from_email, [to])
            mail.attach_alternative(html_content, "text/html")
            mail.send()

            return HttpResponseRedirect('/thanks/')

        else:
            print form.is_valid()   #form contains data and errors
            print form.errors
 
    return render(request, 'blog/hire.html', {
        'form': form,
    })