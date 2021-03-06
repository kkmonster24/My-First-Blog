from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
	obj_list = Post.objects.all().order_by("-timestamp")
	paginator = Paginator(obj_list, 10) # Show 25 contacts per page

	page = request.GET.get('page')
	objects = paginator.get_page(page)
	context={
		"objects" : objects
	}
	return render(request,"home.html",context)
# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully created")
		return redirect('/home/')
	context =	{
		"form" : form
	}
	return render(request,"create.html",context)

def post_list(request,id):


	instance=get_object_or_404(Post,id=id)
	context={
		"instance" : instance
	}
	return render(request,"blogDetail.html",context)

def post_update(request,id ):
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Updated")
		return redirect('/home/')

	context= {
		"instance":instance,
		"form":form
	}

	return render(request,"update.html",context)

def post_delete(request,id):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"Successfully Deleted")
	return redirect('/home/')

