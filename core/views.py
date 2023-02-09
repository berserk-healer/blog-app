from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, CommentForm, PostEditForm


# Create your views here.
class PostList(generic.ListView):

    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5


def post_detail(request, pk):

    template_name = 'post_detail.html'
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.all()
    new_comment = None


    # Create post_detail view
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user
            new_comment.save()
            return redirect('/post/{}'.format(pk))
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form,
                                            })


class PostCreate(LoginRequiredMixin, generic.edit.CreateView):

    login_url = '/accounts/login/'
    form_class = PostForm
    template_name = 'post_create.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Successful!')
            return redirect(f'/post/{new_post.id}')
        return render(request, self.template_name, {'form': form})


class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.edit.UpdateView):

    login_url = '/accounts/login/'
    template_name = 'post_edit.html'
    success_message = 'Post updated successfully!'

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        form = PostEditForm(instance=post)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        form = PostEditForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/post/{pk}')
        return render(request, self.template_name, {'form': form})
            



class PostDelete(LoginRequiredMixin, SuccessMessageMixin, generic.edit.DeleteView):

    login_url = '/accounts/login/'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    success_message = 'Deleted successfully!'


class SearchResultsView(generic.ListView):
    
    model = Post
    template_name = 'search_result.html'
    paginate_by = 7
    
    def get_queryset(self):
        query = self.request.GET['search']
        post_list = Post.objects.filter(title__icontains=query)

        return post_list