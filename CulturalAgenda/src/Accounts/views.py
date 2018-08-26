from django.contrib.auth import authenticate, get_user_model, login, logout

from django.shortcuts import render, redirect


from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if request.POST and form.is_valid():
		print("load the user from the form!")
		user = form.login(request)
		print("user is loaded")
		if user:
			print("try tolog in!")
			login(request, user)
			print("logged in!")
			if next:
				return redirect(next)
			return redirect("/")
	print("not logged in!")
	return render(request,"loggin.html",{'form':form})


    
        

def register_view(request):
	form = UserRegisterForm(request.POST or None)
	print("is the form valid")
	if request.POST and form.is_valid():
		print("the form is valid")
		user = form.save(commit=False)
		if user:
			print("is the user VALID")	
			print(user.password)
			print(user.email)
			print(user.username)
			password = form.cleaned_data.get('password')
			user.set_password(password)
			print('save user data')
			user.save()
			user = form.login(request)
			
			print("then try to login")
			login(request, new_user)
			print("logged in!")
		#login(request,user)
	context = {
	"form":form,
	}
	return render(request,"register_form.html",context)


def logout_view(request):
	logout(request)
	#redirect
	return render(request,"logout.html",{})	