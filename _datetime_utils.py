"""
(Private) date time utilities.
"""

# Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt


import datetime as _datetime


_datetime_ = _datetime.datetime
_timedelta = _datetime.timedelta


def custom_mod(numerator, denominator, signed):
    result = numerator % denominator

    if signed and result > 0 and numerator < 0:
        result -= denominator

    return result


class TimeDeltaCustom:
    """
    A custom timedelta structure.
    """
    us_per_ms = 1000
    ms_per_second = 1000
    seconds_per_minute = 60
    minutes_per_hour = 60
    hours_per_day = 24
    days_per_week = 7
    weeks_per_year = 52


    def __init__(self, time_delta: _timedelta) -> None:
        """
        Initializes an object.

        Args:
            time_delta (_timedelta): a time delta
        """
        self._time_delta = time_delta

        self._us = time_delta.microseconds
        self._seconds = time_delta.seconds
        self._days = time_delta.days

        if time_delta.days < 0:
            self._seconds -=\
                1\
                * self.hours_per_day\
                * self.minutes_per_hour\
                * self.seconds_per_minute

            self._days += 1


        self._ms = int(self._us / self.us_per_ms)
        self._minutes = int(self._seconds / self.seconds_per_minute)
        self._hours = int(self._minutes / self.minutes_per_hour)
        self._weeks = int(self._days / self.days_per_week)
        self._years = int(self._weeks / self.weeks_per_year)

        self.positive =\
            self._days >= 0\
            and self._seconds >= 0

        self.us = self._us
        self.second = custom_mod(self._seconds, self.seconds_per_minute, True)
        self.minute = custom_mod(self._minutes, self.minutes_per_hour, True)
        self.hour = custom_mod(self._hours, self.hours_per_day, True)
        self.day = custom_mod(self._days, self.days_per_week, True)
        self.week = custom_mod(self._weeks, self.weeks_per_year, True)
        self.year = self._years
    # end def


def find_custom_date_time_string(date_time: _datetime_, utc_offset: _timedelta) -> str:
    """
    Finds a custom date time string for the given date time information.

    Args:
        date_time (_datetime_): a date time
        utc_offset (_timedelta): an UTC offset

    Returns:
        str: A custom date time string
    """
    utc_offset_custom = TimeDeltaCustom(utc_offset)

    result =\
        f"{date_time.year:04d}{date_time.month:02d}{date_time.day:02d}"\
        + f"-{date_time.hour:02d}{date_time.minute:02d}{date_time.second:02d}"\
        + f"-{date_time.microsecond:06d}"\

    if utc_offset_custom.positive:
        result += f"-utc{abs(utc_offset_custom.hour):02d}{abs(utc_offset_custom.minute):02d}"
    else:
        result += f"-utc-{abs(utc_offset_custom.hour):02d}{abs(utc_offset_custom.minute):02d}"

    return result


def find_now_custom_date_time_string() -> str:
    """
    Finds a custom date time string for now.

    Returns:
        result: A custom date time string.
    """
    now = _datetime_.now()
    utc_now = _datetime_.now(_datetime.timezone.utc)
    utc_offset = utc_now.astimezone().tzinfo.utcoffset(utc_now)
    result = find_custom_date_time_string(now, utc_offset)
    return result
