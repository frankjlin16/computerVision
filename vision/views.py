import boto3 as boto3
from clarifai.rest import ClarifaiApp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from vision.forms import ImageForm


# Create your views here.

def index(request):
    """ Index page """
    context = {
        "data": "testing, testing, 123",
        "list": [1, 2, 3, 4, 5, 6]
    }
    return render(request, "vision/index.html", context)


def upload(request):
    """ Upload new image """
    if request.method != 'POST':
        form = ImageForm()
    else:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            print(type(new_image.image))
            #vision(new_image.image)
            return redirect('vision:result')
    context = {'form': form}
    return render(request, 'vision/upload.html', context)


def result(request):
    """ Result page """
    return render(request, 'vision/result.html')


def vision(photo):
    client = boto3.client('rekognition')

    app = ClarifaiApp(api_key='0ae4f38ea378451599e860e7e7cb2868')
    model = app.public_models.demographics_model
    model2 = app.public_models.apparel_model
    response_clar_appar = model2.predict_by_filename(photo)

    with open(photo, 'rb') as image:
        response_aws_fac = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])

    with open(photo, 'rb') as image:
        response_celeb_fac = client.recognize_celebrities(Image={'Bytes': image.read()})

    # print(response_clar_demo,response_clar_appar,response_aws_fac,response_celeb_fac)
    clothes_list = list()
    clothes = (response_clar_appar["outputs"][0]["data"]["concepts"])

    for clo in clothes[0:5]:
        if clo['value'] > 0.88:
            clothes_list.append(clo['name'])

    celeb_count = len(response_celeb_fac["CelebrityFaces"])

    face_char = response_aws_fac["FaceDetails"][0]

    smile = face_char['Smile']['Value']
    smile_c = face_char['Smile']['Confidence']

    eyeglasses = face_char['Eyeglasses']['Value']
    eyeglasses_c = face_char['Eyeglasses']['Confidence']

    beard = face_char['Beard']['Value']
    beard_c = face_char['Beard']['Confidence']

    emotions = face_char['Emotions'][0]['Type']
    emotions_c = face_char['Emotions'][0]['Confidence']

    print(emotions, emotions_c, celeb_count, face_char, smile, smile_c, eyeglasses, eyeglasses_c, beard, beard_c)
