from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "author_name",
        "author_age",
        "author_email",
        "author_profile_picture",
        "author_bio",
    )


admin.site.register(Author, AuthorAdmin)
# Register your models here.
