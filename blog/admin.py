from django.contrib import admin

from .models import Blog,Comments 
 

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','post_date')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('blog','name','comment','date_added')

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comments,CommentsAdmin)
 

# Register your models here.
 