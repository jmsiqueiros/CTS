#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:37:56 2017

@author: Carlos Rodriguez, PhD (IIMAS, UNAM)
"""
# Script for mining GDELT project

import argparse
from datetime import date, timedelta
from sh import wget, links2
import zipfile
import csv
import httplib2

parser = argparse.ArgumentParser(
    description='grab urls from gdeltproject.com by date')
parser.add_argument('--start', help='start date, YYYY-MM-DD', required=True)
parser.add_argument('--end', help='end date, YYYY-MM-DD', required=True)
parser.add_argument('--words', help='words to filter by', nargs="+")
args = parser.parse_args()


syear, smonth, sday = args.start.split('-')
eyear, emonth, eday = args.end.split('-')

d1 = date(int(syear), int(smonth), int(sday))  # start date
d2 = date(int(eyear), int(emonth), int(eday))  # end date

delta = d2 - d1   # timedelta

# %%
# If local repository exists, it will be deleted to retrieve fresh info
import shutil
from pathlib import Path
if Path("CSVfiles").is_dir():
    shutil.rmtree("CSVfiles")
# %%
# Create the new directories to retrieve the info
from os import mkdir
from os import remove
mkdir("CSVfiles")
mkdir("CSVfiles/TXTitems")
# %%
# Create a file to save statistics
stats = open("URLstats.txt", "w+")
# %%
for i in range(delta.days + 1):

    date = str(d1 + timedelta(days=i)).replace('-','')
    h = httplib2.Http("http://data.gdeltproject.org/events/%s.export.CSV.zip" % date)
    resp, content = h.request("http://data.gdeltproject.org/events/%s.export.CSV.zip" % date)
    # If file exists, it will be retieved to be unpzipped,
    # once unzipped it will be deleted.
    if resp.status == 200:

        wget("-P", "CSVfiles", "http://data.gdeltproject.org/events/%s.export.CSV.zip" % date)
        zf = zipfile.ZipFile("CSVfiles/%s.export.CSV.zip" % date, "r")
        zf.extractall('CSVfiles')
        remove("CSVfiles/%s.export.CSV.zip" % date)

        # grab the URLs
        urls = []
        with open("CSVfiles/%s.export.CSV" % date, 'r') as data:
            reader = csv.reader(data, delimiter='\t')
            for row in reader:
                url = row[57]
                if args.words:
                    present = False
                    for w in args.words:
                        if w in url.lower():
                            present = True
                        if present:
                            urls.append(url)
                else:
                    urls.append(url)

        # download html dumps of them
        n = 0
        for url in urls:
            try:
                with open('CSVfiles/TXTitems/%s_%s_item.txt' % (date, n), 'w') as f:
                    f.write('\n\n\n\n' + url + '--------------------------\n\n\n\n')
                    f.write(str(links2('-dump', url)))
            except:
                pass
            n += 1

        # If he word is found, the URL is recorded
        stats.write("Date: %s  URLs: %d\r\n" % (date, n))

stats.close()

