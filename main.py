import feedparser, time

URL = "https://whdgus928.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
## ✏공부하고 있는 분야
* 데이터
  * 데이터 정재/가공
  * 데이터 분석
* 웹 개발 - streamlit
* 백엔드
* 알고리즘
* SQL

## ✅ 최근에 작성한 글
"""  # list of blog posts will be appended here


end_text="""
## 💻공부하는 방법
[기술 블로그](https://whdgus928.tistory.com/)

## 📋사용할 수 있는 기술
<img src="https://img.shields.io/badge/Python-gray?style=flat&logo=Python&logoColor=3776AB"> <img src="https://img.shields.io/badge/Java-007396?style=flat&logo=Java&logoColor=white">

<img src="https://img.shields.io/badge/mysql-4479A1?style=flat&logo=mysql&logoColor=white">

## 📃깃허브 활동 요약
![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=whdgus928&show_icons=true&theme=vue )

## 자주 사용하는 언어
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=whdgus928&layout=compact&theme=vue)

## 활동하는 소셜
<a href="https://career.programmers.co.kr/pr/whdgus928_1461"><img src="https://img.shields.io/badge/-programmers-blue?style=flat"/></a>
<a href="https://whdgus928.tistory.com/"><img src="https://img.shields.io/badge/Tistory-000000?style=flat&logo=tistory&logoColor=white"/></a>

## 이력서
<a href="https://www.notion.so/whdgus928/2920bd38d9eb4fa8a3e8fa9cb19fe7b8"><img src="https://img.shields.io/badge/notion-000000?style=flat&logo=notion&logoColor=white"/></a>

## 🌞평소 지내는 모습
<a href="https://blog.naver.com/whdgus928"><img src="https://img.shields.io/badge/Naver-03C75A?style=flat&logo=naver&logoColor=white"/></a>

***

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fwhdgus928%2Fhit-counter&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://github.com/whdgus928)

"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        markdown_text += f"[- {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.write(end_text)
f.close()
