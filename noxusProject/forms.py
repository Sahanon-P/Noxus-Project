from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from noxusProject.models import *
from django.http import request

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class BuildForm(forms.ModelForm):
    class Meta:
       model = Build
       fields = ['build_name', 'champion','starter1','starter2',
    'items_1',
    'items_2',
    'items_3',
    'items_4',
    'items_5',
    'items_6',
    'spell1',
    'spell2',
    'key_stone', 
    'row1',
    'row2',
    'row3',
    'sub_row1',
    'sub_row2',
    ]

    def __init__(self, *args, **kwargs):
        super(BuildForm, self).__init__(*args, **kwargs)
        self.fields['row1'].queryset = SubRune.objects.filter(row=1)
        self.fields['row2'].queryset = SubRune.objects.filter(row=2)
        self.fields['row3'].queryset = SubRune.objects.filter(row=3)

       
