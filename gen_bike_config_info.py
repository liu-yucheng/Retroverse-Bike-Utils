"""
Generate bike configuration information.
Generates configuration information for the specified bike name.
"""

# Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt


from argparse import ArgumentParser as _ArgumentParser
import os as _os
import hashlib as _hashlib_
import _datetime_utils


_os_path = _os.path
_script_basename = _os_path.basename(__file__)
_parser = None
_arguments = None

data_folder_name = None
timestamp = None
arguments_overridden = False
bike_name = None
config_info = None


def _create_context():
    global data_folder_name
    global timestamp

    script_no_ext, _ = _os_path.splitext(_script_basename)

    if data_folder_name is None:
        data_folder_name = _os_path.dirname(__file__)
        data_folder_name = _os_path.join(data_folder_name, f".{script_no_ext}_data")

    _os.makedirs(data_folder_name, exist_ok=True)

    if timestamp is None:
        timestamp = _datetime_utils.find_now_custom_date_time_string()
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
    def _find_hash_hex_str(config_info: str, digit_count: int) -> str:
        config_info_encoded = config_info.encode(encoding="utf-8")
        hash_ = _hashlib_.sha512(config_info_encoded, usedforsecurity=True)
        result = hash_.hexdigest()
        result = result[-digit_count:]
        return result

    global config_info

    config_info = f"\n"\
        + "====-====-====-====\n"\
        + f"timestamp: {timestamp}\n"\
        + f"bike-name: {bike_name}\n"

    hash_hex_str = _find_hash_hex_str(config_info, 8)
    config_info += f"secret: {hash_hex_str}\n"
    hash_hex_str = _find_hash_hex_str(config_info, 4)
    bike_name_prefix = bike_name.split("--")[0]
    config_info += f"ssid: {bike_name_prefix}--{hash_hex_str}\n"
    hash_hex_str = _find_hash_hex_str(config_info, 4)

    config_info += f"password: 0000{hash_hex_str}\n"\
        + f"====-====-====-====\n"
    # end config_info


def main():
    """
    Starts the main procedure.
    """
    print(f"begin {_script_basename}")
    _create_context()
    _parse_arguments()
    _generate_config_info()

    print(
        f"{bike_name = :s}\n"
        + f"{config_info = :s}"
    )

    print(f"end {_script_basename}")


if __name__ == "__main__":
    main()
