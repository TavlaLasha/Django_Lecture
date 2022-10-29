from django import forms


class TestForm(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not username:
            raise forms.ValidationError(('Username is required'), code='invalid')
        if not password:
            raise forms.ValidationError(('Password is required'))

        return super(TestForm, self).clean(*args, **kwargs)
