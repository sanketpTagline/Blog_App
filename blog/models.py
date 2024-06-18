from django.db import models
 
from datetime import date
from django.utils.timezone import now
from author.models import Author
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.TextField()
    content =  models.TextField(default='')
    post_date = models.DateTimeField(auto_now_add=True)
    author =   models.ForeignKey(Author,on_delete=models.CASCADE,related_name="blogs",default='')
    
    def __str__(self):
        return f"{self.title}"
    

class Comments(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=255)
    comment =  models.TextField()
    date_added = models.DateTimeField(auto_now_add=True,null=True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE,default=None,related_name="created_comments")
    
    def __str__(self):
        return  '%s - %s' %(self.blog.title,self.name)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
 
# Create your models here.

# class Author(models.Model):
    # author_name = models.CharField(max_length=120)
    # author_age = models.IntegerField(
    #     validators=[
    #         MinValueValidator(1),
    #         MaxValueValidator(200)
    #     ]
    # )
    # author_email = models.EmailField()
    # author_profile_picture = models.ImageField(
    #    default='avatar.jpg',  
    #     upload_to='profile_avatars'  
    # )
    
    # def save(self, *args, **kwargs):
    #     # save the profile first
    #     super().save(*args, **kwargs)

    #     # resize the image
    #     img = Image.open(self.author_profile_picture.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.author_profile_picture.path)
            
    # def __str__(self):
    #     return f"{self.author_name}"