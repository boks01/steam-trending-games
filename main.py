from selenium import webdriver
import datetime as dt
import time
import requests

# var
path = "C:\selenium_web_driver\chromedriver.exe"
link = "https://steamdb.info/"
driver = webdriver.Chrome(executable_path=path)
trending_game = []
now_date = dt.datetime.now()
date = now_date.strftime("%d-%B(%m)-%Y")
# var
# selenium code
driver.get(link)

time.sleep(2)
for i in range(5):
    game_name = driver.find_element_by_xpath(f'//*[@id="main"]/div[2]/div[1]/div[2]/table/tbody/tr[{i+1}]/td[2]/a').text
    player_now = driver.find_element_by_xpath(f'//*[@id="main"]/div[2]/div[1]/div[2]/table/tbody/tr[{i+1}]/td[4]').text
    data = {
        "name":game_name,
        "players_now":f"{player_now} players"
    }
    trending_game.append(data)

driver.quit()
# selenium code
# sheety code
sheety_link = "https://api.sheety.co/073f31df6c60be1e403436d7f3df689e/hotGamesInSteam/data"
for i in range(len(trending_game)):
    trending_game_name = trending_game[i]['name']
    trending_game_players = trending_game[i]['players_now']
    params = {
        'datum':{
            "date":date,
            "name":trending_game_name,
            "players":trending_game_players,
        }
    }
    post_request = requests.post(sheety_link, json=params)
    print(post_request.text)
print('done')
# sheety code