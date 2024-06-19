from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Comments
from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.urls.base import reverse
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Author
from django.http.response import Http404
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    template_name = "blog/blog_list.html"
    paginate_by = settings.DEFAULT_PAGINATED_RECORDS

    # def get_context_data(self, **kwargs)  :
    #     context = super(BlogListView,self).get_context_data(**kwargs)
    #     context['blogs'] = context['blogs'].order_by("-post_date")
    #     return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by("-post_date")  # Reorder the queryset
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_details.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddCommentView(LoginRequiredMixin, CreateView):
    template_name = "blog/add_comment.html"
    model = Comments
    # form_class = CommentForm
    fields = [
        "comment",
    ]
    # fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(AddCommentView, self).get_context_data(**kwargs)
        context["post"] = Blog.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        post = Blog.objects.get(id=self.kwargs["pk"])
        new_comment.name = self.request.user
        new_comment.blog = post
        new_comment.save(force_insert=True)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "blog:blog_detail",
            kwargs={
                "pk": self.kwargs["pk"],
            },
        )

    # success_url = reverse_lazy("blog:home")
