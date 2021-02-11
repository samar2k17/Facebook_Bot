import sys
import time
from random import choice

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys




class Face_Bot():

    def __init__(self, driver, website, username, password):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--profile-directory=Default')
        self.driver = webdriver.Chrome(driver, chrome_options=options)
        self.driver.get(website)
        self.login(username=username, password=password)
        #self.sndfr()
        st="this is on"
        # self.status(st)
        self.fndstatus(st)

    def show_exceptions(self, e):
        print(e)
        self.driver.quit()
        sys.exit()

    def login(self, username, password):
        try:
            email_text = self.driver.find_element_by_id('email')
            email_text.send_keys(username)
            pass_text = self.driver.find_element_by_id('pass')
            pass_text.send_keys(password)
            pass_text.send_keys(Keys.ENTER)
            time.sleep(6)

        except NoSuchElementException as e:
            self.show_exceptions(e)
        except Exception as e:
            self.show_exceptions(e)

    def sndfr(self):
        try:
            body = self.driver.find_element_by_xpath('//*[@id="facebook"]/body')
            body.click()
            profile = self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/div[1]')
            profile.click()
            time.sleep(10)
            about = self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/div[1]/span[1]')
            about.click()
            time.sleep(20)
            place_lived=self.driver.find_element_by_xpath('//body/div[@id="mount_0_0"]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/a[1]/span[1]')
            place_lived.click()
            time.sleep(10)
            loc_text = self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/span[1]').text
            time.sleep(10)
            search_bar=self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]')
            search_bar.send_keys(loc_text)
            time.sleep(5)
            search_bar.send_keys(Keys.ENTER)
            time.sleep(10)
            self.driver.find_element_by_xpath('//span[contains(text(),"People")]').click()
            time.sleep(5)
            self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/span[1]/div[1]/i[1]').click()
        except NoSuchElementException as e:
            self.show_exceptions(e)
        except Exception as e:
            self.show_exceptions(e)

    def status(self, st="this is me"):
        try:
            self.driver.get('https://www.facebook.com/stories/create')
            time.sleep(10)
            self.driver.find_element_by_xpath(
                '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div['
                '1]/div[2]').click()
            time.sleep(15)
            status = self.driver.find_element_by_tag_name('textarea')
            status.send_keys(st)
            time.sleep(5)
            self.driver.find_element_by_xpath(
                '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div['
                '1]/div/span/span').click()
        except NoSuchElementException as e:
            self.show_exceptions(e)
        except Exception as e:
            self.show_exceptions(e)

    def fndstatus(self,msg="Lets Go"):
        try:
            time.sleep(5)
            profile = self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/div[1]')
            profile.click()
            time.sleep(4)
            freind_tab = self.driver.find_element_by_css_selector(
                '#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.rq0escxv.lpgh02oy.du4w35lb.rek2kq2y > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.pxsmfnpt.pedkr2u6.n1dktuyu.dvqrsczn.l23jz15m.d4752i1f > div > div > div > div > div > div > a:nth-child(4)')
            freind_tab.click()
            time.sleep(20)
            freind = self.driver.find_element_by_xpath('[@class="buofh1pr hv4rvrfc"]')
            time.sleep(5)
            freind.click()
            time.sleep(5)
            self.driver.execute_script('window.scrollTo(0,700)')
            time.sleep(2)
            coment = self.driver.find_element_by_css_selector(
                '#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.rq0escxv.d2edcug0.ecyo15nh.k387qaup.r24q5c3a.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.fhuww2h9.hpfvmrgz.gile2uim.pwa15fzy.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5 > div:nth-child(3) > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div.cwj9ozl2.tvmbv18p > div.ecm0bbzt.hv4rvrfc.e5nlhep0.dati1w0a.j83agx80.btwxx1t3.lzcic4wl > div.g3eujd1d.ni8dbmo4.stjgntxs.rz4wbd8a > div._25-w > div > div > div > form > div > div > div._5rpb > div > div > div > div')
            coment.send_keys(msg)
            time.sleep(2)
            coment.send_keys(Keys.RETURN)
        except NoSuchElementException as e:
            self.show_exceptions(e)
        except Exception as e:
            self.show_exceptions(e)



