from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from accounts.models import Hospitals, Doctor, Comments, Departments, Prescription
from django.urls import reverse_lazy

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',

        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)


class UserRegisterForm2(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',

        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm2, self).clean(*args, **kwargs)


class UserForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email address')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if not email_qs.exists():
            raise forms.ValidationError("This email is not registered")
        return super(UserForgotPasswordForm, self).clean(*args, **kwargs)


class HospitalsForm(forms.ModelForm):
    class Meta:
        model = Hospitals
        fields = [
            'name',
            'province',
            'district',
            'phone',
            'numBeds',
            'numRooms'
        ]


class DoctorForm(forms.ModelForm):
    email2 = forms.EmailField()

    class Meta:
        model = Doctor
        fields = [
            'name',
            'title',
            'email',
            'email2',
            'gsm',
            'address',
            'department',
            'hospital',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = Doctor.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(DoctorForm, self).clean(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'patient',
            'doctor',
            'message'
        ]


class SendPrescriptionForm(forms.ModelForm):
    presc = Prescription.objects.order_by('id').last()

    class Meta:
        model = Prescription
        fields = [
            'patientName',
            'diagnosis',
            'recipe'
        ]
        success_url = reverse_lazy('git_presc:index')
