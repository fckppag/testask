from .models import Post
from django.forms import ModelForm, Textarea, TextInput, CheckboxInput, Select


class CreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["author","title", "body", "chek"]
        widgets = {
            "author": Select(attrs={
                'class': "form-select",
                'aria-label': "Default select example",
            }),
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Введите название"
            }),
            "body": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Введите описание"
            }),
            'chek': CheckboxInput(attrs={
                'class':"form-check-input",
                'id':"flexCheckChecked",
            })
        }

