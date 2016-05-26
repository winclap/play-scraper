# -*- coding: utf-8 -*-

"""
play_scraper.api

:copyright: (c) 2016 Daniel Liu.
:license: MIT, see LICENSE for more details.

"""

from . import scraper


def details(app_id):
    """Sends a GET request to the app's info page, parses the app's details, and
    returns them as a dict.

    :param app_id: the app to retrieve details from, e.g. 'com.nintendo.zaaa'
    :return: a dictionary of app details
    """
    s = scraper.PlayScraper()
    return s.details(app_id)
