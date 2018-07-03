#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:06:07 2017

@author: carlos
"""
# %%
# Routine to find unique autors

import csv
authors = open("report.csv", "r")
uniqauth = open("uniqueauthors.csv", "w+", newline="")
auonly = []
for row in csv.reader(authors):
     au = list(row)[1]
     auonly.append(au)

authors.close()
auset = list(set(auonly))
for i in auset:
    csv.writer(uniqauth).writerow([i])
csv.writer(uniqauth).writerow([str(len(auset))])

uniqauth.close()

# %%
# Routine to find incidence of authors in various URL

import csv
authors = open("report.csv", "r")
URLlis = open("siteslistingauthors.csv", "w+", newline="")
auURL = []

for row in csv.reader(authors):
    au = row[1]
    url = row[2]
    item = au+", "+url
    auURL.append(item)

authors.close()
auURLset = list(set(auURL))
for i in auURLset:
    csv.writer(URLlis).writerow([i])
#    print(i)
csv.writer(URLlis).writerow([str(len(auURLset))])

URLlis.close()

# %%

# Routine to count authors and its URLs citing them
from collections import Counter
import csv
authors = open("report.csv", "r")
auURL = []
included_cols = [1, 2]
for row in csv.reader(authors):
    content = list(row[i] for i in included_cols)
    print(content)

authors.close()
auURLset = list(set(auURL))
for i in auURLset:
    print(i)
print(len(auURLset))

