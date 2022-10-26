from django import forms

class TestForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not username:
            raise forms.ValidationError('Username is required')
        if not password:
            raise forms.ValidationError('Username is required')

        return super(TestForm, self).clean(*args, **kwargs)
