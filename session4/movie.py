import requests
import json

client_id = '########' # 네이버 client id
client_secret = '########' # 네이버 client secret

moviename = "아이언맨" # 검색하고자 하는 영화 이름

headers={ # api 통신을 위한 header / 서버가 이것을 보고 정보를 줄지 말지 결정
    'X-Naver-Client-Id': client_id, 
    'X-Naver-Client-Secret': client_secret
}

url =f'https://openapi.naver.com/v1/search/movie.json?query={moviename}'


response = requests.get(url, headers=headers) # 정보 받아오기

jsonObject = json.loads(response.text) # 정보는 str 타입인데 json.load 사용 시 dictionary 형태로 바꿔줌

min_print = min(10, len(jsonObject["items"])) # if 영화 결과 값이 10개 이하일 경우 출력 개수를 영화 결과 값에 맞춰줌

for i in range(0, min_print):
    if(response.status_code == 200): # 정보를 잘 전달 받았다면
        title = jsonObject["items"][i]["title"]
        title = title.replace('<b>', '') # b태그 제거
        title = title.replace('</b>', '')

        link = jsonObject["items"][i]["link"]

        director = jsonObject["items"][i]["director"]
        director = director.replace('|', '') # | 제거

        print(title)
        print(link)
        print(director)
        print('\n')
    else: # 실패일 때
        print("Error Code:" + response.status_code)