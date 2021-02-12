# Скласти програму, яка читає прогноз погоди у заданому місті з сайту
# meteoprog.ua та зберігає у файлі Excel у окремому рядку поточну дату та прогнози
# температури та вологості повітря протягом поточного дня (вночі, вранці, вдень, увечері).
# Запит на погоду у заданому місті: http://www.meteoprog.ua/ua/weather/<місто>/
# Наприклад, http://www.meteoprog.ua/ua/weather/Kyiv/


# <div class="currentSelectDay"><span style="text-transform: capitalize;">п'ятниця</span>, 12 лютого </div> -- день

import openpyxl
import requests
from bs4 import BeautifulSoup


outfile = "weather.xlsx"
url = "http://www.meteoprog.ua/ua/weather/"
city = "Kyiv"
full_url = url + city

response = requests.get(full_url)

soup = BeautifulSoup(response.text, 'lxml')

# print(soup)
result_row = [city]

detail = soup.find('div', class_="detailBlockWeather")
day = detail.find('div', class_="bgDay").text
result_row.append(day)


# night
temp = detail.find('div', class_="temp")

factor = detail.find('div', class_="factor", title="Вологість")
humidity = factor.find('div', class_="floatL styleFactor")

night = ' '.join((temp.text + humidity.text).split('\n'))
result_row.append(night)


# morning - midday - evening
mains = soup.findAll('div', class_="someDayWeather floatL")
for i in range(3):
    main = mains[i]
    temp = main.find('div', class_="temp")

    factor = main.find('div', class_="factor", title="Вологість")
    humidity = factor.find('div', class_="floatL styleFactor")

    data = ' '.join((temp.text + humidity.text).split('\n'))
    result_row.append(data)

print(result_row)
wb = openpyxl.Workbook()
ws = wb["Sheet"]

ws.append(result_row)

wb.save("output.xlsx")
