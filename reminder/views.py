from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Checklist

# def index(request):
#     return HttpResponse("Hello, world. You're at the reminder index.")


def signin(request):
	# user = request.user
	# return HttpResponse(str(request.user))

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
		return redirect('/checklist')


	return render(request,"login.html")

def logout_view(request):
	logout(request)
	return HttpResponse("Logged out succesfully!")

def signup(request):
	if request.method == "POST":
		username = request.POST['username']
		# username = request.POST.get('username', None)
		email = request.POST['Email']
		# email = request.POST.get("email")
		password = request.POST['password']
		# password = request.POST.get("password")
		try:
			user =  User.objects.get(username=username)
		except:
			user = None
		if user is None:
			User.objects.create_user(username, email, password)
			return redirect('/main')
		else:
			return HttpResponse("username already exists!")
		
	return render(request,"signup.html")

def home(request):
	
	if request.method == "POST":
		name = request.POST.get(name=name)
		time = request.POST['time']
		day = request.POST['day']

	return render(request,"home.html")


def main(request):
	if request.method == "POST":
		name=request.POST.get('name')
		print(name)
		time=request.POST.get('time')
		print(time)
		day=request.POST.get('day')
		print(day)
		Checklist.objects.create(name=name,time=time,day=day,user=request.user)
		# checklist.save()
		return redirect('/checklist')
	return render(request,"main.html")

def checklist(request):
	checklists = Checklist.objects.filter(user=request.user)
	# print(checklists)
	return render(request,"checklist.html",{'checklists': checklists})

def my_checklist(request,check_id):
	myrem = Checklist.objects.get(pk=check_id)
	return render(request, "my_checklist.html", {'checklist':myrem})


def checklist_edit(request, pk):
	checklist = get_object_or_404(Checklist, pk=pk)
	print(type(checklist))
	
	if request.method == "POST":
		checklist = get_object_or_404(Checklist, pk=pk)
		name=request.POST.get('name')
		print(name)
		time=request.POST.get('time')
		print(time)
		day = request.POST.get('day')
		print(day)
		checklist.name=name
		checklist.time=time
		checklist.day=day 
		checklist.save()
		return redirect('/checklist')   
	# checklists = Checklist.objects.all()
	return render(request,"edit.html",{'checklist': checklist})

def delete(request,id):
	obj=Checklist.objects.get(pk=id)
	obj.delete()
	checklists = Checklist.objects.all()
	return redirect("/checklist")
	return render(request,"checklist.html",{'checklists': checklists})

def new(request):
	if request.method == "POST":
		name=request.POST.get('name')
		time=request.POST.get('time')
		day=request.POST.get('day')
		checklist = Checklist(name=name,time=time,day=day,user=request.user)
		checklist.save()
		return redirect('checklist.html', pk=checklist.pk)
	
	return render(request, 'main.html')

