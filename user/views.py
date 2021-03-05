from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import Usercreationform, UserUpdateform, ProfileupdateForm
from .models import Profile
from django.views.generic import DetailView
from news.models import Category, Post
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Usercreationform(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('login')
    else:
        form = Usercreationform()

    return render(request, 'users/register.html', {'form': form})


# def profile(request):
#     profile = Profile.objects.all()
#     latest = Post.objects.all().order_by('-created')[0:3]
#     categories = Category.objects.all()
#     context = { 'profile':profile, 'latest':latest, 'categories':categories}
#     return render(request, 'users/profile.html', context)


def p_update(request):
    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=request.user)
        p_form = ProfileupdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() & p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateform(instance=request.user)
        p_form = ProfileupdateForm(instance=request.user.profile)
        
    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'users/update_p.html', context)



def authors_list(request):
    profile = Profile.objects.all()
    categories = Category.objects.all()
    context = {'profile':profile, 'categories':categories}
    return render(request, 'users/authors.html', context )



# class Profileview(DetailView):
#       template_name = 'users/author-post-list.html'
#       model = Profile
#       context_object_name = 'profile'

#       def get_context_data(self, *args, **kwargs ):
#         cat_menu = Post.objects.all()
#         context = super(Profileview, self).get_context_data(*args, **kwargs )
#         # context['post'] = cat_menu
#         return context 


# def Profileview(request, id):
#     profile = get_object_or_404(Profile, id=id)
#     mypost = profile.post_authors.all()
#     latest = Post.objects.all().order_by('-created')[0:3]
#     categories = Category.objects.all()
#     context = { 'profile':profile, 'latest':latest, 'categories':categories, 'mypost':mypost}
#     return render(request, 'users/author-post-list.html', context)

      


def profile(request):
    latest = Post.objects.filter(status='Publish')
    categories = Category.objects.all()
    context = { 'profile':profile, 'latest':latest, 'categories':categories}
    return render(request, 'users/profile.html', context)