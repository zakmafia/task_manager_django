from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Order, Task

class OrderForm(ModelForm):
    images = forms.ImageField()
    class Meta:
        model = Order
        fields = ['name', 'images']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter the Order Name'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'order')
        labels = {
            'name': '',
            'order': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Task'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
        }
