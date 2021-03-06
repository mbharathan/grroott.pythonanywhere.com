from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FeedbackForm
from .models import Profile, Follow
from blog.models import Post
from django.contrib.auth.models import User

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login!')
			return redirect('login')
	else:	
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

@login_required
def edit_profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated sucessfully!')
			return redirect('user_profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		
		'u_form' : u_form,
		'p_form' : p_form
	}

	return render(request, 'users/edit_profile.html', context)

@login_required
def user_profile(request):
	context = {
	'posts' : Post.objects.filter(author=request.user).order_by('-date_posted')
	}
	return render(request, 'users/user_profile.html', context)


@login_required
def feedback(request):
	if request.method == "POST":
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
			subject = form.cleaned_data.get('subject')
			messages.success(request, f'Thanks for your feedback. Your Feedback has been recorded!')
			return redirect('blog-home')
	else:	
		form = FeedbackForm()
	return render(request, 'users/feedback.html', {'form':form})


def follow_profile(request):
	user = request.user
	if request.method == 'POST':
		profile_id = request.POST.get('profile_id')
		profile_obj = Profile.objects.get(id=profile_id)

		if user in profile_obj.followed.all():
			profile_obj.followed.remove(user)
		else:
			profile_obj.followed.add(user)

		follow, created = Follow.objects.get_or_create(user=user, profile_id=profile_id)

		if not created:
			if follow.follow_value == 'Follow':
				follow.follow_value = 'Following'
			else:
				follow.follow_value = 'Follow'

		follow.save()
	return redirect(request.META.get('HTTP_REFERER', 'profile'))