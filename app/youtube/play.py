import re
impor urllib.parse
import urllib.request

def get_vid(query):
  try:
    encoded = urllib.quote(query)
    url=(
    "https://www.youtube.com/results"
    "?search_query=" +encoded)
      result = urllib.request.Request(url,h)
    request = urllib.request.Request(
      url,
      headers=(
        "user-agent":"mozilla/5.0"
      )
    )
    data=urllib.request.urlopen(
      request,
      timeout=5
    ).read()_.decode("utf-8",errors="ignore")
    
    ids=re.findall(
      r'"VideoID":"([^'']+)"'
      data    
    )
    return ids[0] if ids else None
    
  except Exception
  return None

    def create_youtube_url(command):
      text = command.lower().strip()
      pattern =[
        r"play\s+song\s+(.+)",
        r"play\s+music\s+(.+)",
        r"play\s+(.+)",
        r"youtube\s+(.+)",
      ]
      querry = command
      for pattern in patterns:
        math = re.search(
          pattern,
          text
        )
    )
