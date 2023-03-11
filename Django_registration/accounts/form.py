from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,patient,doctor

class patientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    profile_picture=forms.ImageField(required=False)
    email_id=forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = patient.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.location=self.cleaned_data.get('location')
        customer.email_id=self.cleaned_data.get('email_id')
        customer.profile_picture=self.cleaned_data.get('profile_picture')
        customer.save()
        return user

class doctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    profile_picture=forms.ImageField(required=False)
    email_id=forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = doctor.objects.create(user=user)
        employee.phone_number=self.cleaned_data.get('phone_number')
        employee.location=self.cleaned_data.get('location')
        employee.email_id=self.cleaned_data.get('email_id')
        employee.profile_picture=self.cleaned_data.get('profile_picture')
        employee.save()
        return user
