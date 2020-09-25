# from django import forms
# class StudentForm(forms.Form):
#     firstname = forms.CharField(label="Enter first name", max_length=50)
#     lastname = forms.CharField(label="Enter last name", max_length = 10)
#     email = forms.EmailField(label="Enter Email")
#     file = forms.FileField(upload_to='file/', blank=True, null=True) # for creating


from django import forms
from django.forms import ClearableFileInput
from .models import UploadPdf
class ResumeUpload(forms.ModelForm):

    firstname = forms.CharField(label="Enter first name", max_length=50)
    email = forms.EmailField(label="Enter email")

    class Meta:
        model = UploadPdf
        fields = ['resumes']
        widgets = {
            'resumes': ClearableFileInput(attrs={'multiple': True}),
        }