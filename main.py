# 간단한 홈페이지 제공
# 1. 모듈 가져오기
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# 2. fastapi 객체 생성
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 3. 라우팅 구성
@app.get("/")
def home(req:Request):
    # 홈페이지 요청(GET)
    # > index.html을 읽어 req 데이터 전달하여 동적 html 구성
    # > 응답
    # > 브라우저 화면 구성
    return templates.TemplateResponse(req, "index.html")
