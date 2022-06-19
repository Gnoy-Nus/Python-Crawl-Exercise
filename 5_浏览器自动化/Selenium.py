from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.options import Options
from PIL import Image
from selenium.webdriver.edge.service import Service

edge_options = Options()
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 规避检测
# edge_options.add_argument("--headless") # 实现无可视化界面的操作
# edge_options.add_argument("--disable-gpu")
# bro = webdriver.Edge(executable_path='msedgedriver.exe', options=edge_options)

service = Service("msedgedriver.exe")#应用程序位置
bro = webdriver.Edge(service=service, options=edge_options)
bro.get(url='https://www.bilibili.com')

# # 获取页面html
# page_text = bro.page_source
# print(page_text)

# 执行js代码
# bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(1)

# 模拟搜索
search_input = bro.find_element(by=By.XPATH, value='//*[@id="nav-searchform"]/div[1]/input')
search_input.send_keys('4K')
sleep(1)
btn = bro.find_elements(by=By.XPATH, value='//*[@id="nav-searchform"]/div[2]')[0]
btn.click()
sleep(1)

# # 前进后退
# bro.forward()
# bro.back()

# #iframe
# bro.switch_to.frame('iframe_id')

# #动作链执行拖动动作
# action = ActionChains(bro)
# tag = bro.find_element(by=By.XPATH,value='')
# action.click_and_hold(tag)
# for i in range(1,5):
#     action.move_by_offset(17,0).perform()
#     sleep(0.2)
# action.release()

# #截图,PIL库进行裁剪
# bro.save_screenshot('a.png')
# img = Image.open('a.png')
# rangle = (int(btn.location['x']),int(btn.location['y']),int(btn.location['x']+btn.size['width']),int(btn.location['y']+btn.size['height']))
# print(rangle)
# frame=img.crop(rangle)
# frame.save('part.png')

# 动作链执行连续点击动作
# ActionChains(bro).move_to_element_with_offset(btn,xoffset=0,yoffset=45).click().perform()

# bro.quit()
