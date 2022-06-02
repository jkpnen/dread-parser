#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys

import pandas as pd
import xlsxwriter

from pathlib import Path
from typing import List

from bs4 import BeautifulSoup


class City:
    def __init__(self, name: str):
        self.name = name
        self.html_files = []
        self.soups = []
        self.user_names = []
        self.messages = []
        self.dates = []


def list_files(given_directory: str) -> List[City]:
    """
    Recursively iterate through the given directory and all its subdirectories using pathlib.

    :param given_directory: The directory that is iterated
    :return: The list of HTML-files from the given directory
    """
    cities_list = []
    p = Path(given_directory)
    for folder in p.rglob('*'):
        for file in folder.rglob('*'):
            if file.suffix == '.html':
                city = re.search(r"\[([^]]+)", file.stem)
                found_city = city.group(1)
                if not cities_list:
                    new_city = City(name=found_city)
                    new_city.html_files.append(file)
                    cities_list.append(new_city)
                else:
                    not_match = True
                    for city in cities_list:
                        if city.name == found_city:
                            city.html_files.append(file)
                            not_match = False
                    if not_match:
                        new_city = City(name=found_city)
                        new_city.html_files.append(file)
                        cities_list.append(new_city)
    return cities_list


def do_the_soap(cities):
    for city in cities:
        for html_file in city.html_files:
            with open(html_file) as file_path:
                soup = BeautifulSoup(file_path, 'html.parser')
                city.soups.append(soup)


def iterate_soups(cities) -> List[object]:
    """
    Iterate soups and return the object list of Users (username, comment, date).

    :return: The object list of Users (username, comment, date)
    """
    for city in cities:
        for soup in city.soups:
            for comment in soup.find_all('div', 'commentBody'):
                stripped_comment = re.sub('[^A-Za-z0-9äöüÄÖÜß]+', ' ', comment.text)
                city.messages.append(stripped_comment)
                for c in comment.parent.find_all('a', 'username'):
                    if '/u/' in c.text:
                        username_without_tag = c.text.replace('/u/', '')
                        city.user_names.append(username_without_tag.strip())
                    else:
                        city.user_names.append(c.text)
                    for time_stamp in c.parent.find_all('div', 'timestamp'):
                        date = time_stamp.next.attrs['title']
                        city.dates.append(date)
    return cities


def create_xlsx(cities):
    workbook = xlsxwriter.Workbook('DREAD-MESSAGES.xlsx')

    workbooks = {}
    for city in cities:
        workbooks[city.name] = workbook.add_worksheet(city.name)

    city_names = {}
    for city in cities:
        city_names[city.name] = city.name

    for city in cities:
        city.dates = pd.to_datetime(city.dates)

    for city in cities:
        city_names[city.name] = workbooks[city.name]
        row = 1
        column = 0
        for i in range(len(city.messages)):
            city_names[city.name].write(row, column, city.user_names[i])
            city_names[city.name].write(row, column + 1, city.messages[i])
            city_names[city.name].write(row, column + 2, str(city.dates[i]))
            row += 1
    workbook.close()


def remove_duplicates(cities):
    for city in cities:
        indexes = []
        seen = set()
        for index, m in enumerate(city.messages):
            if m not in seen:
                indexes.append(index)
            seen.add(m)
        city.dates = [city.dates[index] for index in indexes]
        city.user_names = [city.user_names[index] for index in indexes]
        city.messages = list(seen)
    return cities


if __name__ == '__main__':
    loc = sys.argv[1]
    cities_list = list_files(loc)
    do_the_soap(cities_list)
    cities_soup = iterate_soups(cities_list)
    cities_list = remove_duplicates(cities_list)
    create_xlsx(cities_list)
