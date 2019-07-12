from django import forms
from .models import Groups, Users

LIST_OF_GROUPS = Groups.objects.values_list('id', 'name')

class UpdateUserForm(forms.Form):
    name = forms.CharField(max_length=20)
    group = forms.ChoiceField(choices=LIST_OF_GROUPS)

class CreateUserForm(forms.Form):
    name = forms.CharField(max_length=20)
    group = forms.ChoiceField(choices=LIST_OF_GROUPS)