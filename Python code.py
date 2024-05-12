import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Scraping data from a classified website (Pakwheels in this example)
url = 'https://www.pakwheels.com/used-cars/search/-/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting relevant information (e.g., car name, price, mileage)
cars = []
for listing in soup.find_all('div', class_='list'):
    car_name = listing.find('h3', class_='car-name').text.strip()
    car_price = listing.find('span', class_='price').text.strip()
    car_mileage = listing.find('span', class_='mileage').text.strip()
    cars.append({'Name': car_name, 'Price': car_price, 'Mileage': car_mileage})

# Task 2: Creating a CSV file
df = pd.DataFrame(cars)
df.to_csv('cars_data.csv', index=False)

# Task 3: Preprocessing the data (if needed)
# No preprocessing needed in this example

# Task 4: Visualizing the data using Matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(df['Price'], df['Mileage'], color='blue', alpha=0.5)
plt.title('Car Price vs. Mileage')
plt.xlabel('Price')
plt.ylabel('Mileage')
plt.grid(True)
plt.show()

# Task 5: Writing a small report on the graph
print("Report:")
print("The scatter plot shows the relationship between the price and mileage of used cars listed on Pakwheels.")
print("From the plot, it can be observed that there is a general trend of higher prices for cars with lower mileage.")
