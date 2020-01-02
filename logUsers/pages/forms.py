from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
#from .models import Person

class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=150, required=True)

    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter First Name", 'class': 'form-control', 'required': 'true'})
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter Last Name", 'class': 'form-control', 'required': 'true'}),
    )
    email = forms.CharField(
        label="Email",
        widget=forms.TextInput(attrs={"placeholder": "Enter Email", 'class': 'form-control'}),
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={"placeholder": "Enter Username", 'class': 'form-control', 'required': 'true'}),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={"placeholder": "Enter Password", 'class': 'form-control', 'required': 'true'})
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput(attrs={"placeholder": "Enter Password Again", 'class': 'form-control', 'required': 'true'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    # def save(self, commit=True):
    #     #user = super(UserCreationForm, self).save(commit=False)
    #     user = super(UserCreationForm, self).save()
        # Person.objects.create(
        #     first_name=user.first_name,
        #     last_name=user.last_name,
        #     username=user.username,
        #     password=user.password,
        # )

class SignInForm(forms.ModelForm):
    # username = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100)

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={"placeholder": "Enter Username", 'class': 'form-control', 'required': 'true'}),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={"placeholder": "Enter Password", 'class': 'form-control', 'required': 'true'})
    )

    class Meta:
        model = User
        fields = ('username', 'password', )

class EditProfileForm(UserChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # self.fields['first_name'].value = user.first_name
        # self.fields['last_name'].value = user.last_name
        # self.fields['email'].value = user.email

        self.fields['first_name'].widget.attrs['placeholder'] = user.first_name
        self.fields['last_name'].widget.attrs['placeholder'] = user.last_name
        self.fields['email'].widget.attrs['placeholder'] = user.email

    first_name = forms.CharField(
        label="First Name",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        label="Last Name",
        # widget=forms.HiddenInput()
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.CharField(
        label="Email",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )
       #exclude = ()

#UserCreationForm creates a new USER, what if we just used Person and NOT the User model at all
#You can't do the above because in signup view function, the login() function requires a User model instance
#ultimately, if you want to sign up or login, you HAVE to use a User model object
# class SignUpForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100)
#
#     class Meta:
#          model = Person
#          fields = ('first_name', 'last_name', 'username', 'password', )

