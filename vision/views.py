from django.shortcuts import render
from django.http import HttpResponse
from vision.forms import ImageForm


# Create your views here.

def index(request):
    """ Index page """
    return HttpResponse("Hello, world!")


def upload(request):
    """ Upload new image """
    if request.method != 'POST':
        form = ImageForm()
    else:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Upload successful!")
    context = {'form': form}
    return render(request, 'vision/upload.html', context)