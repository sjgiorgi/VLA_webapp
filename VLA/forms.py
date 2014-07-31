from django import forms
from django.contrib.auth.models import User

from VLA.models import Laboratory, Course, UserProfile

# Creates a User with usermane, email address, and password
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), help_text="Please enter a password.")
    #password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(), help_text="Please re-enter your password.")
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        #fields = ['username', 'email', 'password1', 'password2']
    
    # Check if password1 and password2 are equal
    #def clean_password2(self):
    #    password1 = self.cleaned_data.get('password1')
    #    password2 = self.cleaned_data.get('password2')

    #    if not password2:
    #        raise forms.ValidationError("You must confirm your password")
    #    if password1 != password2:
    #        raise forms.ValidationError("Your passwords do not match")
    #    return password1

# Creates a profile for the User with first name, last name, and TUid.
# This profile information is used when generating a Word Document to
# submit for an official Lab Report which is turned in to the TA.
class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, help_text="Please enter your first name.", required=True)
    last_name = forms.CharField(max_length=50, help_text="Please enter your last name.", required=True)
    TUid = forms.IntegerField(min_value=0, max_value=999999999, help_text="Please enter your TUid.", required=True)
    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'TUid' ]
    