#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import schedule
import time
from time import sleep
from rooms import roomYouWant, timeYouWant, backupRoom, backupTime, backupRoom2, backupTime2

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def main():
    schedule_booking()

def look_for_room():

    driver.get("https://juilliard.asimut.net/public/")

    driver.implicitly_wait(15)
    driver.find_element_by_id('okta-signin-username').send_keys("???@juilliard.edu")
    driver.find_element_by_id('okta-signin-password').send_keys("")

    driver.find_element_by_id("okta-signin-submit").submit()

    driver.implicitly_wait(5)

    driver.find_element_by_xpath("//a[@href='?akt=eventsignup']").click()

def go_get_room():

    print("Trying to get your room now!")

    driver.find_element_by_xpath("//h1[@class='filter-title']" and "//h1[@data-itemid='5']").click()

    driver.implicitly_wait(20)

    try:
        room = driver.find_element_by_xpath('//div[@class="event-time"]/p[text()="' + timeYouWant + '"]/../../div[@class="event-body"]/p[@class="event-name"]/span/a[text()="' + roomYouWant + ' (Practice Room)"]')
    except NoSuchElementException:
        print("Couldn't get first room")


    #go to first room and book it
    driver.execute_script("return arguments[0].scrollIntoView();", room)

    action = ActionChains(driver)
    action.move_to_element_with_offset(room, 0, 47).double_click().perform()

    sleep(0.8)
    
    
    
    try:
        room2 = driver.find_element_by_xpath('//div[@class="event-time"]/p[text()="' + backupTime + '"]/../../div[@class="event-body"]/p[@class="event-name"]/span/a[text()="' + backupRoom + ' (Practice Room)"]')
    except NoSuchElementException:
        print("Couldn't get second room")
    
    #go to SECOND room and book it
    driver.execute_script("return arguments[0].scrollIntoView();", room2)

    action2 = ActionChains(driver)
    action2.move_to_element_with_offset(room2, 0, 47).double_click().perform()
    
    sleep(0.8)



    try:
        room3 = driver.find_element_by_xpath('//div[@class="event-time"]/p[text()="' + backupTime2 + '"]/../../div[@class="event-body"]/p[@class="event-name"]/span/a[text()="' + backupRoom2 + ' (Practice Room)"]')
    except NoSuchElementException:
        print("Couldn't get 3rd room")
      
    
    #go to THIRD room and book it
    driver.execute_script("return arguments[0].scrollIntoView();", room3)

    action3 = ActionChains(driver)
    action3.move_to_element_with_offset(room3, 0, 47).double_click().perform()


    #exit after some time has passed
    sleep(20)
    driver.quit()
    exit()
    
    

def schedule_booking():
    schedule.every().day.at("23:59").do(look_for_room)
    schedule.every().day.at("00:00").do(go_get_room)

    while True:
        schedule.run_pending()
        time.sleep(1)

main()