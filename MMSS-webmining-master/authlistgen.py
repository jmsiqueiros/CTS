#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:52:28 2017

@author: Carlos Rodriguez

Generates a list of authors on Zika virus subject
"""
import csv

auth = open("authors.csv", "r")
authlist = open("authorslist.csv", "w", newline="")

for row in csv.reader(auth):
    if any(field.strip() for field in row):
        string = "".join(map(str, row))
        ind = string.split(";")
        ind = (item.lower().strip() for item in ind)

        rev = [" ".join(reversed(n.split(", "))) for n in ind]

        for i in rev:
            if i.strip():
                if i == "[anonymous]" or i == "": continue
                else: csv.writer(authlist).writerow([i])


auth.close()
authlist.close()
