"""
Generates configurations for a bike name.
"""

# Copyright (C) 2024-2025 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt .


from argparse import ArgumentParser as _ArgumentParser
import os as _os
import re as _re
import hashlib as _hashlib_
import json as _json_
import varname as _varname
import _utils__date_time


_os_path = _os.path
_nameof = _varname.core.nameof
_basename__this_file = _os_path.basename(__file__)
_parser = None
_args = None

name_no_ext__this_file: str
"""The name of this file without extension."""
name_no_ext__this_file, _ = _os_path.splitext(_basename__this_file)
folder_name__data: str = None
"""The folder name of script data."""
timestamp: str = None
"""A timestamp for the operation."""
file_name__configs: str = None
"""The file name of the bike configs."""
args__overridden: bool = False
"""Whether the arguments are overridden."""
bike_name: str = None
"""The bike name."""
str__configs: str = None
"""The bike configs in string format."""
dict__configs: dict = None
"""The bike configs in dict format."""


def _context__create():
    global folder_name__data
    global timestamp
    global file_name__configs

    if folder_name__data is None:
        folder_name__data = _os_path.dirname(__file__)
        folder_name__data = _os_path.join(folder_name__data, f".{name_no_ext__this_file}__data")
    # end if

    _os.makedirs(folder_name__data, exist_ok=True)

    if timestamp is None:
        timestamp = _utils__date_time.date_time_custom_str__find_for_now()
    # end if

    if file_name__configs is None:
        file_name__configs = f"bike_configs__{timestamp}.json"
        file_name__configs = _os_path.join(folder_name__data, file_name__configs)
    # end if
# end def


def _args__parse():
    global _parser
    global _args
    global bike_name

    _parser = _ArgumentParser(
        prog=_basename__this_file,
        usage=f"python {_basename__this_file} [--help] <{_nameof(bike_name)}>",
        description="Generates configurations for a bike name.",
        epilog="Copyright (C) 2024-2025 Yucheng Liu. Under the GNU AGPL 3.0 License."
    )

    _parser.add_argument(
        f"{_nameof(bike_name)}",
        type=str,
        help="Bike name.",
        metavar=f"{_nameof(bike_name)}"
    )

    if not args__overridden:
        _args = _parser.parse_args()

        if bike_name is None:
            bike_name = getattr(_args, _nameof(bike_name))
        # end if

        bike_name = str(bike_name)
    # end if
# end def

def _hash_hex_str__find(str_: str, digit_count: int) -> str:
    """
    Finds a hash hex string of a given digit count.
    Args:
        str_ (str): An input string.
        digit_count (int): The digit count of the hash hex string.
    Returns:
        result (str): The hash hex string.
    """
    str__encoded = str_.encode(encoding="utf-8")
    hash_ = _hashlib_.sha512(str__encoded, usedforsecurity=True)
    result = hash_.hexdigest()
    result = result[-digit_count:]
    return result
# end def

def _configs__generate():
    global str__configs
    global dict__configs

    str__configs = \
        f"begin bike configs\n" \
        + f"{_nameof(timestamp)}: {timestamp}\n" \
        + f"{_nameof(bike_name)}: {bike_name}\n"
    # end statement

    dict__configs = {
        _nameof(timestamp): timestamp,
        _nameof(bike_name): bike_name
    }

    secret = _hash_hex_str__find(str__configs, 8)
    str__configs += f"{_nameof(secret)}: {secret}\n"
    dict__configs[_nameof(secret)] = secret
    wifi_ssid = _hash_hex_str__find(str__configs, 4)
    bike_name_prefix = _re.split("_+", bike_name)[0]
    wifi_ssid = f"{bike_name_prefix}_{wifi_ssid}"
    str__configs += f"{_nameof(wifi_ssid)}: {wifi_ssid}\n"
    dict__configs[_nameof(wifi_ssid)] = wifi_ssid
    wifi_password = _hash_hex_str__find(str__configs, 4)
    wifi_password = f"0000{wifi_password}"

    str__configs += \
        f"{_nameof(wifi_password)}: {wifi_password}\n" \
        + f"end bike configs"
    # end statement

    dict__configs[_nameof(wifi_ssid)] = wifi_password
# end def


def _configs_file__generate():
    with open(file_name__configs, "w+", encoding="utf-8") as config_file:
        _json_.dump(dict__configs, config_file, indent=4)
    # end with
# end def


def main():
    """
    Starts the main procedure.
    """
    print(f"begin {_basename__this_file}")
    _context__create()
    _args__parse()
    _configs__generate()
    _configs_file__generate()

    print(
        f"{bike_name = :s}\n"
        + f"{str__configs = :s}\n"
        + f"{file_name__configs = :s}"
    )

    print(f"end {_basename__this_file}")


if __name__ == "__main__":
    main()
