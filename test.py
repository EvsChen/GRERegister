from selenium import webdriver
from time import sleep  
import random
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# driver = webdriver.PhantomJS()
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

profile_dir="~/library/application support/google/chrome"    
# options.add_argument("user-data-dir="+os.path.abspath(profile_dir))  
# options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://gre.etest.net.cn/login.do')
driver.delete_all_cookies()
driver.add_cookie({'name':'FSSBBIl1UgzbN7N443S','value':'HnNmpuFU0NENXZDXL_VdyB_Aatj.17xtDiUdFgi59.Y95BmMSaxTTioJKoYQisYv'})
driver.add_cookie({'name':'JSESSIONID','value':'BD4817762E8DFB0334FDDC89FE645FD4'})
driver.add_cookie({'name':'step','value':'myStatus.do'})
driver.add_cookie({'name':'ajaxStep','value':'myHome'})
driver.add_cookie({'name':'FSSBBIl1UgzbN7N443T','value':'1Boj963pPhAlm1RfF978kjcJxWFleTg9pPX6Zk5xWZAmRHTXacYwPmaIjD.uozgIru7bY1VidVHbZ4qsvKgtr1_KYSMCaQtDs_rc1w9BSVlowgsEab6PLDMO9N0pkyNwdexCfeTtBBy0AeShuhJfoGL4NcNsyMS4bv_n7gKahzGBEOKJsVlboNReZlg4NkTGwlprobB2aa0cLpyoa.KICxVlaBSN7MwFNxYjD.x.TOh6Q4yMGi0v93aeCVygqO3xsq.RxE1Z9Rcfq6auCzNECF.ssss9CDWUKlawtMdBczTs9ilVYR8NVQOmfZbqBmRZsdw22Yi7RFH3TVhNcKN8.mV0x'})
driver.get('https://gre.etest.net.cn/login.do')



# driver.get('https://checkimage.etest.net.cn/67F4623A799FCEC595BCC84290181D50.jpg')
# driver.get('https://gre.etest.net.cn/myStatus.do?neeaID=71406776')
# driver.get('https://gre.etest.net.cn')
# driver.get('https://www.baidu.com')
# sleep(10)
print driver.page_source
# driver.quit()
