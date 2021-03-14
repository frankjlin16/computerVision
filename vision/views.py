from django.shortcuts import render, redirect
from django.http import HttpResponse
from vision.forms import ImageForm


# Create your views here.

def index(request):
    """ Index page """
    context = {
        "data":"testing, testing, 123",
        "list": [1,2,3,4,5,6]
    }
    return render(request, "vision/index.html", context)


def upload(request):
    """ Upload new image """
    if request.method != 'POST':
        form = ImageForm()
    else:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vision:result')
    context = {'form': form}
    return render(request, 'vision/upload.html', context)


def result(request):
    """ Result page """

