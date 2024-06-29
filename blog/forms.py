from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "content", "publication_date")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez le titre ici",
                    "maxlength": "100",
                    "required": True,
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez le contenu ici",
                    "rows": 5,
                    "required": True,
                }
            ),
            "publication_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "YYYY-MM-DD",
                    "type": "date",
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise ValidationError("Le titre de votre article est trop court")
        elif title != title.lower():
            raise ValidationError(
                "Le titre de votre article ne doit contenir que des minuscules"
            )
        return title

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 10:
            raise ValidationError("Le contenu de votre article est trop court")
        return

    def clean_publication_date(self):
        publication_date = self.cleaned_data.get("publication_date")
        if publication_date > timezone.now():
            raise forms.ValidationError("Date de publication dans le futur")
        return publication_date
