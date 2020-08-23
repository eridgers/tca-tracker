import csv
import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# prepare file - change to create new one each week?
# with open('test.csv', 'w') as f:
#         f.write("Date, Time, Climbers \n")

print("imported")
# date time things
currentDateTime = datetime.datetime.now()
minute = currentDateTime.minute
hour = currentDateTime.hour
day = currentDateTime.day
month = currentDateTime.month
year = currentDateTime.year
weekday = currentDateTime.weekday() # 5,6 for weekend

print("set times")
timeRun = str(hour) + ":" + str(minute)
dateRun = str(year) + "-" + str(month) + "-" + str(day)
print("real time variables")
# check time is valid for opening hours
# i.e. weekend 9-6  weekday 7-22
if hour < 7 or hour > 22:
   quit()
elif weekday > 4:
    if hour < 9 or hour > 18:
        quit()

# open browser and navigate webpage
# driver = webdriver.Firefox(executable_path=r'C:\Users\Andrew\Desktop\geckodriver\geckodriver.exe')
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver\geckodriver.exe', service_log_path=r'C:\temp\geckodriver\geckodriver.log')
url = "https://portal.rockgympro.com/portal/public/d0f355e237dda999f3112d94d3c762c7/occupancy?&iframeid=occupancyCounter&fId="
driver.get(url)
print("got the driver")
# select TCA from list code = BRI
select = Select(driver.find_element_by_id('gym-switcher'))
select.select_by_value("BRI")
print("changed input")
# we need to wait
time.sleep(10)
print("waited")
# extract data from graphic
climbers = driver.find_element_by_id("count")
capacity = driver.find_element_by_id("capacity")
print("got elements")
# throw error is capacity != 'of 115'
# if capacity != 'of 115':
#     with open('result.csv', 'a') as f:
#         f.write("error on run, capacity was not 115, was instead "+ capacity.text)
#     driver.quit()

# print results
print(climbers.text + " : " + capacity.text)
with open(r'C:\temp\geckodriver\tca\result.csv', 'a') as f:
    f.write(dateRun + "," + timeRun + "," + climbers.text + "," + capacity.text + "\n")

# close browser
driver.quit()