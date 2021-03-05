from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.db.models import  Q
from user.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category, Comment, Subscribe
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import ListView, DetailView, TemplateView, View, CreateView, UpdateView, DeleteView
from .forms import Contacform, Commentform, subform
# Create your views here.


def homeview(request):
	categories = Category.objects.all() 
	editors_pick = Post.objects.filter(status='Publish')[0:2]
	latest = Post.objects.filter(status='Publish')[0:2]
	month = Post.objects.filter(status='Publish')[0:3]

	if request.method == 'POST':
		email = request.POST.get("email")
		subscribed = Subscribe.objects.create(email=email)
		subscribed.save()
		messages.success(request, 'your Subscribtion has been Recieved')



	context = { 'categories':categories, 'editors_pick':editors_pick, 'latest':latest, 'month': month}
	return render(request, 'news/home.html', context )




def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	categories = Category.objects.all()
	editors_pick = Post.objects.filter(status='Publish')[0:2]
	latest = Post.objects.filter(status='Publish')[0:3]

	new_comment = None
	if request.method == 'POST':
		comment_form = Commentform(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = Commentform()

	context = { 'categories':categories, 'editors_pick':editors_pick, 'latest':latest, 'new_comment': new_comment,
		'form': comment_form, 'post': post}
	return render(request, 'news/post_single.html', context )





def cat_view(request, slug):
	cat = get_object_or_404(Category, slug=slug)
	post = Post.objects.filter(status='Publish')
	categories = Category.objects.all()

   

	context = { 'cat':cat,'post': post, 'categories':categories}
	return render(request, 'news/category.html', context )




class AddPost(LoginRequiredMixin,  CreateView):
	model = Post
	fields = ['title', 'category', 'body', 'image', 'status']

	def form_valid(self, form, *args, **kwargs):
		form.instance.author = self.request.user.profile
		return super().form_valid(form, *args, **kwargs)

	template_name = 'news/addpost.html'


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'category', 'body', 'image', 'status']

	def form_valid(self, form):
		form.instance.author = self.request.user.profile
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user.profile == post.author:
			return True
		return False

	template_name = 'news/addpost.html'


def search(request):
	categories = Category.objects.all()
	latest = Post.objects.filter(status='Publish')[0:3]
	queryset = Post.objects.filter(status='Publish')
	query = request.GET.get('q')
	if query:
		queryset = queryset.filter(
			Q(title__icontains=query) | Q(body__icontains=query)

		).distinct()
	context = {'queryset': queryset, 'categories':categories, 'latest': latest}

	return render(request, 'news/search.html', context)



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'



	def test_func(self):
		post = self.get_object()
		if self.request.user.profile == post.author:
			return True
		return False




# class UserPostListView(ListView):
#     model = Post
#     template_name = 'users/author-post-list.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'mypost'
#     paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.objects.filter(author=Profile.post_authors).order_by('-modified')




# def profile(request):
#     latest = Post.objects.all().order_by('-created')[0:3]
#     categories = Category.objects.all()
#     Post.objects.filter(author=Profile.post_authors).order_by('-modified')
#     context = { 'profile':profile, 'latest':latest, 'categories':categories}
#     return render(request, 'users/profile.html', context)


def userpage(request, id):
	profile = get_object_or_404(Profile, pk=id)
	latest = Post.objects.filter(status='Publish')[0:3]
	categories = Category.objects.all()
	context = { 'profile':profile, 'latest':latest, 'categories':categories}
	return render(request, 'users/author-post-list.html', context)



def contact(request):
	categories = Category.objects.all()
	if request.method == 'POST':
		form = Contacform(data=request.POST)
		if form.is_valid():
			form.save()
			name = f' message from name: {form.cleaned_data["name"]} phone: {form.cleaned_data["phone"]}'
			subject = form.cleaned_data["subject"]
			msg = form.cleaned_data["message"]
			sender = form.cleaned_data["email"]
			
			send_mail( subject, msg, sender, ['palmsj102@gmail.com'] )
			messages.success(request, f' Your message Has been Sent We WIll get back to As Soon as Possible')
			return redirect('/')

	else:
		form = Contacform()

	return render(request, 'news/contact.html', {'form':form,'categories':categories})


# def subscribe(request):
#     pass
