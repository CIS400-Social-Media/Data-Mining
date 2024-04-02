from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define OAuth 2.0 scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

# Define YouTube Data API key
API_KEY = "AIzaSyBbNNLvSYXVFeukr_UDrXtPi4lbt8Y86Uo"

# Initialize the YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def search_channels_by_location(query):
    # Make API request to search for channels based on the query
    request = youtube.search().list(part="snippet", q=query, type="channel", maxResults=50)
    response = request.execute()
    return response.get("items", [])

def extract_channel_ids(channels):
    # Extract channel IDs from the search results
    channel_ids = [channel["id"]["channelId"] for channel in channels]
    return channel_ids

def get_channel_description(channel_id):
    # Make API request to retrieve channel details
    request = youtube.channels().list(part="snippet", id=channel_id)
    response = request.execute()
    channel_description = response["items"][0]["snippet"]["description"]
    return channel_description

def filter_channels_by_location(channels, location_keywords):
    filtered_channels = []
    for channel in channels:
        channel_description = get_channel_description(channel)
        if any(keyword in channel_description.lower() for keyword in location_keywords):
            filtered_channels.append((channel, channel_description))
    return filtered_channels

if __name__ == "__main__":
    # Search for channels based on location-related keywords
    location_query = "travel vlog"
    channels = search_channels_by_location(location_query)

    # Extract channel IDs from the search results
    channel_ids = extract_channel_ids(channels)

    # Filter channels based on location keywords in descriptions
    location_keywords = ["location", "city", "country"]
    filtered_channels = filter_channels_by_location(channel_ids, location_keywords)

    print("Filtered Channels:")
    for channel_id, description in filtered_channels:
        print(f"Channel ID: {channel_id}")
        print(f"Location: {description}")
