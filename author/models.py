from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image


# Create your models here.
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):  
#         """  
#         Create and save a User with the given email and password.  
#         """  
#         if not email:  
#             raise ValueError(('The Email must be set'))  
#         email = self.normalize_email(email)  
          
#         user = self.model(email=email, **extra_fields)  
#         user.set_password(password)  
#         user.save()  
#         return user  
    
#     # def create_user(self, username, password=None, **extra_fields):
#     #     user = self.model(username=username, **extra_fields)
#     #     user.set_password(password)
#     #     user.save()
#     #     return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         user = self.create_user(username=username, password=password, **extra_fields)
#         user.is_admin = True
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):  
#         """  
#         Create and save a SuperUser with the given email and password.  
#         """  
#         extra_fields.setdefault('is_staff', True)  
#         extra_fields.setdefault('is_superuser', True)  
#         extra_fields.setdefault('is_active', True)  
  
#         if extra_fields.get('is_staff') is not True:  
#             raise ValueError(('Superuser must have is_staff=True.'))  
#         if extra_fields.get('is_superuser') is not True:  
#             raise ValueError(('Superuser must have is_superuser=True.'))  
#         return self.create_user(email, password, **extra_fields)  
      
#     def get_full_name(self):  
#         '''  
#         Returns the first_name plus the last_name, with a space in between.  
#         '''  
#         full_name = '%s %s' % (self.first_name, self.last_name)  
#         return full_name.strip()  
  
#     def get_short_name(self):  
#         '''  
#         Returns the short name for the user.  
#         '''  
#         return self.first_name   
   
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(author_user_name=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(author_user_name=username, password=password, **extra_fields)
        user.is_admin = True
        user.save()
        return user    
    
class Author(AbstractBaseUser):
    author_user_name = models.CharField(max_length=50,blank=True)
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
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    
    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.author_profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.author_profile_picture.path)
            
    # def __str__(self):
    #     return f"{self.author_name}"

# from typing import Any

# # Create your models here.



# class Author(AbstractBaseUser):
#     username = models.CharField(max_length=50, unique=True)
#     bio_detail = models.TextField()







