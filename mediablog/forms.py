from django import forms
from django.contrib.auth.models import User
from mediablog.models import MediaBlog,Comment
from ckeditor.widgets import CKEditorWidget
class MediaForm(forms.ModelForm):
    description = forms.CharField(label="Description" ,widget=CKEditorWidget())
    title = forms.CharField(label="Title ",required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Title",
    }))
    link = forms.CharField(label="Link ",required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Link",
    }))
    class Meta:
        model = MediaBlog
        fields = ['title','link','description']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="",widget=forms.Textarea(attrs={
        'class':'form-control',
        'id':'comm',
        'rows':3,
        'cols':40,
        'padding':'10px',
        'placeholder':"Enter  your Text here",
    }))
    class Meta:
        model = Comment
        fields = ['content']



