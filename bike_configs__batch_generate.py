"""
Performs a batch of "bike_configs__generate.py" operations.
"""

# Copyright (C) 2024-2025 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt .


from argparse import ArgumentParser as _ArgumentParser
import os as _os
import json as _json_
import varname as _varname
import bike_configs__generate as _bike_configs__generate
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
"""A timestamp for batch operations."""
file_name__batch_configs: str = None
"""The file name of the batch bike configs."""
args_overridden: bool = False
"""Whether the arguments are overridden."""
bike_names: list[str] = None
"""A list of bike names."""
strs__batch_configs: list[str] = None
"""A list of bike configs in string format."""
dict__batch_configs: dict = None
"""A list of bike configs in dict format."""


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
        file_name__batch_configs = f"batch__bike_configs__{timestamp}.json"
        file_name__batch_configs = _os_path.join(folder_name__data, file_name__batch_configs)
    # end if
# end def


def _args__parse():
    global _parser
    global _args
    global bike_names

    _parser = _ArgumentParser(
        prog=_basename__this_file,
        usage=f"python {_basename__this_file} [--help] <bike_name_1> [bike_name_2] ...[{_nameof(bike_names)}]",
        description="Performs a batch of \"bike_configs__generate.py\" operations.",
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


def _batch_ops__perform():
    global strs__batch_configs
    global dict__batch_configs

    print(f"begin {_nameof(_batch_ops__perform)}")
    strs__batch_configs = []
    dicts__configs = None

    dict__batch_configs = {
        _nameof(dicts__configs): []
    }

    for index, bike_name in enumerate(bike_names):
        print(f"begin Operation {index + 1} / {len(bike_names)}")
        _bike_configs__generate.folder_name__data = folder_name__data
        _bike_configs__generate.timestamp = timestamp
        _bike_configs__generate.file_name__configs = f"bike_configs__{timestamp}__{index + 1}.json"

        _bike_configs__generate.file_name__configs = \
            _os_path.join(folder_name__data, _bike_configs__generate.file_name__configs)
        # end statement

        _bike_configs__generate.args__overridden = True
        _bike_configs__generate.bike_name = bike_name
        _bike_configs__generate.main()
        strs__batch_configs.append(_bike_configs__generate.str__configs)
        dict__batch_configs[_nameof(dicts__configs)].append(_bike_configs__generate.dict__configs)
        print(f"end Operation {index + 1} / {len(bike_names)}")
    # end for

    print(f"end {_nameof(_batch_ops__perform)}")
# end def


def _batch_configs_file__generate():
    with open(file_name__batch_configs, "w+", encoding="utf-8") as batch_configs_file:
        _json_.dump(dict__batch_configs, batch_configs_file, indent=4)
    # end with
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
    _batch_ops__perform()
    _batch_configs_file__generate()
    _list__print(_nameof(bike_names), bike_names)
    _list__print(_nameof(strs__batch_configs), strs__batch_configs)
    print(f"{file_name__batch_configs = :s}")
    print(f"end {_basename__this_file}")
# end def


if __name__ == "__main__":
    main()
# end if
