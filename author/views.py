from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, UpdateView
from .models import Author
from django.core.paginator import Paginator
from .forms import AuthorRegisterForm,AuthorSignupForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, views
from django.shortcuts import redirect



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
        blog_list = self.queryset.get(id = self.kwargs['pk']).blogs.order_by("-post_date")
        
        # page_number = self.request.GET.get("page", 1)
        # page_size = self.request.GET.get("page_size", 3)
        # paginator = Paginator(blog_list, page_size)
        # page_obj = paginator.get_page(page_number)
        context["author_posts"] = blog_list
        return context
    
class AuthorRegisterView(FormView):
    template_name = 'author/register.html'
    form_class = AuthorRegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('blog:home')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(AuthorRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog:home')
        return super(AuthorRegisterView, self).get(*args, **kwargs)

class AuthorSignupView(FormView):
    template_name = 'author/register.html'
    form_class = AuthorSignupForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("blog:home")
    
    print("hello")
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("blog:blog_list")
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(AuthorSignupView, self).form_valid(form)
    
