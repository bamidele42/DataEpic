import requests as r
import bs4 as _bs4
import re


def generate_content(cities):
    """ This function scapes and cleans weather data
    """
    content = []
    # iterate through the city list
    for i in cities:
        city = f"https://www.timeanddate.com/weather/nigeria/{i}"
        page = r.get(city)
        soup = _bs4.BeautifulSoup(page.content, "html.parser")
        # iterate through the weather info tags
        for x in soup.find("div", {"class": "bk-focus__info"}):
            content.append(x.text)
# regex for cleaning the scrape data
    location = re.compile(r"\bL......n:\s\w{1,6}")
    current_time = re.compile(
        r"C.....t\s\w{4}:\s\d{2}\s\w{3}\s\d{4},\s\d{2}:\d{2}:\d{2}")
    latest_time = re.compile(
        r"Lat..t\s\w{6}:\s\d{2}\s\w{3}\s\d{4},\s\d{2}:\d{2}")
    visibity = re.compile(r"Vis......y:\s\d{1,2}\W{1}\w{2}\d{1}\w{2}")
    pressure = re.compile(r"Pr.....e:\s\d{1,}\s\w{4}")
    humidity = re.compile(r"Hu.....y:\s\d{2}\W{1}")
    dew_point = re.compile(r"D.w\s\w{1,5}:\s\d{1,}\W{1,}")
    cities = []
    time = []
    lat_time = []
    visi = []
    pre = []
    hum = []
    dew = []
    for i in content:
        # print(i)
        cities.append(location.findall(i))
        time.append(current_time.findall(i))
        lat_time.append(latest_time.findall(i))
        visi.append(visibity.findall(i))
        pre.append(pressure.findall(i))
        hum.append(humidity.findall(i))
        dew.append(dew_point.findall(i))

    city_list = ["Location"]
    time_list = ["Current Time"]
    report_list = ["Latest Report"]
    pressure_list = ["Presure"]
    hum_list = ["Humidity"]
    dew_list = ["Dew Point"]

    loc = re.compile(r"\B\s\D{1,}")
    cur_time = re.compile(r"\B\s\d{1,}\s\w{1,}\s\d{1,},\s\d{1,}:\d{1,}:\d{1,}")
    report = re.compile(r"\B\s\d{1,}\s\w{1,}\s\d{1,}\W\s\d{1,}:\d{1,}")
    pressure = re.compile(r"\B\d{1,}\s\w{1,}")
    humidity = re.compile(r"\B\s\d{1,}\W")
    dew_point = re.compile(r"\B\s{1,}\d{1,}")
# regex for cleaning data to be saved in google sheet
    city_list.append(loc.findall(cities[0][0])[0].strip())
    city_list.append(loc.findall(cities[1][0])[0].strip())
    city_list.append(loc.findall(cities[2][0])[0].strip())

    time_list.append(cur_time.findall(time[0][0])[0].strip())
    time_list.append(cur_time.findall(time[1][0])[0].strip())
    time_list.append(cur_time.findall(time[2][0])[0].strip())

    report_list.append(report.findall(lat_time[0][0])[0].strip())
    report_list.append(report.findall(lat_time[1][0])[0].strip())
    report_list.append(report.findall(lat_time[2][0])[0].strip())

    pressure_list.append(pressure.findall(pre[0][0])[0].strip())
    pressure_list.append(pressure.findall(pre[1][0])[0].strip())
    pressure_list.append(pressure.findall(pre[2][0])[0].strip())

    hum_list.append(humidity.findall(hum[0][0])[0].strip())
    hum_list.append(humidity.findall(hum[1][0])[0].strip())
    hum_list.append(humidity.findall(hum[2][0])[0].strip())

    dew_list.append(dew_point.findall(dew[0][0])[0].strip())
    dew_list.append(dew_point.findall(dew[1][0])[0].strip())
    dew_list.append(dew_point.findall(dew[2][0])[0].strip())
# returb the clean data
    return city_list, time_list, report_list, pressure_list, hum_list, dew_list


result = generate_content(["Ibadan", "Lagos", "Jos"])
print(result)
