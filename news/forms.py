from django import forms
from news.models import Category
from django.utils.translation import gettext_lazy as _


class CreateCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        labels = {"name": _("Nome")}
        # help_texts = {
        #     'name': 'Enter the name of the category'
        # }
        # error_messages = {
        #     'name': {
        #         'required': 'The name field is required'
        #     }
        # }
        # widgets = {"name": forms.TextInput(attrs={"for": "id_name"})}
