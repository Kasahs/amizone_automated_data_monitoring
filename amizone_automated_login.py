#import sys
import time
import db
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC

#TODO: try to get info without opening browser(not possible)
#TODO: close all pop-ups without specifying name(done)
#TODO: find the div id for the corresponding close button(done)
#TODO: extract data from amizone using beautifulSoup
#TODO: add data to database using mysql
#TODO: make a mechanism to navigate myclasses through input and get data
#TODO: figure out how to make useful information from data
#TODO: organize code
#TODO: do exception handling of the code
#NOTE: program doesn't work if window is minimized

#while(True):
#----setting up chrome driver----
chromedriver = "/usr/share/chromedriver/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.set_window_size(800, 1000)
#driver.maximize_window()
#wait = WebDriverWait(driver, 10)
url = "https://student.amizone.net"
driver.get(url) #getting amizone.net
#function that enters login credentials
def login(username, password):
    try:
    #type | name=_UserName
        driver.find_element(By.NAME, "_UserName").send_keys(username)
    #type | name=_Password
        driver.find_element(By.NAME, "_Password").send_keys(password)
    #click | css=#loginform .login100-form-btn |  
        driver.find_element(By.CSS_SELECTOR, "#loginform .login100-form-btn").click()
    except:
        print("couldn't complete login")
#func to close popups
def close_popups():
    try:
    #   getting names of divs having class 'modal fade in'
    #TODO:search for name attribute of div having class 'modal fade in'
        driver.implicitly_wait(10)
        content = driver.page_source
        page_soup = BeautifulSoup(content,"html.parser")
        popup_divs = page_soup.find_all('div', {"class":"modal fade in"})
    #print(popup_divs)
        popups_name = []
        for div in popup_divs:
            popups_name.append(div['id'])
            print(popups_name)
        if(len(popups_name) == 0):
            print("no popups found")
        else:
            print("starting")
        #   clicking to close pop-ups
            for name in reversed(popups_name):
                xpath = "//div[@id='" + name + "']//button[@class='close']"
                print(xpath)
                driver.find_element(By.XPATH, xpath).click()
            print("clicks complete")
            #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ModalPopAmityHostel button.btn"))).click()
            #driver.execute_script("arguments[0].click()", driver.find_element_by_css_selector("#StudentSatisfactionPop button.btn"))
            #click | id=ModalPopAmityHostel |  
            #driver.find_element(By.XPATH, "//div[@id='ModalPopAmityHostel']//button[@class='close']").click()
            #click | id=StudentSatisfactionPop | 
            #driver.find_element(By.XPATH, "//div[@id='StudentSatisfactionPop']//button[@class='close']").click()
    except:
        print("error occured while closing popups")

start_time = time.time()    #stores time at which program starts
#----------FUNCTION CALLS----------
login("username", "password") #login
close_popups() #close all popups
#----------------------------------

menu_toggler_xpath = "//*[@id='menu-toggler']" #xpath of the menu toggler(hamburger button)
#   clicking on the hamburger button on top left corner
driver.find_element(By.XPATH, menu_toggler_xpath).click()
time_table_navbar_xpath = "//*[@id='10']" #xpath of the timetable option in menu
#   clicking on the timetable button in the menu
driver.find_element(By.XPATH, time_table_navbar_xpath).click()

#   scraping timetable
# print(driver.find_element(By.CLASS_NAME, "tab-content").text)
#NOTE: no need to click on weekdays because all info is in the webpage
#NOTE: just clicking on the tt loads only the current day's tt. if then you click once on any day webpage shows tt of whole week.(why?)
#for i in range(1,8): #iterating over all weekdays 1-7
    #weekday_xpath = "//*[@id='myTab3']/li[" + str(i) + "]/a" #concatenating string to make xpath for each weekday
#clicking on a day to get whole week's tt
weekday_xpath = "//*[@id='myTab3']/li[1]/a" #xpath of day no.1 of the week in the timetable at that time.
driver.find_element(By.XPATH, weekday_xpath).click()

