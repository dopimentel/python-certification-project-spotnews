from django import forms
from .models import Category


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        # labels = {"name": "Nome"}
        # help_texts = {
        #     'name': 'Enter the name of the category'
        # }
        # error_messages = {
        #     'name': {
        #         'required': 'The name field is required'
        #     }
        # }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'})
        # }
