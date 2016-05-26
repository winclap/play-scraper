# -*- coding: utf-8 -*-

import unittest

from play_scraper.scraper import PlayScraper


DETAILED_KEYS = 32


class ScraperTestBase(unittest.TestCase):
    def setUp(self):
        self.s = PlayScraper()


class TestScrapingDetails(ScraperTestBase):
    def test_fetching_app_with_all_details(self):
        app = self.s.details('com.android.chrome')

        self.assertEqual(len(app.keys()), DETAILED_KEYS)
        self.assertEqual(app['app_id'], 'com.android.chrome')
        self.assertEqual(app['category'], ['COMMUNICATION'])
        self.assertEqual(app['installs'], [1000000000, 5000000000])
        self.assertTrue(app['top_developer'])


if __name__ == '__main__':
    unittest.main()
