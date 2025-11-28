"""
(Private) custom date time utilities.
"""

# Copyright (C) 2024-2025 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt .


import datetime as _datetime


_datetime_ = _datetime.datetime
_timedelta = _datetime.timedelta


def mod_custom(numer, denom, signed):
    """
    Performs a custom mod operation.

    Args:
        numer: A numerator.
        denom: A denominator.
        signed: Whether the operation is signed.

    Returns:
        result: The result.
    """
    result = numer % denom

    if signed and result > 0 and numer < 0:
        result -= denom
    # end if

    return result
# end def


class TimeDelta_Custom:
    """A custom timedelta structure."""
    US_PER_MS = 1000
    """Unit converstion multiplier - ms to us."""
    MS_PER_S = 1000
    """Unit converstion multiplier - s to ms."""
    S_PER_MIN = 60
    """Unit converstion multiplier - min to s."""
    MIN_PER_H = 60
    """Unit converstion multiplier - ms to h."""
    H_PER_DAY = 24
    """Unit converstion multiplier - h to day."""
    DAYS_PER_WEEK = 7
    """Unit converstion multiplier - day to week."""
    WEEKS_PER_YEAR = 52
    """Unit converstion multiplier - week to year."""

    def __init__(self, time_delta: _timedelta) -> None:
        """
        Initializes an object.

        Args:
            time_delta (_timedelta): a time delta
        """
        self.time_delta: _timedelta = time_delta
        """
        The standard library time delta.
        """
        self._us_in_s = time_delta.microseconds
        self._s_in_day = time_delta.seconds
        self._days_total = time_delta.days

        if time_delta.days < 0:
            self._s_in_day -= self.H_PER_DAY * self.MIN_PER_H * self.S_PER_MIN
            self._days_total += 1
        # end if

        self._ms_in_s = int(self._us_in_s / self.US_PER_MS)
        self._min_in_day = int(self._s_in_day / self.S_PER_MIN)
        self._h_in_day = int(self._min_in_day / self.MIN_PER_H)
        self._weeks_total = int(self._days_total / self.DAYS_PER_WEEK)
        self._years_total = int(self._weeks_total / self.WEEKS_PER_YEAR)
        self.is_positive: bool = self._days_total >= 0 and self._s_in_day >= 0
        """Whether the time delta is positive."""
        self.us_in_s: int = self._us_in_s
        """Microseconds in second."""
        self.ms_in_s: int = self._ms_in_s
        """Milliseconds in second."""
        self.s_in_min: int = mod_custom(self._s_in_day, self.S_PER_MIN, True)
        """Seconds in minute."""
        self.min_in_h: int = mod_custom(self._min_in_day, self.MIN_PER_H, True)
        """Minutes in hour."""
        self.h_in_day: int = mod_custom(self._h_in_day, self.H_PER_DAY, True)
        """Hours in day."""
        self.days_in_week: int = mod_custom(self._days_total, self.DAYS_PER_WEEK, True)
        """Days in week."""
        self.weeks_in_year: int = mod_custom(self._weeks_total, self.WEEKS_PER_YEAR, True)
        """Weeks in year."""
        self.years_total: int = self._years_total
        """Total years."""
    # end def
# end class


def date_time_str_custom__find_for(date_time: _datetime_, utc_offset: _timedelta) -> str:
    """
    Finds a custom date time string for the given date time information.

    Args:
        date_time (_datetime_): a date time
        utc_offset (_timedelta): an UTC offset

    Returns:
        result (str): A custom date time string
    """
    utc_offset__custom = TimeDelta_Custom(utc_offset)

    result = \
        f"{date_time.year:04d}{date_time.month:02d}{date_time.day:02d}" \
        + f"_{date_time.hour:02d}{date_time.minute:02d}{date_time.second:02d}" \
        + f"_{date_time.microsecond:06d}"
    # end statement

    if utc_offset__custom.is_positive:
        result += \
            f"_utc_{abs(utc_offset__custom.h_in_day):02d}" \
            + f"{abs(utc_offset__custom.min_in_h):02d}"
        # end statement
    else:
        result += \
            f"_utc_-{abs(utc_offset__custom.h_in_day):02d}" \
            + f"{abs(utc_offset__custom.min_in_h):02d}"
        # end statement
    # end if

    return result
# end def


def date_time_str_custom__find_for_now() -> str:
    """
    Finds a custom date time string for now.

    Returns:
        result: A custom date time string.
    """
    now = _datetime_.now()
    utc = _datetime_.now(_datetime.timezone.utc)
    utc_offset = utc.astimezone().tzinfo.utcoffset(utc)
    result = date_time_str_custom__find_for(now, utc_offset)
    return result
# end def
