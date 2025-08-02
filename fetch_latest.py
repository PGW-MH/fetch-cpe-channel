import json
import feedparser


FEED_URL = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCbELDDHGqMbjsA_4Kyd7vMw'
feed = feedparser.parse(FEED_URL)

if not feed.entries:
    raise Exception('No videos found in the feed')

latest = feed.entries[0]
video_id = latest.yt_videoid

data = {
    'video_id': video_id
}

with open('latest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
