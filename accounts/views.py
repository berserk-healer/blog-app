from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm
from core.models import Post
from .models import CustomUser



class SignUpView(generic.CreateView):

    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(email=new_user.email, password=request.POST['password1'])
            login(request, authenticated_user)
            messages.success(request, 'Registration successful!')
            return redirect(reverse_lazy('home'))
        return render(request, self.template_name, {'form': form})


def user_index(request, pk):

    template_name = 'user_index.html'
    current_user = CustomUser.objects.get(id=pk)
    post_list = Post.objects.filter(author=current_user)
    paginator = Paginator(post_list, 7)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user != current_user:
        return redirect(reverse_lazy('home'))

    return render(request, template_name, {'post_list': post_list, 'user': current_user, 'page_obj': page_obj})
    
    
class UserProfileEdit(SuccessMessageMixin, generic.edit.UpdateView):

    model = CustomUser
    template_name = 'user_profile.html'
    fields = ['username', 'email', 'first_name', 'last_name', 'age', 'country','description', 'profile_image']
    success_message = 'Profile updated successfully!'
    