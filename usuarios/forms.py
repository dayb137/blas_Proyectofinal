from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class Registro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key:'' for key in fields}
        
class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    telefono = forms.IntegerField(required=False)
    avatar = forms.ImageField(required=False)
    
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name', 'avatar']
        
class NuevoPassword(PasswordChangeForm):
    old_password = forms.CharField(label='Password actual')
    new_password1= forms.CharField(label='Password nuevo')
    new_password2 = forms.CharField(label='Repetir Password')
    
   
    
    