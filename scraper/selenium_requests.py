from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import requests

caps = DesiredCapabilities().CHROME
#caps["pageLoadStrategy"] = "normal"  # complete
caps["pageLoadStrategy"] = "eager"  #interactive
#caps["pageLoadStrategy"] = "none"
chromedriver = "/opt/chromedriver"
#options = Options()
#options.set_headless(headless=True)
driver = webdriver.Chrome(
    #options=options,
    desired_capabilities=caps,
    executable_path=chromedriver)
driver.set_window_size(800, 1000)
# driver.set_network_conditions(
#     offline=False,
#     latency=5,  # additional latency (ms)
#     download_throughput=500 * 1024,  # maximal throughput
#     upload_throughput=500 * 1024)  # maximal throughput
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
wait = driver.implicitly_wait(10)

url = "https://student.amizone.net"
driver.get(url)  # getting amizone.net

def login(username, password):
    try:
    # type | name=_UserName
        driver.find_element(By.NAME, "_UserName").send_keys(username)
    # type | name=_Password
        driver.find_element(By.NAME, "_Password").send_keys(password)
    # click | css=#loginform .login100-form-btn |
        driver.find_element(
            By.CSS_SELECTOR, "#loginform .login100-form-btn").click()
    except:
       print("couldn't complete login")

username = "7071804"
password = "gulabjamun"

login(username, password)

request_cookies_browser = driver.get_cookies()
print(request_cookies_browser)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Set-Cookie': 'ASPSESSIONIDSWDCBSBQ=GKACLGDCKMDFKAOHNOOOPBOM; secure; path=/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection':'keep-alive',
    'DNT': '1',
    'Host': 'amizone.net',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
}
s = requests.Session()
for dic in request_cookies_browser:
    dic.pop('httpOnly')
    print(dic)
    s.cookies.set(**dic)

#c = [s.cookies.set(c['name'], c['value']) for c in request_cookies_browser]
#print(c)
resp = s.get(url+"/Home", headers = headers)
with open("amizone.html", 'w') as f:
    f.write(resp.text)
print(resp.text)