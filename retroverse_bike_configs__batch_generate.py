"""
Performs a "_bike_configs__batch_generate.py" operation with a "Retroverse-Bike_" prefix for each bike name.
"""

# Copyright (C) 2024-2025 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt .


from argparse import ArgumentParser as _ArgumentParser
import os as _os
import varname as _varname
import bike_configs__batch_generate as _bike_configs__batch_generate
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
"""The timestamp for batch operations."""
file_name__batch_configs: str = None
"""The file name of the batch bike configs."""
args_overridden: bool = False
"""Whether the arguments are overridden."""
bike_names: list[str] = None
"""A list of bike names."""
retroverse_bike_names: list[str] = None
"""A list of retroverse bike names."""


def _context__create():
    global folder_name__data
    global timestamp
    global file_name__batch_configs

    if folder_name__data is None:
        folder_name__data = _os_path.dirname(__file__)
        folder_name__data = _os_path.join(folder_name__data, f".{name_no_ext__this_file}__data")
    # end if

    _os.makedirs(folder_name__data, exist_ok=True)

    if timestamp is None:
        timestamp = _utils__date_time.date_time_custom_str__find_for_now()
    # end if

    if file_name__batch_configs is None:
        file_name__batch_configs = f"batch__retroverse_bike_configs__{timestamp}.json"
        file_name__batch_configs = _os_path.join(folder_name__data, file_name__batch_configs)
    # end if
# end def


def _args__parse():
    global _parser
    global _args
    global bike_names

    _parser = _ArgumentParser(
        prog=_basename__this_file,

        usage=\
            f"python {_basename__this_file} [--help] <bike_name_1>" \
            + f" [bike_name_2] ...[{_nameof(bike_names)}]"
        ,

        description=\
            "Performs a \"_bike_configs__batch_generate.py\" operation" \
            + " with a \"Retroverse-Bike_\" prefix for each bike name."
        ,

        epilog="Copyright (C) 2024-2025 Yucheng Liu. Under the GNU AGPL 3.0 License.",
    )

    _parser.add_argument(
        f"{_nameof(bike_names)}",
        nargs="+",
        type=str,
        help="Bike names.",
        metavar=f"{_nameof(bike_names)}"
    )

    if not args_overridden:
        _args = _parser.parse_args()

        if bike_names is None:
            bike_names = getattr(_args, _nameof(bike_names))
        # end if

        for index, bike_name in enumerate(bike_names):
            bike_names[index] = str(bike_name)
        # end for
    # end if
# end def


def _op__perform():
    global retroverse_bike_names

    retroverse_bike_names = []

    for bike_name in bike_names:
        retroverse_bike_names.append(f"Retroverse-Bike_{bike_name}")
    # end for

    print(f"begin {_nameof(_op__perform)}")
    _bike_configs__batch_generate.folder_name__data = folder_name__data
    _bike_configs__batch_generate.timestamp = timestamp
    _bike_configs__batch_generate.file_name__batch_configs = file_name__batch_configs
    _bike_configs__batch_generate.args_overridden = True
    _bike_configs__batch_generate.bike_names = retroverse_bike_names
    _bike_configs__batch_generate.main()
    print(f"end {_nameof(_op__perform)}")
# end def


def _list__print(name: str, list_: list):
    """
    Prints a list with a given name.
    Args:
        name (str): The name of the list.
        list_ (list): The list to print.
    """
    info = f"begin list {name}\n"

    for index, element in enumerate(list_):
        info += \
            f"begin element {index + 1} / {len(list_)}\n" \
            + f"{element:s}\n" \
            + f"end element {index + 1} / {len(list_)}\n"
        # end statement
    # end for

    info += f"end list {name}"
    print(info)
# end def


def main():
    """
    Starts the main procedure.
    """
    print(f"begin {_basename__this_file}")
    _context__create()
    _args__parse()
    _op__perform()
    _list__print(_nameof(bike_names), bike_names)
    _list__print(_nameof(retroverse_bike_names), retroverse_bike_names)
    print(f"{file_name__batch_configs = :s}")
    print(f"end {_basename__this_file}")
# end def


if __name__ == "__main__":
    main()
# end if
