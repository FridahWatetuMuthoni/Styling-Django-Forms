from django import forms
from django.utils.html import format_html
from .models import Post

"""
This works i just didnt need it again
class CustomClearableFileInput(forms.ClearableFileInput):
    def render(self, name, value, attrs= None, renderer=None):
        html = super().render(name,value,attrs,renderer)
        label = format_html('<label for="{}" class="image-label">Choose An Image</label>',attrs['id'])
        return format_html('{}{}',label,html)
"""

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','body','image']
        widgets ={
            'title': forms.TextInput(attrs={'class':'inputs'}),
            'description': forms.TextInput(attrs={'class':'inputs'}),
            'body':forms.Textarea(attrs={'class':'textarea'}),
            #'image':CustomClearableFileInput(attrs={'class':'image-upload'})
            'image':forms.ClearableFileInput(attrs={'class':'image-upload'})
        }
        labels = {
            'image':''
        }
