import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # print(df)

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    x_2050 = np.arange(1880, 2051)
    plt.plot(x_2050, res.intercept + res.slope * x_2050, 'r')

    # Create second line of best fit
    x = df[df['Year'] >= 2000]['Year']
    y = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    x_2050 = np.arange(2000, 2051)
    plt.plot(x_2050, res.intercept + res.slope * x_2050, 'b')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()