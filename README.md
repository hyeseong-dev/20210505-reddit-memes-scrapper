# Simple APIs using FastAPI Webfamework ๐


## **๐ ํ๋ก์ ํธ ์๊ฐ**

> ์๋ํ์ธ์. ์ด๋ฒ ํ ์ดํ๋ก์ ํธ๋ requests, bs4, FastAPI๋ฅผ ์ด์ฉํ์ฌ image webscrapper๋ฅผ ๋ง๋ค์์ผ๋ฉฐ ์ด๋ฅผ ๊ทธ๋ฆผํ์ผ๋ก ์ ์ฅ ํ
> FastAPI ์น ํ๋ ์์ํฌ๋ฅผ ์ด์ฉํ์ฌ ์๋์ ๊ฐ์ Endpoint API๋ฅผ ๋ง๋ค์์ต๋๋ค. 
> ์ ์ ํ์ค์ ์ reddit ์น์ฌ์ดํธ์ ๊ฐ์ํ๊ณ  ๊ฐ๋ฐ์ ๋ฑ๋ก์ ํ ์ดํ client_secret, client_id, user_agent ๊ฐ์ ๋ฐ์ ์ด์ฉํด์ผ ํฉ๋๋ค. 

### <ํน์ง>
1. requests, beautifulsoup ํจํค์ง์ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ด์ฉํ์ฌ ์ด๋ฏธ์ง ์น ์คํฌ๋ํ
2. ์คํฌ๋ํํ ์ด๋ฏธ์ง๋ฅผ ๋ณ๋์ ๊ตฌ๋ถ๋ ์นดํ๊ณ ๋ฆฌ๋ณ ์ด๋ฏธ์ง ํด๋์ ์ ์ฅ
3. ๊ตฌ๋ถ๋ ์นดํ๊ณ ๋ฆฌ๋ณ ์ด๋ฏธ์ง๋ค์ GET, POST ์์ฒญ์ ๋ฐ๋ผ์ API๋ฅผ ์์ฑ
4. POST ์์ฒญ ์ ์ด๋ฏธ ์์ฑ๋ ๋๋ ํ ๋ฆฌ์ "ํ์ํฌ๋งท-ํ์ผ์ด๋ฆ.ํ์ฅ์'ํ์์ผ๋ก ์ ์ฅ

### ํ์ฉ ํจํค์ง ๋ฐ ๋ผ์ด๋ธ๋ฌ๋ฆฌ 

- praw
- beautifulsoup4
- aiohttp
- python-multipart
- requests
- uvicorn
- fastapi
- python-dotenv

### <ํ๋ก์ ํธ ๋๋ ํ ๋ฆฌ ๊ตฌ์กฐ>
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

### GET ์์ฒญ ์ 
์ฌ๋ฌ general-memes ์ค ๋๋คํ ์ด๋ฏธ์ง๋ฅผ ์์ฒญ์ ์๋ต์ผ๋ก ์ฒ๋ฆฌํ๋๋ก ๋ก์ง์ ๊ตฌ์ฑํ์์ต๋๋ค.
![image](https://user-images.githubusercontent.com/57933835/117153133-a6163c80-adf5-11eb-9611-2ac08bc0d86f.png)
![image](https://user-images.githubusercontent.com/57933835/117153249-c219de00-adf5-11eb-89d8-aa5f2ef6f81b.png)

### POST ์์ฒญ ์ 
![image](https://user-images.githubusercontent.com/57933835/117153502-00af9880-adf6-11eb-8579-2584ca7bd1d3.png)

<ํ์ผ ์ ํ>
![image](https://user-images.githubusercontent.com/57933835/117153589-191fb300-adf6-11eb-8039-53953380feb6.png)

<response๋ ์ด๋ฏธ์ง>
![image](https://user-images.githubusercontent.com/57933835/117153790-42d8da00-adf6-11eb-9da5-56c169000674.png)

<์ง์ ๋ ํ์์ ์ด๋ฆ์ผ๋ก ์ ์ฅ๋ ์ด๋ฏธ์ง ํ์ผ>
![image](https://user-images.githubusercontent.com/57933835/117154029-7451a580-adf6-11eb-9796-00bc11145a11.png)



