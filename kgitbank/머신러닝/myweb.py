from wsgiref.simple_server import make_server 


def application(environ, start_response):
    response_body = "Hello Python Web"
    response_status="200 OK"

    response_headers = [('Content-Type', 'text/plain'), 
    ('Content-Length', str(len(response_body)))]

    start_response(response_status, response_headers)
    return [response_body.encode("utf-8")]

httpd = make_server('localhost', 5000, application) 
print("Server start http://127.0.0.1:5000")

httpd.handle_request()

from flask import Flask 

#1. Flask 객체를 만든다 
app = Flask( __name__ )  #모듈명 __main__ 

#2. 라우터만들기 - 클라이언트엣 접속요청이 오면 url 분석해서 누가 응대할지를 지정
#http://127.0.0.1:5000/
@app.route("/")
def index():
    return "Hello Python !!!"

#http://127.0.0.1:5000/myhome
@app.route("/myhome")
def myhome():
    return "Welcome my home !!!"

#@ - 데코레이터, 코드를 숨겨놓고 다른코드를 가로채서 수행한다
@app.route("/test1")
def test1():
    return "<h1>This is routing test</h1>"

#서버로 값을 보내는방법(get방식, post방식) 
#http://127.0.0.1:5000/logon?userid=test&password=1234
#키와 값 쌍으로, 키=값&키2=값2&키3=값3 (1024byte 이내에만)
from flask import request 

@app.route("/logon", methods=["POST", "GET"])
def logon():
    userid = request.values["userid"]
    password = request.values["password"]

    return f"<h1>userid :{userid} password:{password}</h1>"


if __name__ == "__main__":
    print("http://127.0.0.1:5000 server started")
    app.run("0.0.0.0", port=5000)
    #0.0.0.0 - 현재 컴퓨터가 사용중인 아이피를 사용하라는 의미