from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        # fields = ("name", "comment")
        fields = ("comment",)
        # order_by = ("-date_added")

        widgets = {
            # "name": forms.TextInput(attrs={"class": "form-control"}),
            "comment": forms.Textarea(attrs={"class": "form-control"}),
        }
