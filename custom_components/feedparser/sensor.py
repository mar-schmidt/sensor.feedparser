"""
A component which allows you to parse an RSS feed into a sensor

For more details about this component, please refer to the documentation at
https://github.com/custom-components/sensor.feedparser

Following spec from https://validator.w3.org/feed/docs/rss2.html
"""

import logging
import voluptuous as vol
from datetime import timedelta
from dateutil import parser
from time import strftime
from subprocess import check_output
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import (PLATFORM_SCHEMA)

__version__ = '0.0.4'
_LOGGER = logging.getLogger(__name__)

REQUIREMENTS = ['feedparser']

CONF_NAME = 'name'
CONF_FEED_URL = 'feed_url'

DEFAULT_SCAN_INTERVAL = timedelta(hours=1)

COMPONENT_REPO = 'https://github.com/custom-components/sensor.feedparser/'
SCAN_INTERVAL = timedelta(hours=1)
ICON = 'mdi:rss'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_FEED_URL): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([FeedParserSensor(hass, config)])

class FeedParserSensor(Entity):
    def __init__(self, hass, config):
        self.hass = hass
        self._feed = config[CONF_FEED_URL]
        self._name = config[CONF_NAME]
        self._state = None
        self.hass.data[self._name] = {}
        self.update()

    def update(self):
        import feedparser
        parsedFeed = feedparser.parse(self._feed)

        if not parsedFeed :
            return False
        else:
            self._state = len(parsedFeed.entries)
            self.hass.data[self._name] = parsedFeed

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def device_state_attributes(self):
        attrs = {}
        attrs['rss'] = self.hass.data[self._name]
        return attrs
