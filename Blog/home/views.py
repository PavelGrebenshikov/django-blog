from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts, Category, Comments
# Create your views here.


class PostsView(ListView):
    model = Posts
    context_object_name = "Posts"
    template_name = "home/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {"Category": Category.objects.all(), "Posts": Posts.objects.all()}

class PostsDetail(ListView):
    model = Posts
    context_object_name = "PostsDetail"
    template_name = "home/post_page.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {"Category": Category.objects.all(),
         "PostsDetail": Posts.objects.filter(category_post__slug=self.kwargs['slug'])}

class PostsID(ListView):
    model = Posts
    context_object_name = "Posts"
    template_name = "home/post.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {"Posts": Posts.objects.filter(id=self.kwargs['pk']), "Comments": Comments.objects.all()}