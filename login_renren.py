import requests
import re


def login_renren():
    """模拟登陆人人网"""
    data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}
    url = "http://www.renren.com/PLogin.do"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    session = requests.session()  # 初始化一个session类
    session.post(url, headers=headers, data=data)  # 使用session发送post请求
    html_str = session.get("http://www.renren.com/327550029/profile", headers=headers)
    res = re.findall("毛兆军", html_str.content.decode())  # 判断登陆是否成功
    print(res)

if __name__ == '__main__':
    login_renren()
