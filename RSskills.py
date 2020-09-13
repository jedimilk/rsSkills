from bs4 import BeautifulSoup
import requests

url = 'https://apps.runescape.com/runemetrics/app/levels/player/Jedi+Milk'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='a-xp-levels-table__row-thieving')

print(results.prettify())

#hello austin :)))))))))

#hello again
