from dotenv import load_dotenv
load_dotenv()
import os
import requests
from pprint import pprint


def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.
    API_Key = os.getenv('API_Key')
    title = input()
    URL1 = f'https://api.themoviedb.org/3/search/movie/?api_key={API_Key}&language=ko-KR&region=KR&query={title}'

    try: 
        response1 = requests.get(URL1).json()
        data1 = response1['results']
        favor = data1[0]['id']

        URL2 = f'https://api.themoviedb.org/3/movie/{favor}/recommendations?api_key={API_Key}&language=ko-KR'
        
        response2 = requests.get(URL2).json()
        data2 = response2['results']
        names = []
        for movies in data2:
            names.append(movies['title'])
        return names

    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
