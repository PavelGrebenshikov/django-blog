from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Posts, Category, Comments
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
# Create your views here.


class PostsView(ListView):
    model = Posts
    context_object_name = "Posts"
    template_name = "home/index.html"
    ordering = ['-create_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        return {"Category": Category.objects.all(), "Posts": Posts.objects.all().order_by('-create_date')}

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
        post = get_object_or_404(Posts, pk=self.kwargs['pk'])
        return {"Posts": Posts.objects.filter(id=self.kwargs['pk']), "Comments": Comments.objects.filter(post=post)}

@login_required
def view_comment(request, pk):
    template_name = 'home/comment.html'
    post = get_object_or_404(Posts, pk=pk)
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = request.user
            form.post = post
            form.save()
            return HttpResponseRedirect(f"/home/post/{pk}/")
    else:
        form = CommentForm()
    return render(request, template_name, {"form": form})