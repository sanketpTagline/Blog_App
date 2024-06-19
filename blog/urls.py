from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, HomeView, AddCommentView

app_name = "blog"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("blogs/", views.BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path(
        "blog/<int:pk>/add_comments", views.AddCommentView.as_view(), name="add_comment"
    ),
]
