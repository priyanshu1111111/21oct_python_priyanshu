from .models import *
from django import forms
class SnippetSerializer(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = '__all__'

class CommentSerializer(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
