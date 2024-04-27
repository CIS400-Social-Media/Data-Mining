import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# Selects which graph to show
show = 5

if len(sys.argv) == 2:
    show = int(sys.argv[1])

# Gets data from csv
if(show == 1):
    data = pd.read_csv('output/Gaming_life_expectancy.csv')
elif(show == 2):
    data = pd.read_csv('output/News & Politics_happiness.csv')
elif(show == 3):
    data = pd.read_csv('output/Sports_happiness.csv')
elif(show == 4):
    data = pd.read_csv('output/Pets & Animals_freedom.csv')
elif(show == 5):
    data = pd.read_csv('output/Entertainment_happiness.csv')

# Makes a scatterplot based on graph chosen
if(show == 1):
    # Gets the slope (a) and the y intercept (b) using polyfit
    a, b = np.polyfit(data['Sentiment'], data['2024'], 1)
    # Plots the scatterplot
    plt.scatter(data['Sentiment'], data['2024'])
    # Plots the line of best fit
    plt.plot(data['Sentiment'], a*data['Sentiment']+b, 'r')
    # Labels the graph and axis accordingly
    plt.xlabel("Sentiment")
    plt.ylabel("Life Expectancy")
    plt.title("Gaming - Sentiment vs Life Expectancy")
    # Makes the x-axis only show the three sentiments
    plt.xticks([0,50,100])
elif(show == 2):
    a, b = np.polyfit(data['Sentiment'], data['2022'], 1)
    plt.scatter(data['Sentiment'], data['2022'])
    plt.plot(data['Sentiment'], a*data['Sentiment']+b, 'r')
    plt.xlabel("Sentiment")
    plt.ylabel("Happiness")
    plt.title("News & Politics - Sentiment vs Happiness")
    plt.xticks([0,50,100])
elif(show == 3):
    a, b = np.polyfit(data['Sentiment'], data['2022'], 1)
    plt.scatter(data['Sentiment'], data['2022'])
    plt.plot(data['Sentiment'], a*data['Sentiment']+b, 'r')
    plt.xlabel("Sentiment")
    plt.ylabel("Happiness")
    plt.title("Sports - Sentiment vs Happiness")
    plt.xticks([0,50,100])
elif(show == 4):
    a, b = np.polyfit(data['Sentiment'], data['2022'], 1)
    plt.scatter(data['Sentiment'], data['2022'])
    plt.plot(data['Sentiment'], a*data['Sentiment']+b, 'r')
    plt.xlabel("Sentiment")
    plt.ylabel("Freedom Index")
    plt.title("Pets & Animals - Sentiment vs Freedom Index")
    plt.xticks([3.5,7])
elif(show == 5):
    a, b = np.polyfit(data['Sentiment'], data['2022'], 1)
    plt.scatter(data['Sentiment'], data['2022'])
    plt.plot(data['Sentiment'], a*data['Sentiment']+b, 'r')
    plt.xlabel("Sentiment")
    plt.ylabel("Happiness")
    plt.title("Entertainment - Sentiment vs Happiness")
    plt.xticks([0,50,100])

# Shows the graph
plt.show()