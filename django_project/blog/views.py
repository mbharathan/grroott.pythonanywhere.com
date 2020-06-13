from django.shortcuts import render
from django.http import HttpResponse

posts = [

{
	'author' : 'Groot1',
	'title' : 'Post 1',
	'content' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
	'date_posted': 'June 13, 2020'
},

{
	'author' : 'Groot2',
	'title' : 'Post 2',
	'content' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
	'date_posted': 'June 14, 2020'
}

	]
	
def home(request):
	context = {
	'posts' : posts
	}
	return render(request, 'blog/home.html', context)
def about(request):
	return render(request, 'blog/about.html', {'title':'About'})