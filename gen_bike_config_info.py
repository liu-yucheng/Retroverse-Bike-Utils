"""
Generate bike configuration information.
Generates configuration information for the specified bike name.
"""

# Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt


from argparse import ArgumentParser as _ArgumentParser
import os as _os
import re as _re
import hashlib as _hashlib_
import json as _json_
import varname as _varname
import _datetime_utils


_os_path = _os.path
_varname_core = _varname.core
_nameof = _varname_core.nameof
_script_basename = _os_path.basename(__file__)
_parser = None
_arguments = None

data_folder_name = None
timestamp = None
config_file_name = None
arguments_overridden = False
bike_name = None
config_info = None
config_dict = None


def _create_context():
    global data_folder_name
    global timestamp
    global config_file_name

    script_no_ext, _ = _os_path.splitext(_script_basename)

    if data_folder_name is None:
        data_folder_name = _os_path.dirname(__file__)
        data_folder_name = _os_path.join(data_folder_name, f".{script_no_ext}_data")

    _os.makedirs(data_folder_name, exist_ok=True)

    if timestamp is None:
        timestamp = _datetime_utils.find_now_custom_date_time_string()

    if config_file_name is None:
        config_file_name = f"bike-config_{timestamp}.json"
        config_file_name = _os_path.join(data_folder_name, config_file_name)
    # end if


def _parse_arguments():
    global _parser
    global _arguments
    global bike_name

    _parser = _ArgumentParser(
        prog=_script_basename,
        usage=f"python {_script_basename} [--help] <bike-name>",
        description="Generates configuration information for the specified bike name.",
        epilog="Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License."
    )

    _parser.add_argument(
        "bike_name",
        type=str,
        help="The bike name.",
        metavar="string"
    )

    if not arguments_overridden:
        _arguments = _parser.parse_args()

        if bike_name is None:
            bike_name = _arguments.bike_name

        bike_name = str(bike_name)


def _generate_config_info():
    def _find_hash_hex_str(info: str, digit_count: int) -> str:
        config_info_encoded = info.encode(encoding="utf-8")
        hash_ = _hashlib_.sha512(config_info_encoded, usedforsecurity=True)
        result = hash_.hexdigest()
        result = result[-digit_count:]
        return result

    global config_info
    global config_dict

    config_info = f"begin config-info\n"\
        + f"{_nameof(timestamp)}: {timestamp}\n"\
        + f"{_nameof(bike_name)}: {bike_name}\n"

    config_dict = {
        _nameof(timestamp): timestamp,
        _nameof(bike_name): bike_name
    }

    secret = _find_hash_hex_str(config_info, 8)
    config_info += f"{_nameof(secret)}: {secret}\n"
    config_dict[_nameof(secret)] = secret

    ssid = _find_hash_hex_str(config_info, 4)
    bike_name_prefix = _re.split("_+", bike_name)[0]
    ssid = f"{bike_name_prefix}_{ssid}"
    config_info += f"{_nameof(ssid)}: {ssid}\n"
    config_dict[_nameof(ssid)] = ssid

    password = _find_hash_hex_str(config_info, 4)
    password = f"0000{password}"

    config_info += f"{_nameof(password)}: {password}\n"\
        + f"end config-info"

    config_dict[_nameof(password)] = password


def _generate_config_file():
    with open(config_file_name, "w+", encoding="utf-8") as config_file:
        _json_.dump(config_dict, config_file, indent=4)
    # end with


def main():
    """
    Starts the main procedure.
    """
    print(f"begin {_script_basename}")
    _create_context()
    _parse_arguments()
    _generate_config_info()
    _generate_config_file()

    print(
        f"{bike_name = :s}\n"
        + f"{config_info = :s}\n"
        + f"{config_file_name = :s}"
    )

    print(f"end {_script_basename}")


if __name__ == "__main__":
    main()
