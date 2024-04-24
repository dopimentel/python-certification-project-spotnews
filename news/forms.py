import datetime
from django import forms
from news.models import Category, News
from django.utils.translation import gettext_lazy as _


class CreateCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        labels = {"name": _("Nome")}


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
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
            "created_at": forms.DateInput(
                attrs={"type": "date", "value": datetime.date.today()}
            ),
            "categories": forms.CheckboxSelectMultiple(),
        }
