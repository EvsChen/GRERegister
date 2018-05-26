from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep  
from pymongo import MongoClient
import urllib
import os
import captcha

client = MongoClient('localhost',27017);
db = client.gre;
success = db.success;
fail = db.fail
neeaId = '71406776'
password = '86993136Gre'
driver = webdriver.Firefox()
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
# driver = webdriver.PhantomJS()
options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# options.add_argument('headless')
options.add_argument('window-size=1200x600')
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
options.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(chrome_options=options)

driver.get('https://gre.etest.net.cn/login.do')
input_locator = (By.ID,'checkImageCode')
class not_loading(object):
    def __init__(self, locator):
        self.locator = locator
    def __call__(self, driver):
        try:
            src = EC._find_element(driver, self.locator).get_attribute('src')
            if src != "https://gre.etest.net.cn/resources/images/loading.gif":
                return True
            else:
                return False
        except: 
            return False

class js_loaded(object):
    def __init__(self,script):
        self.script = script
    def __call__(self, driver):
        try:
            driver.execute_script(self.script)            
        except: 
            return False
        else: 
            return True

try:
    captcha_input = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(input_locator))
    print 'Input located'
    WebDriverWait(driver,20,0.5).until(js_loaded('inputClick()'))
    img_locator = (By.ID,'chkImg')
    # captcha_image = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(img_locator))
    WebDriverWait(driver, 20, 0.5).until(not_loading(img_locator))
    captcha_image = driver.find_element_by_id('chkImg')
    captcha_url = captcha_image.get_attribute('src')
    # while (captcha_url == "https://gre.etest.net.cn/resources/images/loading.gif"):
        # captcha_image = driver.find_element_by_id('chkImg')
        # captcha_url = captcha_image.get_attribute('src')        
    print 'Image located'    
    # captcha_image = driver.find_element_by_id('chkImg')
    # print captcha_image
    print captcha_url
except Exception,e:
    print Exception,":",e

driver.close()

# driver.get('https://www.baidu.com')
# driver.get('https://gre.etest.net.cn')
# scriptToExecute = "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;";
# netData = driver.execute_script(scriptToExecute);
# print netData
# while True:
#     # captcha_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'checkImageCode')))
#     # print captcha_input
#     # captcha_input.click()    
#     # captcha_input.send_keys('aaa')
#     captcha_input = driver.find_element_by_id('checkImageCode')
#     # sleep(1) 
#     while True:
#         captcha_input.click()
#         captcha_image = driver.find_element_by_id('chkImg')
#         captcha_url = captcha_image.get_attribute('src') 
#         print captcha_url
#         data = urllib.urlopen(captcha_url).read()
#         filename = captcha_url.split('/')[-1]
#         if filename != "loading.gif": 
#             break
#     # print(captcha_image)
#     # print(captcha_url)
#     foldername = filename.split('.')[0]
#     filepath = './captcha/'+foldername+'/'+filename
#     try:
#         os.mkdir('./captcha/'+foldername+'/')
#         f = open(filepath, 'wb')
#         f.write(data)  
#         f.close()  
#     except: 
#         print 'Already tested'
#     result = captcha.readCaptcha(filepath)
#     print(result)
#     id_input = driver.find_element_by_id('neeaId')
#     id_input.send_keys(neeaId)
#     pw_input = driver.find_element_by_id('password')
#     pw_input.send_keys(password)
#     captcha_input.send_keys(result)
#     captcha_input.send_keys(Keys.ENTER)
#     sleep(2)
#     try:
#         driver.find_element_by_id('checkImageCode.errors')
#     except:
#         try:
#             driver.find_element_by_id('checkImageCodeError')
#         except:
#             sucdata = {
#                 'name': foldername,
#                 'result': result
#             }
#             success.insert_one(sucdata)
#             print 'True'
#             break
#         else: 
#             print 'Not enough length'
#     else:
#         print 'Wrong code'
#     print 'Insert to failure'
#     faildata = {
#         'name':foldername,
#         'failresult': result
#     }
#     fail.insert_one(faildata)
# driver.quit()
# driver.close()