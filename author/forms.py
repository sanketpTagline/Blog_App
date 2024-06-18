from django.contrib.auth.forms  import UserCreationForm
from .models import Author

class AuthorRegisterForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ('author_user_name','author_bio')