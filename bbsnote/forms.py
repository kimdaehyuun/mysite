from django import forms
from django.forms import fields
from bbsnote.models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['subject', 'content']