#   go to next/prev date in myClasses------
#date_prev_next = ""
#while(date_prev_next != "end"):
    #date_prev_next = input("type prev/next:")
    #if(date_prev_next == "next"):
        # click | css=.fc-icon-right-single-arrow | 
    #    driver.find_element(By.CSS_SELECTOR, ".fc-icon-right-single-arrow").click()
    #    print(driver.find_element(By.XPATH, "//*[@id='calendar']/div[1]/div[3]/h2").text)
    #if(date_prev_next == "prev"):
    #    # click | css=.fc-prev-button |
    #    driver.find_element(By.CSS_SELECTOR, ".fc-prev-button").click()
    #    print(driver.find_element(By.XPATH, "//*[@id='calendar']/div[1]/div[3]/h2").text)


#   get info about classes and attendance marked from myclasses-----

#TODO: for a course check whether green or blue dot is shown
#date = driver.find_element(By.XPATH, "//*[@id='calendar']/div[1]/div[3]/h2").text
#print(calendar_date_element.text)
#driver.find_element(By.ID, "ModalPopAmityHostel").click()
#time.sleep(5)
#driver.implicitly_wait(5000)
#driver.find_element(By.ID, "StudentSatisfactionPop").click()
#url = driver.current_url
#driver.find_element(By.CLASS_NAME, "close").click()
#driver.implicitly_wait(5000)
#   write page content to a file
#NOTE: how to srape data from timetable for any day?
content = driver.page_source
#print(content)
page_soup = BeautifulSoup(content, "html.parser")
page_soup_text = BeautifulSoup.prettify(page_soup)
with open("amizone.html", "w") as file:
    file.write(page_soup_text)
period_data = [] #list to make sql statement
#scraping timetable data
divs_class_tab_pane = page_soup.findAll("div", {"class":"tab-pane"})  #finds and makes a list all the <div class="tab-pane in active" id="[day]">
for day_div in divs_class_tab_pane:    #selects each day's div from divs_class_tab_pane list
    print()
    day = day_div["id"].strip()    #gets the id attribute of div tag e.g <div class="tab-pane in active" id="Sunday"> returns the day
    print(day)
    try:
        #find all <div class="thumbnail timetable-box"> elements which contains p tags of details of a class
        div_thumbnail_timetable_box = day_div.findAll("div", {"class":"thumbnail timetable-box"})
        if(len(div_thumbnail_timetable_box) == 0):
            print("no classes alloted yet")
    except:
        print("no classes today")
    #selecting element one at a time from div_thumbnail_timetable_box
    for ttbox in div_thumbnail_timetable_box:   
        period_data.append(day) #appending day to list
        print()
        #get text from <p class="class-time"> the class time
        class_time = ttbox.find('p', {"class":"class-time"}).text.strip()
        period_data.append(class_time) #appending class time to list
        print(class_time)
        #get text from <p class="course-code"> the course code
        course_code = ttbox.find('p', {"class":"course-code"}).text.strip()
        period_data.append(course_code) #appending course_code to list
        print(course_code)
        #get text from <p class="course-teacher"> the course teacher
        course_teacher = ttbox.find('p', {"class":"course-teacher"}).text.strip()
        period_data.append(course_teacher) #appending course_teacher to list
        print(course_teacher)
        class_location = ttbox.find('p', {"class":"class-loc"}).text.strip()
        period_data.append(class_location)
        print(class_location)
        print(period_data)

        #connecting to database #TODO: exception handliling required here
        mydb = db.establish_con("localhost", "manik", "sweetbread","amizone")
        script = "','".join(period_data)
        period_data.clear()
        query = "INSERT INTO amizone.tt_data(`day`,`time`,course,teacher, class_loc) VALUES ('" + script + "');"
        #running MySQL query in the database
        mycursor = db.run_sql(mydb, query)
        #mycursor = db.run_sql(mydb, "SELECT * FROM amizone.tt_data;")
        mydb.commit()
#driver.quit()
print("execution time: %ss" % (round(time.time() - start_time, 5)))
#    time.sleep(10)
