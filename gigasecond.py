# Given a moment, determine the moment that would be after a gigasecond has passed.
# A gigasecond is 10^9 (1,000,000,000) seconds.

import time
import datetime
from datetime import date, timedelta

def add(moment):
    
    new_datetime = moment + datetime.timedelta(0, 1000000000)
    return new_datetime
