from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id = '############'

def home(request):
    if request.method == 'POST':
        # 입력된 내용을 바탕으로 
        # https://api.themoviedb.org/3/search/movie?api_key=###########&query=hello
        # 위 url로 get 요청 보내기
        form = SearchForm(request.POST)
        searchword = request.POST.get('search') # POST request온 데이터 중에서 search로써 입력된 값을 갖고 오겠다.
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+ my_id +'&query=' + searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html', {'resdata':resdata, 'obj':obj})
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)
        obj =obj['results']
        return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):
    # https://api.themoviedb.org/3/movie/300?api_key=
    # 이 url에 get 요청 보내기
    url = 'https://api.themoviedb.org/3/movie/'+ movie_id + '?api_key='+my_id
    response = requests.get(url)
    resdata = response.text
    resdata = json.loads(resdata)
    return render(request, 'detail.html', {'resdata':resdata})

