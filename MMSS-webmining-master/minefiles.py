#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:59:15 2017

@author: Carlos Rodriguez
"""
import csv
import os

authors = open("authorslist.csv")
auth = authors.read().split("\n")
auth = auth[:-1]

report = open("report.csv", "w", newline="")

path="/home/carlos/zikaproj/CSVfiles/TXTitems/"

findings = 0

for tf in os.listdir(path):
    textfile = path+tf
    txt=open(textfile, "r")
    URL = txt.readlines()[4].rstrip()
    for au in auth:
        txt.seek(0)
        for line in txt:
            line = line.lower()
            if au in line:
                findings += 1
                entry = [findings, au, URL]
                csv.writer(report).writerow(entry)
    txt.close()

authors.close()
report.close()
