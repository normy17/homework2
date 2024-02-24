from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error('password', "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class ThreeNumbersForm(forms.Form):
    number1 = forms.CharField(
        label='Число 1',
        widget=forms.TextInput()
    )

    number2 = forms.CharField(
        label='Число 2',
        widget=forms.TextInput()
    )

    number3 = forms.CharField(
        label='Число 3',
        widget=forms.TextInput()
    )

    choice = forms.ChoiceField(
        label='Что нужно найти?',
        widget=forms.RadioSelect,
        choices=[
            ('max', 'Максимальное из трёх'),
            ('min', 'Минимальное из трёх'),
            ('avg', 'Среднеарифметическое из трёх')
        ]
    )


class RegForm(forms.Form):
    name = forms.CharField()
    second_name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[
            ('male', 'male'),
            ('female', 'female')
        ]
    )
    address = forms.CharField()
    subscribe = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices={
            'subscribe': 'Хотите ли подписаться на новости нашего интернет-магазина?'
        }
    )


class YearForm(forms.Form):
    year = forms.CharField(
        label='Введите год',
        widget=forms.TextInput()
    )