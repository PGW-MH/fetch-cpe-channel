import json
import feedparser
from datetime import datetime

CHANNELS = {
    'ZH': 'https://www.youtube.com/feeds/videos.xml?channel_id=UCbELDDHGqMbjsA_4Kyd7vMw',
    'EN': 'https://www.youtube.com/feeds/videos.xml?channel_id=UCm0zMBHYwYGzsYnrqE0kk1g',
    'KID': 'https://www.youtube.com/feeds/videos.xml?channel_id=UCQ7Z5kbCT5uv4IyYHVwA3sg'
}

latest_video = None

for chan, url in CHANNELS.items():
    feed = feedparser.parse(url)
    if not feed.entries:
        continue

    entry = feed.entries[0]
    published = datetime(*entry.published_parsed[:6])

    if latest_video is None or published > latest_video['published']:
        latest_video = {
            'channel': chan,
            'video_id': entry.yt_videoid,
            'title': entry.title,
            'published': published
        }

if latest_video is None:
    raise Exception('No videos found in any feed')

latest_video['published'] = latest_video['published'].isoformat()
with open('latest.json', 'w', encoding='utf-8') as f:
    json.dump(latest_video, f, ensure_ascii=False)
