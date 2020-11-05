from django import forms
from django.contrib.auth.forms import UsernameField

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        #super().__init__()...親クラスUserCreationFormの__init__を実行するの意味
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にする
        #self.fields['username'].widget.attrs['class'] = 'form-control'
        #self.fields['password1'].widget.attrs['class'] = 'form-control'
        #self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Password(confirmation)'})

    class Meta:#Meta情報
        model = User
        fields = ("username", "password1","password2")


class LoginForm(AuthenticationForm):
    '''form for login screen '''
    #username = UsernameField(
    #    label = 'User Name',
    #    max_length = 255,
    #)
    #password = forms.CharField(
    #    label = 'Password',
    #    strip = False,
    #    widget = forms.PasswordInput(render_value = True),
    #)
    def __initi__(self):
        #super().__init__()
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Password(confirmation)'})

    class Meta:
       model = User
       fields = ("username", "password1","password2")




from django.contrib.auth.forms import AuthenticationForm
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'
