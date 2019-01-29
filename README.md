# sensor.feedparser
RSS feed custom component for [Home Assistant](https://www.home-assistant.io/)

To get started put `/custom_components/feedparser/sensor.py` here:
`<config directory>/custom_components/feedparser/sensor.py`

**Example configuration.yaml:**

```yaml
sensor:
  platform: feedparser
  name: Engineering Feed
  feed_url: 'https://www.sciencedaily.com/rss/matter_energy/engineering.xml'
```

**Configuration variables:**

key | description
:--- | :---
**platform (Required)** | The platform name
**name (Required)** | Name your feed
**feed_url (Required)** | The RSS feed URL
***

Due to how `custom_components` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.
