import pandas as pd
import matplotlib.pyplot as plt

bnb = pd.read_csv('BNB.csv')
cake = pd.read_csv('xmr.csv')

# Get the date column from the Cake DataFrame
date = cake["Date"]

# Get the price columns from the Binance and Cake DataFrames
bnb1 = bnb["Price"]
cake1 = cake["Price"]

# Create the line plots
plt.plot(date, bnb1, label="Binance")
plt.plot(date, cake1, label="Cake")

# Set the x and y labels
plt.xlabel("Month-wise from Aug-2022 to Aug-2023")
plt.ylabel("Price in USD")

# Add a legend to the top right corner of the plot
plt.legend(loc="upper right")

# Set the title of the plot
plt.title("Price Comparison of Two Cryptocurrencies")

# Display the plot
plt.show()
