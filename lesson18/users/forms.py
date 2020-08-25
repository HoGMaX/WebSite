from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class RegisterForm(UserCreationForm):

    username = forms.CharField(label='Имя',required=True,
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Введите имя"})
    )
    email = forms.EmailField(label='email',required=True,
         widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Введите е-mail"})
    )
    password1 = forms.CharField(label='пароль',required=True,
        help_text='Пароль не должен быть менее чем из 8 символов',
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    password2 = forms.CharField(label='повтор пароля',required=True,
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )


    class Meta():
        model = User
        fields = ['username','email','password1','password2']

class UpdateForm(forms.ModelForm):
    username = forms.CharField(label='Имя',required=True,
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Введите имя"})
    )
    email = forms.EmailField(label='email',required=True,
         widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Введите е-mail"})
    )

    class Meta():
        model = User
        fields = ['username','email']

class UpdateUserIcon(forms.ModelForm):

    img = forms.ImageField(
        label = 'Загрузить аватар',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']
class UpdateGender(forms.ModelForm):
    Gender = [
    ('m','мужской'),
    ('w','женский'),
    ('o','нет'),
    ]
    agreement = forms.BooleanField(required=False,label = 'Соглашение на отправку уведомлений на почту',widget=forms.CheckboxInput())
    gender_choise = forms.ChoiceField(label='Пол:',choices = Gender,required=True)
    class Meta():
        model = Profile
        fields = ['gender_choise','agreement']
