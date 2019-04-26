from selenium import webdriver
import time

def login_in(driver,user,pawword):
    driver.get("https://github.com/login")
    #登录，输入用户名密码并点击登录
    driver.find_element_by_name("login").send_keys(user)
    driver.find_element_by_id("password").send_keys(pawword)
    time.sleep(2)
    driver.find_element_by_name("commit").click()
    time.sleep(2)

    #判断是否登录成功
    driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > summary > img").click()
    name=driver.find_element_by_xpath("/html/body/div[1]/header/div[8]/details/details-menu/div[1]/a/strong").text
    print(name)
    if name==user:
        print("登录成功！")
    else:
        print("登录失败！")

def login_out(driver):
    driver.refresh()
    time.sleep(2)
    driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > summary > img").click()
    driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button").click()
    time.sleep(2)
    driver.refresh()
    print("关闭浏览器")
    driver.close()
    driver.quit()

if __name__ == '__main__':
    user="BBQ20190420"
    pwd="youareapig2012"
    driver=webdriver.Chrome()
    login_in(driver,user,pwd)
    login_out(driver)


