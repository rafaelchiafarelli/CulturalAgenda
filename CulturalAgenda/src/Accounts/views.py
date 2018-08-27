from django.contrib.auth import authenticate, get_user_model, login, logout

from django.shortcuts import render, redirect


from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
def login_form(request):
	next = request.GET.get('next')
	print('loggin module')
	form = UserLoginForm(request.POST or None)
	return form

def login_view(request):
	next = request.GET.get('next')
	print('loggin module')
	print(request)
	form = UserLoginForm(request.POST or None)
	print(form)
	if request.POST and form.is_valid():
		user = form.login(request)
		if user:
			login(request, user)
			if next:
				return redirect(next)
			return redirect("/")
	return render(request,"loggin.html",{'loggin_form':form})

def register_view(request):
	form = UserRegisterForm(request.POST or None)
	if request.POST and form.is_valid():
		user = form.save(commit=False)
		if user:
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			user = authenticate(username=user.username, password=password)
			login(request, new_user)
		#login(request,user)
	context = {
	"loggin_form":form,
	}
	return render(request,"register_form.html",context)


def logout_view(request):
	logout(request)
	#redirect
	return render(request,"logout.html",{})	