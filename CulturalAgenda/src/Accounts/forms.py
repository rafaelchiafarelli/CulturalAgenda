from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout


User = get_user_model()


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("Usu[ario ou senha incorretos")
			if not user.check_password(password):
				raise forms.ValidationError("Senha incorreta")
			if not user.is_active:
				raise forms.ValidationError("Usuario inativo")
			return super(UserLoginForm, self).clean(*args,**kwargs)
	def login(self, request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return user


class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label = 'Seu email')
	email2 = forms.EmailField(label = 'Confirme seu email')
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = [
				'username',				
				'password',
				'email',
				'email2',
		]
	def clean(self, *args, **kwargs):
		print(self.cleaned_data)
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Emails devem ser iguais")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Este email ja esta registrado")
		return super(UserRegisterForm,self).clean(*args,**kwargs)

	def clean_email(self):
		print(self.cleaned_data)
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Emails devem ser iguais")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Este email ja esta registrado")
		return email
		
	def register(self, request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return user