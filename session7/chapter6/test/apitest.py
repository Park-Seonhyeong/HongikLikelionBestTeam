import os
import sys
import ssl
import urllib.request # 특정 url에 request를 날릴 수 있도록 하는 것
import json

client_id = "pm73vkV61Dx8twKLEERv"
client_secret = "Uao_WtCVHg"

encText = urllib.parse.quote("닥터스트레인지")
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

# response = urllib.request.urlopen(request)
context = ssl._create_unverified_context()
response = urllib.request.urlopen(request,context=context)

rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

resdata = response_body.decode('utf-8')

# with open('movie.json', 'w', encoding='UTF-8 sig') as file:
#     file.write(json.dumps(resdata, ensure_ascii=False)) # json.dumps -> json 내용을 실어주어라

pydata = json.loads(resdata) # json 내용을 가지고 와 줘라
data = pydata['items']

print(data[0]['title'])