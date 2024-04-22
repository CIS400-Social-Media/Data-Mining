import json
import pandas as pd

# Read data from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Convert data to DataFrame
youtube_df = pd.DataFrame(data, columns=['Country', 'Video Title', 'Category', 'Sentiment'])

# Define a dictionary to map sentiment categories to numerical values
sentiment_mapping = {'Positive': 100.0, 'Negative': 0.0, 'Neutral': 50.0}

# Map sentiment categories to numerical values
youtube_df['Sentiment'] = youtube_df['Sentiment'].map(sentiment_mapping)

# Load the life expectancy dataset
life_expectancy_data = pd.read_csv("lex.csv")

# Initialize an empty dictionary to store correlation results for each category
correlation_results = {}

# Iterate over unique categories
for category in youtube_df['Category'].unique():
    # Filter YouTube DataFrame for the current category
    category_df = youtube_df[youtube_df['Category'] == category]
    
    # Merge category DataFrame with life expectancy dataset on 'Country'
    merged_df = pd.merge(left=category_df, right=life_expectancy_data, how='inner', left_on='Country', right_on='country')
    
    # Remove rows with NaN values
    merged_df = merged_df.dropna(subset=['2024', 'Sentiment'])
    
    # Calculate correlation between life expectancy and sentiment for the current category
    correlation = merged_df['2024'].corr(merged_df['Sentiment'])
    
    # Store correlation result in the dictionary
    correlation_results[category] = correlation

    merged_df.to_csv(f"./output/{category}_life_expectancy.csv")

# Print correlation results for each category
for category, correlation in correlation_results.items():
    print(f"Correlation between Life Expectancy and Sentiment Analysis for {category}: {correlation}")

# Save correlation results to a CSV file
correlation_df = pd.DataFrame.from_dict(correlation_results, orient='index', columns=['Correlation'])
correlation_df.to_csv("category_life_expectancy_correlation.csv")