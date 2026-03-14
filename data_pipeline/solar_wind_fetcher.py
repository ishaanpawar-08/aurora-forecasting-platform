import requests

url = "https://services.swpc.noaa.gov/products/solar-wind/mag-1-day.json"

response = requests.get(url)

data = response.json()

print("Latest IMF data:")
print(data[-1])
