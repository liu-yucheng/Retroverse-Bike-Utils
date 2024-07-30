"""
Batch generate bike configuration information.
Performs a batch of "gen_bike_config_info.py" operations.
"""

# Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt


from argparse import ArgumentParser as _ArgumentParser
import os as _os
import varname as _varname
import gen_bike_config_info as _gen_bike_config_info
import _datetime_utils


_os_path = _os.path
_varname_core = _varname.core
_script_basename = _os_path.basename(__file__)
_parser = None
_arguments = None

data_folder_name = None
timestamp = None
arguments_overridden = False
bike_names = None
config_info_list = None


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
    global bike_names

    _parser = _ArgumentParser(
        prog=_script_basename,
        usage=f"python {_script_basename} [--help] <bike-name-1> [bike-name-2] ...[bike-names]",
        description="Performs a batch of \"gen_bike_config_info.py\" operations.",
        epilog="Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License."
    )

    _parser.add_argument(
        "bike_names",
        nargs="+",
        type=str,
        help="The bike names.",
        metavar="list of strings"
    )

    if not arguments_overridden:
        _arguments = _parser.parse_args()

        if bike_names is None:
            bike_names = _arguments.bike_names

        for index, bike_name in enumerate(bike_names):
            bike_names[index] = str(bike_name)
        # end for
    # end if


def _perform_batch_operations():
    global config_info_list

    print("begin Batch operations")
    config_info_list = []

    for index, bike_name in enumerate(bike_names):
        print(f"begin Operation {index + 1} / {len(bike_names)}")
        _gen_bike_config_info.data_folder_name = data_folder_name
        _gen_bike_config_info.timestamp = timestamp
        _gen_bike_config_info.arguments_overridden = True
        _gen_bike_config_info.bike_name = bike_name
        _gen_bike_config_info.main()
        config_info_list.append(_gen_bike_config_info.config_info)
        print(f"end Operation {index + 1} / {len(bike_names)}")

    print("end Batch operations")


def main():
    """
    Starts the main procedure.
    """
    def _print_list(name: str, list_: list):
        info = f"\nbegin list {name}\n"

        for index, element in enumerate(list_):
            info += f"begin element {index + 1} / {len(list_)}\n"\
                + f"{element:s}\n"\
                + f"end element {index + 1} / {len(list_)}\n"
            # end info

        info += f"end list {name}\n"
        print(info)

    print(f"begin {_script_basename}")
    _create_context()
    _parse_arguments()
    _perform_batch_operations()
    print(f"{bike_names}")
    _print_list(_varname_core.nameof(bike_names), bike_names)
    _print_list(_varname_core.nameof(config_info_list), config_info_list)
    print(f"end {_script_basename}")


if __name__ == "__main__":
    main()
