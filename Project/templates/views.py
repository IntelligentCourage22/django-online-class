from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib import messages



def Signup(request,student):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
    
        user = MyUser.objects.create(username=username , password=password , is_student=student )
        user.save()
        
        print('user created')
        messages.success(request, f"Account created for {username}!")
        return HttpResponseRedirect("/login")
    
     
    else:      
        return render(request , 'users/SignupSt.html')
   

 
   
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        #messages.info(user,'user is tis')
        if user is not None:
            auth.login(request , user)
            return redirect('app-about')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/login')
    else:
        return render(request, 'users/login.html' )
    
    


def home(request):
    return render(request , 'Himani_classes/index.html')

def about(request):
    return render(request , 'Himani_classes/about.html')

