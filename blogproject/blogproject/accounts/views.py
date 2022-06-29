from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    #POST 요청이 들어오면 로그인 처리 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd) #사용자가 입력한 아이디와 비번이 실제로 있는지 검사해줌
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'login.html')
        
    #GET 요청이 들어오면 login form 을 담고있는 login.html 띄워줌
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')