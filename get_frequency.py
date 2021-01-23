# -*- coding: utf-8 -*-
"""
Created on Thus June 09 12:46:00 2019
Author: saurabh
"""

import pandas as pd
def compute_frequency(date_column_series):
    """
        Computes frequency of date column
        ------
        Parameters:
            date_column_series : pandas series
                series with date specified column
        Returns:
        ------
            frequency: str
                frequency of a dataset
        Exceptions
        ------
            No exception
    """

    try:
        date_column_series = pd.to_datetime(date_column_series)
        freq_series = date_column_series.sort_values().dt.date
        difference = freq_series - freq_series.shift(1)
        days = difference.mode().iloc[0].days

        print('days',days)
        
        if days > 92:
            frequency = 'YS(Year start)'
        elif 92 <= days > 31:
            frequency = 'QS(Quarter start)'
        elif 31 <= days > 1:
            frequency = 'MS(Month start)'
        elif 7 <= days > 1:
            frequency = 'W(Weekly)'
        elif days == 1:
            frequency = 'D(Calendar day)'
        else:
            frequency = 'Could not find frequency'
        return frequency
    except:
        return 'Invalid dates'

