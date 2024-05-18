from django.shortcuts import render, redirect
from .models import User,Book,Rental


def login(req):
    return render(req,"login.html")

def signup(req):
    return render(req,"signup.html")

def Home(req):
    return render(req,"Home.html")

def About(req):
    return render(req,"About.html")

def SignSave(req):
	obj=User()
	obj.user_name=req.POST.get('user')
	obj.name=req.POST.get('name')
	obj.email=req.POST.get('email')
	obj.phone=req.POST.get('phone')
	obj.password=req.POST.get('pass')
	obj.save()
	return redirect("/")

def CheckLog(req):
	user_n = req.POST.get('user_n')
	user_pass = req.POST.get('user_pass')
	userResult=User.objects.filter(user_name=user_n, password=user_pass)
	if(userResult):
		listData=userResult.values()
		uid=listData[0]['id']
		user_name = listData[0]['user_name']
		req.session['uid']=uid
		req.session['user_name']=user_name
		return render(req,"Home.html")
	else:
		return render(req,"login.html",{'Error':'Invalid User Name and Password'})



def BookRender(req):
    return render(req,"AddBook.html")

def AddBook(req):
	if 'uid' in req.session:
		uid=req.session['uid']
		obj=Book()
		obj.b_date=req.POST.get('b_date')
		obj.b_category=req.POST.get('b_category')
		obj.b_name=req.POST.get('b_name')
		obj.b_author=req.POST.get('b_author')
		obj.b_publish=req.POST.get('b_publish')
		obj.b_year=req.POST.get('b_year')
		obj.user_id=uid
		obj.save()
		return redirect('/BookRender')
	else:
		return render(req,'login.html')

def ShowBook(req):
	if 'uid' in req.session:
		uid=req.session['uid']
		record=Book.objects.filter(user_id=uid)
		if(record):
			listData=record.values()
			return render(req,"ShowBook.html",{'data':listData})
	else:
		return redirect('/')   







def RentRender(req):
    return render(req,"AddRent.html")

def AddRent(req):
	if 'uid' in req.session:
		uid=req.session['uid']
		obj=Rental()
		obj.r_date=req.POST.get('r_date')
		obj.r_time=req.POST.get('r_time')
		obj.rb_name=req.POST.get('rb_name')
		obj.person_name=req.POST.get('person_name')
		obj.return_date=req.POST.get('return_date')
		obj.submit=req.POST.get('submit')
		obj.user_id=uid
		obj.save()
		return redirect('/RentRender')
	else:
		return render(req,'login.html')

def ShowRent(req):
	if 'uid' in req.session:
		uid=req.session['uid']
		record=Rental.objects.filter(user_id=uid)
		if(record):
			listData=record.values()
			return render(req,"ShowRent.html",{'data':listData})
	else:
		return redirect('/')



def logout(req):
    del req.session['uid']
    del req.session['user_name']
    return redirect('/')