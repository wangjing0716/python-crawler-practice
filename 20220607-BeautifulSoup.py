from bs4 import BeautifulSoup

html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.title.string)
#学习python的正确姿势
print(soup.p.string)
#小帅b的故事
print(soup.title.parent.name)
#head
print(soup.a)
#<a class="sister" href="http://example.com/1" id="link1">一个笑话长</a>
print(soup.find_all('a'))
#[<a class="sister" href="http://example.com/1" id="link1">一个笑话长</a>, <a class="sister" href="http://example.com/2" id="link2">一个笑话短</a>]
print(soup.find(id="link2"))
#<a class="sister" href="http://example.com/2" id="link2">一个笑话短</a>
print(soup.get_text())
# 学习python的正确姿势
#
# 小帅b的故事
# 有一天，小帅b想给大家讲两个笑话
# 一个笑话长,
# 一个笑话短 ,
# 他问大家，想听长的还是短的？
# ...

print(soup.select("title"))
# [<title>学习python的正确姿势</title>]
print(soup.select("body a"))
# [<a class="sister" href="http://example.com/1" id="link1">一个笑话长</a>, <a class="sister" href="http://example.com/2" id="link2">一个笑话短</a>]
print(soup.select("p > #link1"))
# [<a class="sister" href="http://example.com/1" id="link1">一个笑话长</a>]