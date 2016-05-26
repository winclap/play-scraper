# -*- coding: utf-8 -*-

import unittest
import logging

import play_scraper.settings as s
from play_scraper.lists import CATEGORIES, COLLECTIONS, AGE_RANGE
from play_scraper.utils import build_url, send_request


logging.disable(logging.CRITICAL)


class BasicSetup(unittest.TestCase):
    def setUp(self):
        self.category = CATEGORIES['GAME_ACTION']
        self.collection = COLLECTIONS['TOP_FREE']


class TestBuildUrl(unittest.TestCase):
    def test_building_app_url(self):
        expected = 'https://play.google.com/store/apps/details?id=com.facebook.orca'
        self.assertEqual(build_url('details', 'com.facebook.orca'), expected)

    def test_building_simple_dev_name(self):
        expected = 'https://play.google.com/store/apps/developer?id=Disney'
        self.assertEqual(build_url('developer', 'Disney'), expected)

    def test_building_multiple_word_dev_name(self):
        expected = 'https://play.google.com/store/apps/developer?id=SQUARE+ENIX+INC'
        self.assertEqual(build_url('developer', 'SQUARE ENIX INC'), expected)


class TestSendRequest(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.google.com/'
        self.age = AGE_RANGE['FIVE_UNDER']

    def test_send_normal_request(self):
        method = 'GET'
        response = send_request(method, self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.url, self.url)

    def test_request_with_params(self):
        method = 'GET'
        params = {'q': 'google play store'}
        response = send_request(method, self.url, params=params)
        expected_url = "{base}{params}".format(
            base=self.url, params='?q=google+play+store')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.url, expected_url)


if __name__ == '__main__':
    unittest.main()
