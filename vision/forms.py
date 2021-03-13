from django.forms import ModelForm

from vision.models import Image


class ImageForm(ModelForm):
    """ Image form based on Image model """
    class Meta:
        model = Image
        fields = ['image']
