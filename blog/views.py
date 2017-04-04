from django.shortcuts import render
from django.views import generic
from .forms import PostForm
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post

class IndexView(generic.TemplateView):
    template_name = "blog/index.html"

class AboutView(generic.TemplateView):
    template_name = "blog/about.html"

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

            return HttpResponseRedirect('/members/')

        else:
            print form.is_valid()   #form contains data and errors
            print form.errors
 
    return render(request, 'blog/hire.html', {
        'form': form,
    })