#!/usr/bin/python

from apiclient.discovery import build

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCYjeP3vDPBBQTdq9ru3-3OxMTZn7K0Knc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  # Call the search.list method to retrieve results matching the specified query term.
  search_response = youtube.search().list(
    q=options,
    part="id,snippet",
    type="video",
    maxResults=4
  ).execute()
  videos = []
  videoids = []
  for search_result in search_response.get("items", []):
    videos.append("%s" % (search_result["snippet"]["title"]))
    videoids.append("%s" % (search_result["id"]["videoId"]))
  print ("Titles:\n", "\n".join(videos), "\n")
  print ("Video Ids:\n", "\n".join(videoids), "\n")
  return videos, videoids
