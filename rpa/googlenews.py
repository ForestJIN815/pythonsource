import requests
from bs4 import BeautifulSoup


def main(keyword):
    url = f"https://news.google.com/search?q={keyword}&hl=ko&gl=KR&ceid=KR%3Ako"

    res = requests.get(url)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        news = data_extract(soup)

        for item in news:
            for k, v in item.items():
                print(f"{k} : {v}")
            print()


def data_extract(soup):
    base_url = "https://news.google.com"

    # [
    #    {"title": "", "writer": ""},
    #    {"title": "", "writer": ""},
    #    {"title": "", "writer": ""},
    # ]

    news = []

    articles = soup.select("article")

    for article in articles:
        news_item = {}

        element = article.find("a", class_="JtKRv")

        # 제목
        title = element.text.strip()
        # 링크
        link = base_url + element["href"][1:]
        # 작성자
        writer = article.find("div", class_="bInasb")
        if writer:
            writer = writer.text.strip()
        else:
            writer = ""

        # 작성일시
        datetime = article.find("time", class_="hvbAAd")["datetime"].split("T")
        date = datetime[0]
        time = datetime[1]

        news_item["title"] = title
        news_item["link"] = link
        news_item["writer"] = writer
        news_item["date"] = date
        news_item["time"] = time
        news.append(news_item)

    return news


if __name__ == "__main__":
    main("파이썬")
