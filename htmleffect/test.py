#coding: utf-8
from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='/Users/stranger/workspace/phantomjs/bin/phantomjs')
driver.set_window_size(1120, 550)
driver.get("http://weixin.sogou.com/gzh?openid=oIWsFtxJdR84pEeI3toDCwIet64M")
driver.find_element_by_id('kw').send_keys("realpython")
driver.find_element_by_id("su").click()
print driver.current_url
driver.quit()