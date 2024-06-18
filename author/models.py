from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image
        
class Author(models.Model):
     
    author_name = models.CharField(max_length=120)
    author_age = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(200)
        ]
    )
    author_email = models.EmailField()
    author_bio = models.TextField(default="") 
    author_profile_picture = models.ImageField(
       default='avatar.jpg',  
        upload_to='profile_avatars'  
    )
         
    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.author_profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.author_profile_picture.path)
            
    def __str__(self):
        return f"{self.author_name}"