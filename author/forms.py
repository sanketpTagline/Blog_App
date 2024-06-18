from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User

from .models import Author

class AuthorRegisterForm(UserCreationForm):
    class Meta:
        model = Author
        # fields = ('author_email','author_bio')
        fields = "__all__"
        
class AuthorSignupForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for visible  in self.visible_fields():
            visible.field.widget.attrs['class'] = "input"
            
    class Meta:
        model = User
        fields = ["username",'password1','password2']