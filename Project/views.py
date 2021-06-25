from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .db_operations import *
from django.http import Http404


def Signup_student(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['PhoneNumber']
        password = request.POST['password']
        groupid = request.POST['groupname']
        print(groupid)
        check = check_name(name=name)
        emailcheck = check_email(email=email)
        number_check = check_number(number=number)
        if check == True:
            messages.info(request, 'Username is taken')
            return redirect("/signup_student")

        if emailcheck == True:
            messages.info(request, 'Email is used by another account')
            return redirect("/signup_student")

        if number_check == True:
            messages.info(request, 'Phone Number is used by another account')
            return redirect("/signup_student")

        else:
            register_student(name=name, password=password,
                             email=email, number=number, groupid=groupid)
            return HttpResponseRedirect("/login_student")

    else:
        groupnames = group_name()
        return render(request, 'SignupSt.html', context={"gn": groupnames})


def signup_group(request, groupname):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['PhoneNumber']
        password = request.POST['password']
        check = check_name(name=name)
        emailcheck = check_email(email=email)
        number_check = check_number(number=number)
        if check == True:
            messages.info(request, 'Username is taken')
            return redirect("/signup_student")

        if emailcheck == True:
            messages.info(request, 'Email is used by another account')
            return redirect("/signup_student")

        if number_check == True:
            messages.info(request, 'Phone Number is used by another account')
            return redirect("/signup_student")

        else:
            register_student(name=name, password=password,
                             email=email, number=number, groupid=groupname)
            return HttpResponseRedirect("/login_student")

    else:
        return render(request, 'signup_group.html')


def admin_login(request):
    groupnames = group_name()
    groupdesc = group_desc()
    groupid = group_id()
    grouptime = group_time()
    groupday = group_day()
    return render(request, 'admin_login.html', context={"gn": groupnames, "gd": groupdesc, "gi": groupid, "gt": grouptime, "gday": groupday})


def admin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm = login_teacher(password=password, email=email)
        if confirm == True:
            return HttpResponseRedirect("/admin_login")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect("/admin")
    else:
        return render(request, 'admin.html')


def group_list(request):
    if request.method == 'POST':
        groupname = request.POST['group']
        return redirect('student_list', groupname)
    else:
        groups = group_name()
        return render(request, 'group_list.html', context={"gn": groups})


def student_list(request, groupname):
    if request.method == 'POST':
        gid = request.POST.getlist('groupid')
        print(gid)
        return HttpResponseRedirect('/student_list')
    else:
        print(groupname)
        students = get_students_from_group(groupname)
        print(students)
        return render(request, 'student_list.html', context={"sl": students})


def creategrp(request):
    if 'user' in request.session:
        if request.method == "POST":
            name = request.POST['name']
            desc = request.POST['desc']
            time = request.POST['time']
            day = request.POST['day']
            create_group(name=name, desc=desc, time=time, day=day)
            return HttpResponseRedirect("/admin_login")
        else:
            return render(request, 'create_group.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm = login_student(password=password, email=email)
        if confirm == True:
            request.session['user'] = email
            return HttpResponseRedirect("/")
        elif email == 'himani.bhatnagar@gmail.com' and password == 'Himani1234':
            return HttpResponseRedirect("/admin_login")

        else:
            messages.info(request, 'Invalid credentials')
            return redirect("/login_student")

    else:
        return render(request, 'login.html')


def home(request):
    if 'user' in request.session:
        cuser = request.session['user']
        cur_user = Information.name(cuser)
        current_user = traverse(cur_user)
        return render(request, 'index.html', context={"current_user": current_user})
    else:
        return render(request, 'index.html')


def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return render(request, 'logout.html')
    else:
        raise Http404


def about(request):

    if request.method == "POST":
        name = request.POST['fname']
        pw = request.POST['lname']
        print(f'"Username: " {name}, Password: {pw}')
        return HttpResponseRedirect('/')
    else:
        return render(request, 'index1.html', )
