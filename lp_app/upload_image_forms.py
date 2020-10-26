from django import forms 
from .models import *

#class form để request submit lên 
class ImageUploadForm(forms.ModelForm): 
    #nó có hai trường tương ứng với 2 trường có tên là title và imgage trong model
    class Meta: 
        model = Image 
        fields = ['title', 'image'] 