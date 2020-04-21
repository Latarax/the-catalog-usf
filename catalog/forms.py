from django import forms 
    
class RegisterForm(forms.Form): 
    first_name = forms.CharField(max_length = 100) 
    last_name = forms.CharField(max_length = 100)
    city = forms.CharField(max_length=100) 
    user_name = forms.CharField(max_length=100) 
    password = forms.CharField(widget = forms.PasswordInput())

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=100) 
    password = forms.CharField(widget = forms.PasswordInput())