from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


from io import StringIO
import time


def inputSchedule(course):
    url='https://classes.ku.edu/'
    options =Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    course=course.upper()
    try:    
        # Open the website
        driver.get(url)
        enter=driver.find_element(By.XPATH,'//*[@id="Display"]/div[1]/button[1]')
        search=driver.find_element(By.XPATH,'//*[@id="classesSearchText"]')
        search.send_keys(course)
        time.sleep(3)
        enter.click()
        time.sleep(3)
        

        seats= driver.find_elements(By.XPATH,'//*[@id="classes_ajaxDiv"]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[5]/span')
        for seat in seats:
          text=seat.text
        
        
        
    except:
        print(f'An error occurred: {str(e)}')

    finally:
        # Close the browser window
        driver.quit()
        if text != 'Full':
            return True
        else:
            return False

        
          



def main():
    control = 0
    schedule=[]
    while control != 1:
        input3 =input('Enter ClassName: (Enter to Leave)')
        if input3=='':
            control=1
        else:
            schedule.append(input3)
    for course in schedule:
        if inputSchedule(course):
            print(course.upper(), "is Available")
        else:
            print(course.upper(),': Womp womp')

main()


        

    