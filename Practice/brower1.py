from selenium import webdriver
import time

path="/Users/bqq/PycharmProjects/qqtest/VIPtest2/Practice/screenshot/"
mytime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
#打开百度
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

#等待加载
time.sleep(5)

#刷新页面
driver.refresh()
time.sleep(3)

#前进和后退
driver.get('http://www.runoob.com/w3cnote')
time.sleep(3)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)

#设置窗口大小
#driver.set_window_size(540,960)
#time.sleep(3)
#driver.maximize_window()


#截屏
driver.get_screenshot_as_file(path+"/"+mytime+".png")
time.sleep(2)

# #id定位
# driver.find_element_by_id("kw").send_keys("python")
# #name定位
# driver.find_element_by_name("wd").send_keys("python")
# #class定位
# driver.find_element_by_class_name("s_ipt").send_keys("python")
# #文本定位,当带有超链接的时候，可以使用此种方式
# driver.find_element_by_link_text("hao123").click()
# #文本定位，带文字过多时，可以使用模糊匹配
# driver.find_element_by_partial_link_text("ao123").click()
# #xpath定位
# driver.find_element_by_xpath('//*[@id="s_menus_wrapper"]/span[2]').click()
# #css定位
# driver.find_element_by_css_selector("#lg").click()

#关闭
driver.close()
driver.quit()

