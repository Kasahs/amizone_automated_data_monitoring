Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@hackasaur 
hackasaur
/
amizone_automated_data_monitoring
1
00
 Code Issues 0 Pull requests 0 Actions Projects 0 Wiki Security Insights Settings
amizone_automated_data_monitoring/amizone_automated_login.py / 
@hackasaur hackasaur added my Classes timetable scrapper
3d1dd94 on 29 Jan
267 lines (245 sloc)  11.8 KB
 
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

You're using code navigation to jump to definitions or references.
Learn more or give us feedback
#import sys
import time
import db
from bs4 import BeautifulSoup
from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# from selenium.webdriver.support import expected_conditions as EC

# TODO: try to get info without opening browser(not possible)
# TODO: close all pop-ups without specifying name(done)
# TODO: find the div id for the corresponding close button(done)
# TODO: extract data from amizone using beautifulSoup
# TODO: add data to database using mysql
# TODO: make a mechanism to navigate myclasses through input and get data
# TODO: figure out how to make useful information from data
# TODO: organize code
# TODO: do exception handling of the code
# NOTE: program doesn't work if window is minimized
# NOTE: popups don't close when pageLoadStrategy is eager try time.sleep()
# NOTE: in amizone can't check both attendance and timetable without logging in again
# NOTE: myClasses timetable scraping doesn't work properly without time.sleep(2)
start_time = time.time()  # stores time at which program starts

# while(True):

# ***setting up chrome driver***
caps = DesiredCapabilities().CHROME
#caps["pageLoadStrategy"] = "normal"  # complete
caps["pageLoadStrategy"] = "eager"  #interactive
#caps["pageLoadStrategy"] = "none"
chromedriver = "/usr/share/chromedriver/chromedriver"
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

# ***write page content to a file and return page soup***

def page_content_to_file(*argsv):
    wait
    content = driver.page_source
    page_soup = BeautifulSoup(content, "html.parser")
    #page_soup_text = BeautifulSoup.prettify(page_soup)
    if(len(argsv) > 1):
        raise NameError(
            'page_content_to_file cannot take more than 2 arguments')
    if(len(argsv) == 1):
        filename = argsv[0]
        with open(filename, "w") as file:
            file.write(content)
            print("wrote to file {}".format(filename))
    return page_soup

# ***function that enters login credentials***
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

# ***function to close popups***
def close_popups():
    # try:
    page_soup = page_content_to_file("popup.html")
    #   getting names of divs having class 'modal fade in'
        # driver.implicitly_wait(10)
        # content = driver.page_source
        # page_soup = BeautifulSoup(content,"html.parser")
    popup_divs = page_soup.find_all('div', {"class": "modal fade in"})
# print(popup_divs)
    popups_name = []
    for div in popup_divs:
        popups_name.append(div['id'])
        print(popups_name)
    if(len(popups_name) == 0):
        print("no popups found popups_name length=0")
    else:
        print("starting")
    #   clicking to close pop-ups
        for name in reversed(popups_name):
            xpath = "//div[@id='" + name + "']//button[@class='close']"
            print(xpath)
            driver.find_element(By.XPATH, xpath).click()
        print("clicks complete")
            # extra code
                # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ModalPopAmityHostel button.btn"))).click()
                # driver.execute_script("arguments[0].click()", driver.find_element_by_css_selector("#StudentSatisfactionPop button.btn"))
                # click | id=ModalPopAmityHostel |
                # driver.find_element(By.XPATH, "//div[@id='ModalPopAmityHostel']//button[@class='close']").click()
                # click | id=StudentSatisfactionPop |
                # driver.find_element(By.XPATH, "//div[@id='StudentSatisfactionPop']//button[@class='close']").click()
    # except:
        # print("error occured while closing popups")
    return 0

def menu_click(option):
    # xpath of the menu toggler(hamburger button)
    menu_toggler_xpath = "//*[@id='menu-toggler']"
    #   clicking on the hamburger button on top left corner
    driver.find_element(By.XPATH, menu_toggler_xpath).click()
    if(option == "timetable"):
        # xpath of the timetable option in menu
        time_table_navbar_xpath = "//*[@id='10']"
        #   clicking on the timetable button in the menu
        driver.find_element(By.XPATH, time_table_navbar_xpath).click()
        print("clicked on timetable.")
        wait

username = #enter username here
password = #enter password here

#-----initial common activity------
login(username, password)  # logs in
close_popups()  # closes all popups
#----------------------------------

checkpoint = input("enter something to go ahead")
#***scraping my Classes timetable***
days_span = 7
for i in range(1, days_span):
    page_soup = page_content_to_file("amizone.html")
    date = driver.find_element(By.XPATH, "//*[@id='calendar']/div[1]/div[3]/h2").text
    print(date)
    period_data = []
    myClasses_table = page_soup.find("table", {"class": "fc-list-table"})
    #print(myClasses_table)
    if(myClasses_table != None):
        trs_of_classes = myClasses_table.findAll("tr", {"class":"fc-list-item class-schedule-color"})
        #print(trs_of_classes)
        for tr in trs_of_classes:
            class_time = tr.find("td", {"class":"fc-list-item-time fc-widget-content"}).text
            class_attendance = tr.find("td", {"class":"fc-list-item-marker fc-widget-content"}).span["style"]
            td_course_teacher_loc = tr.find("td", {"class":"fc-list-item-title fc-widget-content"})
            course_name = td_course_teacher_loc.find("span", {"class":"course-name"}).text.strip()
            teacher = td_course_teacher_loc.find("span", {"class":"course-teacher"}).text.strip()
            class_loc = td_course_teacher_loc.find("span", {"class":"course-location"}).text.strip()
            period_data.extend([class_time, class_attendance,course_name,teacher,class_loc])
            
            print(period_data)
            period_data.clear()
    else:
        print("no classes today")
    #click | css=.fc-icon-right-single-arrow |
    driver.find_element(By.CSS_SELECTOR, ".fc-icon-right-single-arrow").click()
    print("clicked on next")
    time.sleep(2)


