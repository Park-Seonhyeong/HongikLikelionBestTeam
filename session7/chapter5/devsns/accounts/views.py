from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password) 
        #authenticate는 이 username과 password에 해당하는 user 객체를 반환하고
        #만약 그렇지 않다면 none을 반환한다.

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: # 실제로 존재하는 회원이 아니라면
            return render(request, 'bad_login.html')
    # request == POST
    # 로그인 시키기 


    else:
        return render(request, 'login.html')
    # request == GET
    # login html 띄우기

def logout(request):
    auth.logout(request) 
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # home redirection
            return redirect('home')
    return render(request, 'register.html')
