from . models import Image,Profile
from django import forms

class PostImage(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['likes','comments','date','user','userId',]
class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile
        