#***go to next/prev date in myClasses***
prev_next_date = ""
while(prev_next_date != "end"):
    prev_next_date = input("type prev/next:")
    try:
        if(prev_next_date == "next"):
            # click | css=.fc-icon-right-single-arrow |
            driver.find_element(By.CSS_SELECTOR, ".fc-icon-right-single-arrow").click()
            print(driver.find_element(By.XPATH, "//*[@id='calendar']/div[1]/div[3]/h2").text)
            print("clicked on next")
        elif(prev_next_date == "prev"):
            # click | css=.fc-prev-button |
            driver.find_element(By.CSS_SELECTOR, ".fc-prev-button").click()
            print(driver.find_element(By.XPATH, "//*[@id='calendar']/div[1]/div[3]/h2").text)
            print("clicked on previous")
    except exceptions.NoSuchElementException as e:
        print(e, "unable to click. Something may be blocking the element")
    page_soup = page_content_to_file("amizone.html")
    myClasses_table = page_soup.find("table", {"class": "fc-list-table"})
    print(myClasses_table)

#   get info about classes and attendance marked from myclasses
# TODO: for a course check whether green or blue dot is shown
# ***clicking on the hamburger button and choosing timetable***

menu_click("timetable") #clicks on timetable in the menu
# ***scraping timetable***
# print(driver.find_element(By.CLASS_NAME, "tab-content").text)
# NOTE: no need to click on weekdays because all info is in the webpage
# NOTE: clicking on the tt loads only the current day's tt. if then you click once on any day webpage shows tt of whole week.(why?)
# for i in range(1,8): #iterating over all weekdays 1-7
    # weekday_xpath = "//*[@id='myTab3']/li[" + str(i) + "]/a" #concatenating string to make xpath for each weekday

# clicking on a day to get whole week's tt
# page_soup = page_content_to_file("amizone_tt_page.html")
weekday_xpath = "//*[@id='myTab3']/li[1]/a" #xpath of day no.1 of the week in the timetable at that time.
driver.find_element(By.XPATH, weekday_xpath).click()

period_data = [] #list to make sql statement
# scraping timetable data
page_soup = page_content_to_file()
divs_class_tab_pane = page_soup.findAll("div", {"class":"tab-pane"})  #finds and makes a list all the <div class="tab-pane in active" id="[day]">
for day_div in divs_class_tab_pane:    #selects each day's div from divs_class_tab_pane list
    print()
    day = day_div["id"].strip()    #gets the id attribute of div tag e.g <div class="tab-pane in active" id="Sunday"> returns the day
    print(day)
    try:
        # find all <div class="thumbnail timetable-box"> elements which contains p tags of details of a class
        div_thumbnail_timetable_box = day_div.findAll("div", {"class":"thumbnail timetable-box"})
        if(len(div_thumbnail_timetable_box) == 0):
            print("no classes alloted yet")
    except:
        print("no classes today")
    # selecting element one at a time from div_thumbnail_timetable_box
    for ttbox in div_thumbnail_timetable_box:   
        period_data.append(day) #appending day to list
        print()
        # get text from <p class="class-time"> the class time
        class_time = ttbox.find('p', {"class":"class-time"}).text.strip()
        period_data.append(class_time) #appending class time to list
        print(class_time)
        # get text from <p class="course-code"> the course code
        course_code = ttbox.find('p', {"class":"course-code"}).text.strip()
        period_data.append(course_code) #appending course_code to list
        print(course_code)
        # get text from <p class="course-teacher"> the course teacher
        course_teacher = ttbox.find('p', {"class":"course-teacher"}).text.strip()
        period_data.append(course_teacher) #appending course_teacher to list
        print(course_teacher)
        class_location = ttbox.find('p', {"class":"class-loc"}).text.strip()
        period_data.append(class_location)
        print(class_location)
        print(period_data)

        # connecting to database #TODO: exception handliling required here
        mydb = db.establish_con("localhost", "manik", "sweetbread","amizone")
        script = "','".join(period_data)
        period_data.clear()
        query = "INSERT INTO amizone.tt_data(`day`,`time`,course,teacher, class_loc) VALUES ('" + script + "');"
        # running MySQL query in the database
        mycursor = db.run_sql(mydb, query)
        # mycursor = db.run_sql(mydb, "SELECT * FROM amizone.tt_data;")
        mydb.commit()

# extra code
    # date = driver.find_element(By.XPATH, "//*[@id='calendar']/div[1]/div[3]/h2").text #to get the date of myClasses
    # print(calendar_date_element.text)
    # driver.find_element(By.ID, "ModalPopAmityHostel").click()
    # time.sleep(5)
    # driver.find_element(By.ID, "StudentSatisfactionPop").click()
    # url = driver.current_url
# driver.quit()
print("execution time: %ss" % (round(time.time() - start_time, 5)))
#    time.sleep(10)
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
