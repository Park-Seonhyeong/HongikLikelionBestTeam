from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreeCommentForm, FreePostForm
from .models import Post, Comment, FreePost, FreeComment 
from django.core.paginator import Paginator

def home(request):
    posts = Post.objects.filter().order_by('-date') # Post의 객체들을 모두 가져와라

    paginator = Paginator(posts, 5) # 게시물 5개씩 나누기
    pagnum = request.GET.get('page') # {page:1} 에서 해당 페이지의 넘버를 저장하기
    posts = paginator.get_page(pagnum) # 해당하는 페이지 넘버 즉, pagnum에 해당하는 게시물들이 posts에 담기게 된다.
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    # request method가 Post일 경우 
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        # 입력값 저장

    # request method가 GET일 경우
        # form 입력 html 띄우 기
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})


def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id)

def freehome(request):
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})


def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user            
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})


def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        # finished_form.author = request.user
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)
    