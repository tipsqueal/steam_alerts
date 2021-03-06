# Copyright 2015 jydo inc. All rights reserved.
import requests
from steam_alerts import logger


status_types = {
    0: 'offline',
    1: 'online',
    2: 'busy',
    3: 'away',
    4: 'snooze',
    5: 'looking to trade',
    6: 'looking to play'
}


class SteamService:
    def __init__(self, steam_key):
        self.steam_key = steam_key

    def resolve_vanity_url(self, vanity_url):
        url = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"
        payload = {'key': self.steam_key, 'vanityurl': vanity_url}

        return requests.get(url, params=payload).json()['response']['steamid']

    def get_player_statuses(self, steam_ids):
        logger.info('Retrieving statuses...')
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
        params = {'key': self.steam_key, 'steamids': steam_ids}

        return requests.get(url, params=params).json()['response']['players']
