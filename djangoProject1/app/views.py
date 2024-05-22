from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from .models import *
from django.contrib.auth import authenticate, login as _login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect("/login")
        return render(request, "index.html")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        data = request.POST
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if user:
            _login(request, user)
            return JsonResponse({"msg": "登录成功"})
        else:
            return JsonResponse({"err": "用户名或者密码错误"})

def register(request):
    if request.method == "POST":
        data = request.POST
        if User.objects.filter(username=data.get("username")).exists():
            return JsonResponse({"err": "已存在相同用户名"})
        User.objects.create_user(username=data.get("username"), password=data.get("password"))
        return JsonResponse({"msg": "注册成功"})


@login_required
def pictures(request):
    if request.method == "GET":
        images_list = Pictures.random_picture()
        return JsonResponse({"msg":"success", "data": images_list})
    else:
        if not request.FILES.get("file"):
            return JsonResponse({"err": "请上传图片"})
        p = Pictures.objects.create(upload=request.FILES.get("file"))
        p.save()
        return JsonResponse({"msg": "上传成功"})

@login_required
def user_admin(request):
    if request.method == "GET":
        return render(request, "admin.html")

@login_required
def comment(request):
    if request.method == "POST":
        data = request.POST
        try:
            if not request.user.is_authenticated:
                logout(request)
                return redirect("/login")
            if not request.POST.get("content", ""):
                return {"err": "请输入评论内容"}
            elif not request.POST.get("picture"):
                return {"err": "请选择一个图片进行评论"}
            c = Comment.objects.create(user=request.user, content=request.POST.get("content"),
                                       picture=Pictures.objects.get(id=request.POST.get("picture")))
            c.save()
            return JsonResponse({"msg": "评论成功！"})
        except Exception as e:
            raise e
            return JsonResponse({"err": "评论失败"})