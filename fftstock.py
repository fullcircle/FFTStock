import yfinance as yf

# Download stock data for AAPL from 2020-01-01 to 2021-01-01
stock_data = yf.download('NVDA', start='2024-01-01', end='2024-04-19')

# Display the downloaded data
print(stock_data.head())

import numpy as np
import pandas as pd
from scipy.fft import fft
import matplotlib.pyplot as plt

# Calculate daily returns
daily_returns = stock_data['Close'].pct_change().dropna()

# Perform FFT
fft_result = fft(daily_returns.values)
fft_magnitude = np.abs(fft_result)
fft_freq = np.fft.fftfreq(len(fft_magnitude))

# Plot the FFT results
plt.figure(figsize=(12, 6))
plt.plot(fft_freq, fft_magnitude, 'b')
plt.title('FFT of Stock Movements')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()
