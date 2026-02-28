from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd

URL = "https://www.nba.com/stats"


#SETUP THE SELENIUM

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


#NAVIGATE THROUGH WEBSITE AND EXTRACT THE SEASON STATE

driver.get(URL)

reject_b = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'onetrust-reject-all-handler')))
reject_b.click()

season_state_b = driver.find_element(By.XPATH, value="//button[text()='SEASON LEADERS']")
season_state_b.click()

state_players_category = driver.find_elements(By.CSS_SELECTOR, value='.LeaderBoardWithButtons_lbwbCardWrapper__re1TJ div a h2')
headers_list = [header.text for header in state_players_category]

state_players_name = driver.find_elements(By.CSS_SELECTOR, value='.Columns_left__XkWXE section div div div div table tbody tr td a')
names_list = [name.text for name in state_players_name][:45]

state_players_value = driver.find_elements(By.CLASS_NAME, value='LeaderBoardWithButtons_lbwbCardValue__5LctQ')
values_list = [value.text for value in state_players_value][:45]

#ORGANIZE THE DATA IN DICTIONARY

expand_category = [category.text for category in state_players_category for n in range(5)]
rank_list = [1, 2, 3, 4, 5] * 9
data = {
    "Category": expand_category,
    "Name": names_list,
    "value": values_list,
    "Rank": rank_list
}

#CONVERT DATA IN .CSV FORMAT

df = pd.DataFrame(data)
df.to_csv('nba_players_season_state.csv', index=False)

driver.close()
