# http请求包括两个参数：网址url和http-header
#使用库urllib
import urllib.request
url="https://movie.douban.com/top250"
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

}
#构造一个request请求对象
req=urllib.request.Request(url=url,headers=header)
#调用urlopen函数向豆瓣服务器发送请求，获取到回复response
response=urllib.request.urlopen(req)
#读取回复并使用UTF-8编码进行解码
html=response.read().decode("utf-8")
print(html)