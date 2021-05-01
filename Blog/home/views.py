from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Posts, Category, Comments
from .forms import CommentForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
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

@login_required
@require_http_methods("POST")
def view_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/")
    else:
        form = CommentForm()
    return render(request, 'home/comment.html', {"form": form})