from django import forms


class TestForm(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Input Username'}))
    age = forms.CharField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Input Age'}))


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        age = self.cleaned_data.get('age')

        if not username:
            raise forms.ValidationError(('Username is required'), code='invalid')
        if not age:
            raise forms.ValidationError(('Age is required'))

        return super(TestForm, self).clean(*args, **kwargs)
