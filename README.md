# Simple APIs using FastAPI Webfamework 🚄


## **🏠프로젝트 소개**

> 안녕하세요. 이번 토이프로젝트는 requests, bs4, FastAPI를 이용하여 image webscrapper를 만들었으며 이를 그림파일로 저장 후
> FastAPI 웹 프레임워크를 이용하여 아래와 같은 Endpoint API를 만들었습니다. 
> 유의 하실점은 reddit 웹사이트에 가입하고 개발자 등록을 한 이후 client_secret, client_id, user_agent 값을 받아 이용해야 합니다. 

### <특징>
1. requests, beautifulsoup 패키지와 라이브러리를 이용하여 이미지 웹 스크래핑
2. 스크래핑한 이미지를 별도의 구분된 카테고리별 이미지 폴더에 저장
3. 구분된 카테고리별 이미지들을 GET, POST 요청에 따라서 API를 생성
4. POST 요청 시 이미 생성된 디렉토리에 "타임포맷-파일이름.확장자'형식으로 저장

### 활용 패키지 및 라이브러리 

- praw
- beautifulsoup4
- aiohttp
- python-multipart
- requests
- uvicorn
- fastapi
- python-dotenv

### <프로젝트 디렉토리 구조>
![image](https://user-images.githubusercontent.com/57933835/117150748-651d2880-adf3-11eb-84bf-697020e6fb28.png)

### <API Endpoints>
![image](https://user-images.githubusercontent.com/57933835/117150845-7e25d980-adf3-11eb-8246-b71fb5e64e41.png)

### Modules
#### main.py
![image](https://user-images.githubusercontent.com/57933835/117151356-f42a4080-adf3-11eb-94eb-a6cc4675e397.png)

#### meme_collector.py
![image](https://user-images.githubusercontent.com/57933835/117151420-05734d00-adf4-11eb-98dc-06f56bb3f821.png)
![image](https://user-images.githubusercontent.com/57933835/117151454-0e641e80-adf4-11eb-9e5f-ac78533e0e6c.png)

#### services.py
![image](https://user-images.githubusercontent.com/57933835/117151482-18861d00-adf4-11eb-9273-3e61b159cf6b.png)



