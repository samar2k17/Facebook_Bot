import time

from Face_Bot.Face_Bot import Face_Bot
if __name__ == "__main__":
    username = '9205502894'
    password = 'samar@123'
    url = 'https://www.facebook.com'
    driver = 'D:/chromedriver.exe'
    Face_Bot(driver, url, username, password)
    time.sleep(20)






