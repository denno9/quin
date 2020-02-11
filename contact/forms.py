from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm,TextInput,Textarea,EmailInput,NumberInput

from .models import Contact
class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
   

    class Meta:

        model=Contact
        

        fields = ('__all__')
        
    
        widgets = {
            'fullname':TextInput(),
            'email' : EmailInput(),
            'subject' :TextInput(),
            'body'  : Textarea(),
        }
        labels = {
        "fullname": "Name*",
        "email":"email*",
        "Subject":"subject*",
        "body":"body*"
        }
