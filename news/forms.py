from django import forms
from news.models import Category, News
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


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = [
        #     "title",
        #     "content",
        #     "author",
        #     "created_at",
        #     "image",
        #     "categories",
        # ]
        fields = "__all__"
        labels = {
            "title": _("Título"),
            "content": _("Conteúdo"),
            "author": _("Autoria"),
            "created_at": _("Criado em"),
            "image": _("URL da Imagem"),
            "categories": _("Categorias"),
        }
        widgets = {
            "created_at": forms.DateInput(attrs={"type": "date"}),
            "categories": forms.CheckboxSelectMultiple(),
            "image": forms.FileInput(),

        }
