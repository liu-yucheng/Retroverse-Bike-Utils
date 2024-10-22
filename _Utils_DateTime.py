"""
(Private) date time utilities.
"""

# Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt


import datetime as _datetime


_datetime_ = _datetime.datetime
_timedelta = _datetime.timedelta


def Mod_Custom(Numerator, Denominator, Signed):
    """
    Performs a custom mod operation.

    Args:
        Numerator: A numerator.
        Denominator: A denominator.
        Signed: Whether the operation is signed.

    Returns:
        Result: The result.
    """
    Result = Numerator % Denominator

    if Signed and Result > 0 and Numerator < 0:
        Result -= Denominator

    return Result


class TimeDelta_Custom:
    """
    A custom timedelta structure.
    """
    Unit_USPerMS = 1000
    Unit_MSPerSecond = 1000
    Unit_SecondsPerMinute = 60
    Unit_MinutesPerHour = 60
    Unit_HoursPerDay = 24
    Unit_DaysPerWeek = 7
    Unit_WeeksPerYear = 52


    def __init__(self, TimeDelta: _timedelta) -> None:
        """
        Initializes an object.

        Args:
            TimeDelta (_timedelta): a time delta
        """
        self._TimeDelta = TimeDelta

        self._US_InSecond = TimeDelta.microseconds
        self._Second_InDay = TimeDelta.seconds
        self._Day_Total = TimeDelta.days

        if TimeDelta.days < 0:
            self._Second_InDay -= \
                1 \
                * self.Unit_HoursPerDay \
                * self.Unit_MinutesPerHour \
                * self.Unit_SecondsPerMinute

            self._Day_Total += 1


        self._MS_InSecond = int(self._US_InSecond / self.Unit_USPerMS)

        self._Minute_InDay = \
            int(self._Second_InDay / self.Unit_SecondsPerMinute)

        self._Hour_InDay = int(self._Minute_InDay / self.Unit_MinutesPerHour)
        self._Week_Total = int(self._Day_Total / self.Unit_DaysPerWeek)
        self._Year_Total = int(self._Week_Total / self.Unit_WeeksPerYear)

        self.Positive = \
            self._Day_Total >= 0 \
            and self._Second_InDay >= 0

        self.US_InSecond = self._US_InSecond
        self.MS_InSecond = self._MS_InSecond

        self.Second_InMinute = \
            Mod_Custom(self._Second_InDay, self.Unit_SecondsPerMinute, True)

        self.Minute_InHour = \
            Mod_Custom(self._Minute_InDay, self.Unit_MinutesPerHour, True)

        self.Hour_InDay = \
            Mod_Custom(self._Hour_InDay, self.Unit_HoursPerDay, True)

        self.Day_InWeek = \
            Mod_Custom(self._Day_Total, self.Unit_DaysPerWeek, True)

        self.Week_InYear = \
            Mod_Custom(self._Week_Total, self.Unit_WeeksPerYear, True)

        self.Year_Total = self._Year_Total
    # end def


def DateTime_Custom_FindStringFor(
        DateTime: _datetime_,
        UTCOffset: _timedelta
) -> str:
    """
    Finds a custom date time string for the given date time information.

    Args:
        DateTime (_datetime_): a date time
        UTCOffset (_timedelta): an UTC offset

    Returns:
        Result (str): A custom date time string
    """
    UTCOffset_Custom = TimeDelta_Custom(UTCOffset)

    Result =\
        f"{DateTime.year:04d}{DateTime.month:02d}{DateTime.day:02d}"\
        + f"-{DateTime.hour:02d}{DateTime.minute:02d}{DateTime.second:02d}"\
        + f"-{DateTime.microsecond:06d}"\

    if UTCOffset_Custom.Positive:
        Result += \
            f"-utc{abs(UTCOffset_Custom.Hour_InDay):02d}"\
            + f"{abs(UTCOffset_Custom.Minute_InHour):02d}"
    else:
        Result += \
            f"-utc-{abs(UTCOffset_Custom.Hour_InDay):02d}"\
            + f"{abs(UTCOffset_Custom.Minute_InHour):02d}"

    return Result


def DateTime_Custom_FindStringFor_Now() -> str:
    """
    Finds a custom date time string for now.

    Returns:
        Result: A custom date time string.
    """
    Now = _datetime_.now()
    Now_UTC = _datetime_.now(_datetime.timezone.utc)
    Now_UTCOffset = Now_UTC.astimezone().tzinfo.utcoffset(Now_UTC)
    Result = DateTime_Custom_FindStringFor(Now, Now_UTCOffset)
    return Result
