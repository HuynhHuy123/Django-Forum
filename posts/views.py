from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
def index(request):
    #If the method is Post
    if request.method == 'POST':
        form = PostForm(request.POST)
    #If the form is valid
        if form.is_valid():
        #Yes, Save
            form.save()
        #Redirect to 
            return HttpResponseRedirect('/')
        else:
        #No, Show Error
            return HttpResponseRedirect(form.error.as_json())
    posts =Post.objects.all()[:20]
    #show
    return render(request, 'posts.html', {'posts': posts})

def delete(request, post_id):
    output ='POST ID is ' + str(post_id)
    return HttpResponse(output)


