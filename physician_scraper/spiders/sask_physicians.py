"""
Scraper for the College of Physicians and Surgeons of Saskatchewan
The objective is to compile the full list of physicians in the province
with all the available data.
"""

import json
from typing import Set

import scrapy

API_URL = "https://www.cps.sk.ca/CPSSWebApi/api/Physicians/?callback=angular.callbacks._2&name="

seen_ids: Set[int] = set()


class SaskPhysiciansSpider(scrapy.Spider):
    """
    Scraper for the College of Physicians and Surgeons of Saskatchewan.
    Since the site loads its data dynamically, we're hitting the api instead of the site.
    """

    name = "sask_physicians"
    allowed_domains = ["www.cps.sk.ca"]

    # we search for every name with at least one of the letters in the alphabet
    # if there are people with no english letters in their name we'll miss them

    start_urls = [API_URL + c for c in "abcdefghijklmnopqrstuvwxyz"]

    def parse(self, response):
        raw = response.body.decode("utf-8")
        #                       idk if the _2 is constant
        physician_list = raw.lstrip("angular.callbacks._2(").rstrip(");")
        physician_list = json.loads(physician_list)

        for physician in physician_list:
            if physician["ID"] in seen_ids:
                continue
            seen_ids.add(physician["ID"])

            yield physician
