from django import forms # type: ignore
from .models import *

class CompanyInChargeForm(forms.ModelForm):
    class Meta:
        model = CompanyInCharge
        fields = '__all__'  

class UniversityInChargeForm(forms.ModelForm):
    class Meta:
        model = UniversityInCharge
        fields = '__all__'  

class ConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = '__all__'

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'})
}
        
class ForgotForm(forms.ModelForm):
    class Meta:
        model = Forgot
        fields = ['email']
        
class VerifyForm(forms.ModelForm):
    class Meta:
        model = Verify
        fields = ['otp']
        
class Forgot2Form(forms.ModelForm):
    class Meta:
        model = Forgot2
        fields = '__all__'
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = new_user
        fields = ['firstname','lastname','phonenumber','country_code','email','password']
        
class NextForm(forms.ModelForm):
    class Meta:
        model = new_user
        fields = ['course','education','percentage','preferred_destination','start_date','mode_study','entrance','passport','country_code','phonenumber']
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = new_user
        fields =['email','password']