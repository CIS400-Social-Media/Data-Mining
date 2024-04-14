from googleapiclient.discovery import build
from textblob import TextBlob
from googleapiclient.errors import HttpError

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

def get_video_category(video_id):
    # Make API request to retrieve video details
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    if response["items"]:
        category_id = response["items"][0]["snippet"]["categoryId"]
        return get_category_name(category_id)
    return None

def get_category_name(category_id):
    # Make API request to retrieve category details
    request = youtube.videoCategories().list(part="snippet", id=category_id)
    response = request.execute()
    if response["items"]:
        return response["items"][0]["snippet"]["title"]
    return None

def get_trending_videos(country_code, max_results=10):
    # Make API request to retrieve trending videos
    request = youtube.videos().list(part="snippet", chart="mostPopular", regionCode=country_code, maxResults=max_results)
    response = request.execute()
    trending_videos = [(video["id"], video["snippet"]["title"], video["snippet"]["channelTitle"]) for video in response["items"]]
    return trending_videos

def analyze_video_comments(video_id):
    try:
        # Make API request to retrieve video comments
        request = youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=10)
        response = request.execute()

        # Extract comments from the response
        comments = [comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for comment in response["items"]]

        # Perform sentiment analysis
        positive_count = 0
        negative_count = 0
        for comment in comments:
            analysis = TextBlob(comment)
            if analysis.sentiment.polarity > 0:
                positive_count += 1
            elif analysis.sentiment.polarity < 0:
                negative_count += 1

        # Determine overall sentiment
        if positive_count > negative_count:
            return "Positive"
        elif positive_count < negative_count:
            return "Negative"
        else:
            return "Neutral"
    except HttpError as e:
        if e.resp.status == 403:
            return "Comments Disabled"
        else:
            raise

if __name__ == "__main__":
    # Get country codes and names
    country_codes = get_country_codes()

    # Get trending videos for each country
    for country_code, country_name in country_codes.items():
        print(f"Trending Videos in {country_name}:")
        trending_videos = get_trending_videos(country_code)
        for i, (video_id, video_title, channel_title) in enumerate(trending_videos, 1):
            category_name = get_video_category(video_id)
            print(f"{i}. {video_title} by {channel_title} - {category_name}")
            # Analyze comments
            sentiment = analyze_video_comments(video_id)
            print(f"   Sentiment: {sentiment}")
        print()

