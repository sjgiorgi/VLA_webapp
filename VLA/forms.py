from django import forms
from VLA.models import Laboratory, Course, UserProfile
from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the course name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Course

class LabForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the lab.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the lab.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Laboratory
        fields = ('title', 'url', 'views')
        
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data
    
class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")
    password_again = forms.CharField(help_text="Please re-enter your password.")
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_again']
        
class Help(forms.ModelForm):
    question = forms.CharField(max_length=200, help_text="Please enter a username.")
    #class Meta:
        #model =

#class UserProfileForm(forms.ModelForm):
#    website = forms.URLField(help_text="Please enter your website.", required=False)

#    class Meta:
#        model = UserProfile
#        fields = ['website', ]
    