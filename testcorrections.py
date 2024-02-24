#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:57:49 2024

@author: jack1019
"""


def count_unique_proteins():
    """
    Did not work on this function after discussing with Professor Nussbaum,
    since I can only get back 1.5 points maximum on this problem.
    """
    pass


def count_proteins():
    """
    Did not work on this function after discussing with Professor Nussbaum,
    since I can only get back 1.5 points maximum on this problem.
    """
    pass


def merge_protein_counts():
    """
    Did not work on this function after discussing with Professor Nussbaum,
    since I can only get back 1.5 points maximum on this problem.
    """
    pass


def dates_to_iso8601(dates_list):
    """
    Takes in a list of dates formatted as in dates_list and returns a list of
    the same dates in ISO-8601 format.
    """
    iso_dates = []
    for date in dates_list:
        full_date = date.split()
        day = full_date[1][:-1]
        if len(day) == 1:
            day = "0" + day
        iso_dates.append(full_date[2] + "-" + isohelper(date) + "-" +
                          day)
    return iso_dates


def isohelper(date):
    """
    Takes a date formatted as shown in dates_list and converts the month from
    a word to numbers.
    """
    result = date.split()[0]
    if result == "January":
        result = "01"
    elif result == "February":
        result = "02"
    elif result == "March":
        result = "03"
    elif result == "April":
        result = "04"
    elif result == "May":
        result = "05"
    elif result == "June":
        result = "06"
    elif result == "July":
        result = "07"
    elif result == "August":
        result = "08"
    elif result == "September":
        result = "09"
    elif result == "October":
        result = "10"
    elif result == "November":
        result = "11"
    elif result == "December":
        result = "12"
    return result


def sort_dates(dates_list):
    """
    Accepts list of dates formatted as in dates_list and returns a list with
    the same dates sorted in chronological order.
    """
    iso_dates = []
    for date in dates_list:
        full_date = date.split()
        day = full_date[1][:-1]
        if len(day) == 1:
            day = "0" + day
        iso_dates.append(int(full_date[2] + isohelper(date) + day))
    sorted_dates_iso = sorted(iso_dates)
    sorted_dates = []
    for iso_date in sorted_dates_iso:
        iso_date = str(iso_date)
        iso_year = iso_date[:4]
        iso_month = iso_date[4:6]
        iso_day = iso_date[6:]
        if iso_day[0] == "0":
            sorted_dates.append(month_convert(iso_month) + " " + iso_day[1] +
                                ", " + iso_year)
        else:
            sorted_dates.append(month_convert(iso_month) + " " + iso_day +
                                ", " + iso_year)
    return sorted_dates


def month_convert(month):
    """
    Takes in a month formatted in MM form and converts it to a string. For
    example, 01 becomes January.
    """
    if month == "01":
        month = "January"
    if month == "02":
        month = "February"
    if month == "03":
        month = "March"
    if month == "04":
        month = "April"
    if month == "05":
        month = "May"
    if month == "06":
        month = "June"
    if month == "07":
        month = "July"
    if month == "08":
        month = "August"
    if month == "09":
        month = "September"
    if month == "10":
        month = "October"
    if month == "11":
        month = "November"
    if month == "12":
        month = "December"
    return month
