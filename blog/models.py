from django.db import models

from datetime import date
from django.utils.timezone import now
from author.models import Author
from django.contrib.auth.models import User
from django.conf import settings


class Blog(models.Model):
    title = models.TextField()
    content = models.TextField(default="")
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="blogs", default=""
    )

    def __str__(self):
        return f"{self.title}"


class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name="created_comments"
    )
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self):
    #     if len(self.comment) > settings.TRUNCATE_CHAR_LIMIT:
    #         return self.comment[:settings.TRUNCATE_CHAR_LIMIT] + "..."
    #     else:
    #         return self.comment
    # name = models.CharField(max_length=255)
    def __str__(self):
        return "%s" % (self.blog.title)
