from django import forms
from django import forms
from django.db import models
from .models import Comment
from django.contrib.auth.models import User


class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('comment',)
