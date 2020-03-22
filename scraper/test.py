# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# import time
# chromedriver = "/usr/share/chromedriver/chromedriver"
# driver = webdriver.Chrome(chromedriver)
# def main():
#     print("hello world")
#     #driver.get("https://student.amizone.net")
#     #driver.find_element(By.NAME, "_UserName").send_keys("7071804")
#     #driver.find_element(By.NAME, "_Password").send_keys("gulabjamun")
#     #driver.find_element(By.CSS_SELECTOR, "#loginform .login100-form-btn").click()
#     #driver.implicitly_wait(10)
#     #11 | click | id=ModalPopAmityHostel |  
#     #driver.find_element(By.ID, "ModalPopAmityHostel").click()
#     # 11 | click | id=StudentSatisfactionPop |  | 
#     #driver.find_element(By.ID, "StudentSatisfactionPop").click()

# start_time = time.time()
# main()
# print("execution time: %s s" % (round(time.time() - start_time , 5)))

import time
start_time = time.time()
def isPrime(n): #to check whether number is prime
    if(n <= 1):
        return False
    if(n % 2 == 0 or n % 3 == 0) : 
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True
    # i = 5
    # while(i * i <= n) : 
    #     if (n % i == 0 or n % (i + 2) == 0) : 
    #         return False
    #     i = i + 6
    # return True
    
if(isPrime(157)):
    print("it's prime!")
else:
    print("it's not prime")
    
def prime_in_interval(*argv): #to return a list of prime numbers within an interval
    prime_list=[] #append all prime numbers in the list and return it
    if(len(argv) > 2): #argv to have variable arguments
        raise NameError("prime_in_interval doesn't take more than 2 arguments") #raises error
    if(len(argv) == 1):
        start = 1
        end = argv[0]
    else:
        start = argv[0]
        end = argv[1]
    for num in range(start, end + 1):
        if(isPrime(num)):
            prime_list.append(num)
    return prime_list

for i in prime_in_interval(2000):
    print(i, end =",")
print()
print(round(time.time() - start_time,10))