from src.sources import active_feeds
from src.entities import entities

print("\n----------------------\n", "Sources", "\n----------------------\n")
for feed in active_feeds:
    print(feed.feed.title)
    for feed_entry in feed.entries:

        for entity in entities:
            entity.count += entity.matches(feed_entry.title)

print("\n----------------------\n", "Entity Frequency", "\n----------------------\n")
for entity in entities:
    print(entity, ": ", entity.count)
