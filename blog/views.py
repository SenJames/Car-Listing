from django.shortcuts import render
from listing_app import templates
from blog.models import *
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.http import HttpResponseRedirect
# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'blog_post'
    template_name='listing_app/blog.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        most_recent = Post.objects.order_by('-created_date')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post_det'
    template_name='listing_app/blog-detail.html'
    
    def get_context_data(self, **kwargs):
        most_recent = Post.objects.order_by('-created_date')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        return context


def Postlist(request):
    blog_post = Post.objects.all()
    most_recent = Post.objects.order_by('-created_date')[:3]


    context = {
        'blog_post': blog_post,
        'most_recent': most_recent
    }
    return render(request, 'listing_app/blog.html', context)
    
    



