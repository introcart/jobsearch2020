import requests
from bs4 import BeautifulSoup
import csv

webpage_response = requests.get("https://www.thinkful.com/blog/top-30-u-s-cities-to-become-a-web-developer-in/")

webpage = webpage_response.content


soup = BeautifulSoup(webpage, "html.parser")
best_cities = []
soup.find_all("td")
cities = soup.find_all("tr")
for city in cities:
    city_rank = city.select("td")[0].get_text()
    city_location = city.select("td")[1].get_text()
    jobs = city.select("td")[2].get_text()
    idx = city_location.find(',')
    city = city_location[:idx]
    state = city_location[idx+2:]
    city = {'rank': city_rank, 'city': city, 'state': state, 'jobs': jobs}
    best_cities.append(city)
new_best_cities = best_cities[1:]
with open('best_web_dev_cities.csv', mode='w', newline="") as csv_file:
    cols = ["rank", "city", "state", "jobs"]
    writer = csv.DictWriter(csv_file, fieldnames=cols)
    writer.writeheader()
    writer.writerows(new_best_cities)






