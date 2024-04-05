from googleapiclient.discovery import build

# Define YouTube Data API key
API_KEY = "AIzaSyBbNNLvSYXVFeukr_UDrXtPi4lbt8Y86Uo"

# Initialize the YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_country_codes():
    # Make API request to retrieve supported regions (countries)
    request = youtube.i18nRegions().list(part="snippet", hl="en_US")
    response = request.execute()
    country_codes = {region["snippet"]["gl"]: region["snippet"]["name"] for region in response["items"]}
    return country_codes

def get_trending_videos(country_code, max_results=10):
    # Make API request to retrieve trending videos
    request = youtube.videos().list(part="snippet", chart="mostPopular", regionCode=country_code, maxResults=max_results)
    response = request.execute()
    trending_videos = [(video["snippet"]["title"], video["snippet"]["channelTitle"]) for video in response["items"]]
    return trending_videos

if __name__ == "__main__":
    # Get country codes and names
    country_codes = get_country_codes()

    # Get trending videos for each country
    for country_code, country_name in country_codes.items():
        print(f"Trending Videos in {country_name}:")
        trending_videos = get_trending_videos(country_code)
        for i, (video_title, channel_title) in enumerate(trending_videos, 1):
            print(f"{i}. {video_title} by {channel_title}")
        print()