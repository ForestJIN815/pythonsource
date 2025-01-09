from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# 크롬 브라우저를 구동하기 위해 크롬 드라이버 다운로드 후 실행시켜주는 함수
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    return driver


if __name__ == "__main__":
    driver = set_chrome_driver()
    driver.get("https://www.naver.com")
