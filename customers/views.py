from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from . models import Customer
from django.contrib import messages
def signout (request):
	logout(request)
	return redirect('home')
# Create your views here.

def show_account(request):
	
	if request.POST and 'register' in request.POST :
		c=True
		try:
			username=request.POST.get('username')
			password=request.POST.get('password')
			email=request.POST.get('email')
			phone=request.POST.get('phone')
			# create user objects
			user=User.objects.create_user(
				username=username,
				password = password,
				email=email
			)

			#create customer account
			customer=Customer.objects.create(
					user=user,
					phone=phone,
					address=address
				)
			success_messages="Successful"
			messages.success(request,success_messages)

		except Exception as e :
			error_messages="Duplicate username or Invalid Content"
			messages.error(request,error_messages)

	if request.POST and 'login' in request.POST :
		c=False
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user:
			login(request,user)
			return redirect('home')
		else:
			error_messages="Duplicate username or Invalid Content"
			messages.error(request,error_messages)

	return render(request,'account.html')