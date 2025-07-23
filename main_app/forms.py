from django import forms
from .models import Task
from .models import Selecting
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SelectingForm(forms.ModelForm):
    class Meta:
        model = Selecting
        fields = ['date', 'choice']
        
            
        


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(format=('%Y-%m-%d'),attrs={'placeholders': 'Select a date', 'type' : 'date'}),
        }
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')        