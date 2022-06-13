from multiprocessing.pool import ThreadPool

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome('D:\other software\chromedriver_win32\chromedriver.exe')
browser.get("https://www.designspiration.com/search/saves/?q=interior%20design")

continue_btn = WebDriverWait(browser, 20).until(presence_of_element_located((By.CLASS_NAME, "buttonsContainer")))
continue_btn.click()


# js = "var q=document.documentElement.scrollTop=10000"
# js = "var q=document.getElementById('id').scrollTop=10000"
# js = "var q=document.body.scrollTop=10000"
# browser.execute_script(js)

def get_imgs():
    for i in range(0, 10):
        browser.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    text = browser.page_source
    main_page = BeautifulSoup(text, "html.parser")
    imgs = main_page.find_all("img", class_="gridItemContent")
    img_srcs = set()
    for img in imgs:
        img_src = img.get("src")
        img_srcs.add(img_src)
    return img_srcs
    # for img in imgs:
    #     count += 1
    #     img_src = img.get("src")
    #     print("count = {}, img_src = {}", count, img_src)
    #     # 下载图片
    #     img_resp = requests.get(src)
    #     # img_resp.content#这里拿到的字节
    #     img_name = src.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    #     with open("D:/tmp\img/" + img_name, mode="wb") as f:
    #         f.write(img_resp.content)  # 图片内容写入到文件


# 下载图片数据
def down_img(img_url):
    img_name = img_url.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    r = requests.get(url=img_url, timeout=8)
    with open("D:/tmp/img/" + img_name, mode="wb") as f:
        f.write(r.content)
    print(f'{img_name} 图片下载成功了！')


# 多线程下载图片数据
def thread_down(imgs):
    try:
        # 开4个 worker，没有参数时默认是 cpu 的核心数
        pool = ThreadPool()
        results = pool.map(down_img, imgs)
        pool.close()
        pool.join()
        print("采集所有图片完成！")
    except:
        print("Error: unable to start thread")


def main():
    imgs = get_imgs()
    thread_down(imgs)


if __name__ == '__main__':
    main()
