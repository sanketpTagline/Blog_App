from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Comments
from django.views.generic import TemplateView,CreateView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.conf import settings
from .forms import CommentForm

from django.urls import reverse_lazy


# Create your views here.
 
class HomeView(TemplateView):
    template_name = 'base.html'


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'
    paginate_by = settings.DEFAULT_PAGINATED_RECORDS
    
    # def get_context_data(self, **kwargs)  :
    #     context = super(BlogListView,self).get_context_data(**kwargs)
    #     context['blogs'] = context['blogs'].order_by("-post_date")
    #     return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by("-post_date")  # Reorder the queryset
        return queryset
    
# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'blog/blog_details.html'
#     context_object_name = 'blog'
    
#     def get_context_data(self, **kwargs):
#         context = super(BlogDetailView,self).get_context_data(**kwargs)
#         # context = self.queryset.get(pk=self.kwargs['pk'])
    
#         return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_details.html'
    context_object_name = 'blog'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddCommentView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name =  "blog/add_comment.html"
    # fields = '__all__'
    
    
    def form_valid(self, form):
        form.instance.blog_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('blog:home')
    
    
 

 
    
 
