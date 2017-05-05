#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

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
  thumbnails =[]
  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    videos.append("%s" % (search_result["snippet"]["title"]))
    videoids.append("%s" % (search_result["id"]["videoId"]))
    thumbnails.append("%s" % (search_result["snippet"]["thumbnails"]["high"]["url"]))
  print ("Titles:\n", "\n".join(videos), "\n")
  print ("Video Ids:\n", "\n".join(videoids), "\n")
  print ("Thumbnails:\n", "\n".join(thumbnails), "\n")
  return videos, videoids


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=5)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except (HttpError, e):
    print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
