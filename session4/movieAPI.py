import os
import sys
import urllib.request # API로 요청을 올바르게 보내기 위해서 ipipmport함 
client_id = "iIN2d281tAV1NI4ZHxSS" # 위에서 받은 클라이언트 ID 넣어줌
client_secret = "P6r6AnZ3Kt" # 위에서 받은 시크릿키 넣어줌

encText = urllib.parse.quote("기생충")
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id) # API주소로 요청을 보낼 때 헤더에 클라이언트 ID를 꼭 넣어줘야함
request.add_header("X-Naver-Client-Secret",client_secret) # API주소로 요청을 보낼 때 헤더에 시크릿키를 꼭 넣어줘야함

response = urllib.request.urlopen(request) # API주소로부터 받은 API객체를 response에 넣는다.
rescode = response.getcode() # HTTP 코드 200은 성공을 의미
if(rescode==200): # 성공일 때
    response_body = response.read()
    response_body = response_body.decode('utf-8') # 한국어로 정보를 얻기 위해 utf-8로 디코딩 함
    response_body = response_body.replace('<b>', ' ')
    response_body = response_body.replace('</b>',' ')
    response_body = response_body.replace('|', ' ')
    print(response_body)
else: # 실패일 때
    print("Error Code:" + rescode)