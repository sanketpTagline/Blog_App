from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, UpdateView
from .models import Author
from django.core.paginator import Paginator
from .forms import AuthorSignupForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, views, logout
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404


# AuthorRegisterForm,


# Create your views here.
class BloggerListView(ListView):
    queryset = Author.objects.all()
    template_name = "author/all_bloggers.html"
    context_object_name = "authors"
    paginate_by = 10


class BloggerDetailView(DetailView):
    queryset = Author.objects.prefetch_related("blogs")
    template_name = "author/blogger_detail.html"
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_list = self.queryset.get(id=self.kwargs["pk"]).blogs.order_by("-post_date")

        # page_number = self.request.GET.get("page", 1)
        # page_size = self.request.GET.get("page_size", 3)
        # paginator = Paginator(blog_list, page_size)
        # page_obj = paginator.get_page(page_number)
        context["author_posts"] = blog_list
        return context


class AuthorSignupView(FormView):
    template_name = "author/register.html"
    form_class = AuthorSignupForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("blog:home")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("blog:blog_list")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(AuthorSignupView, self).form_valid(form)


class AuthorLogIn(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        else:
            return reverse_lazy("blog:blog_list")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class AuthorLogOut(View):
    def get(self, request):
        logout(request)
        messages.success(request, f"You have been logged out.")
        return redirect("author:login")
