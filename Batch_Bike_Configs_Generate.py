"""
Performs a batch of "Bike_Configs_Generate.py" operations.
"""

# Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt


from argparse import ArgumentParser as _ArgumentParser
import os as _os
import json as _json_
import varname as _varname
import Bike_Configs_Generate as _Bike_Configs_Generate
import _Utils_DateTime


_os_path = _os.path
_nameof = _varname.core.nameof
_Script_basename = _os_path.basename(__file__)
_Parser = None
_Arguments = None

Script_NoExt, _ = _os_path.splitext(_Script_basename)
Folder_Data_Name = None
Timestamp = None
File_BatchConfigs_Name = None
Arguments_Overridden = False
Bike_Names = None
Configs_str_list = None
BatchConfigs_dict = None


def _Context_Create():
    global Folder_Data_Name
    global Timestamp
    global File_BatchConfigs_Name

    if Folder_Data_Name is None:
        Folder_Data_Name = _os_path.dirname(__file__)

        Folder_Data_Name = \
            _os_path.join(Folder_Data_Name, f".{Script_NoExt}_Data")
        # end statement

    _os.makedirs(Folder_Data_Name, exist_ok=True)

    if Timestamp is None:
        Timestamp = _Utils_DateTime.DateTime_Custom_FindStringFor_Now()

    if File_BatchConfigs_Name is None:
        File_BatchConfigs_Name = f"Batch_Bike-Configs_{Timestamp}.json"

        File_BatchConfigs_Name = \
            _os_path.join(Folder_Data_Name, File_BatchConfigs_Name)
        # end statement
    # end if


def _Arguments_Parse():
    global _Parser
    global _Arguments
    global Bike_Names

    _Parser = _ArgumentParser(
        prog=_Script_basename,

        usage=\
            f"python {_Script_basename} [--help] <Bike_Name1>"
            + f" [Bike_Name2] ...[{_nameof(Bike_Names)}]",

        description=\
            "Performs a batch of \"Bike_Configs_Generate.py\" operations.",

        epilog=\
            "Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License."
    )

    _Parser.add_argument(
        f"{_nameof(Bike_Names)}",
        nargs="+",
        type=str,
        help="Bike names.",
        metavar=f"{_nameof(Bike_Names)}"
    )

    if not Arguments_Overridden:
        _Arguments = _Parser.parse_args()

        if Bike_Names is None:
            Bike_Names = _Arguments.Bike_Names

        for index, bike_name in enumerate(Bike_Names):
            Bike_Names[index] = str(bike_name)
        # end for
    # end if


def _BatchOperations_Perform():
    global Configs_str_list
    global BatchConfigs_dict

    print(f"begin {_nameof(_BatchOperations_Perform)}")
    Configs_str_list = []
    config_dict_list = None
    BatchConfigs_dict = {
        _nameof(config_dict_list): []
    }

    for Index, Bike_Name in enumerate(Bike_Names):
        print(f"begin Operation {Index + 1} / {len(Bike_Names)}")
        _Bike_Configs_Generate.Folder_Data_Name = Folder_Data_Name
        _Bike_Configs_Generate.Timestamp = Timestamp

        _Bike_Configs_Generate.File_Configs_Name = \
            f"Bike-Configs_{Timestamp}_{Index + 1}.json"

        _Bike_Configs_Generate.File_Configs_Name = _os_path.join(
            Folder_Data_Name,
            _Bike_Configs_Generate.File_Configs_Name
        )

        _Bike_Configs_Generate.Arguments_Overridden = True
        _Bike_Configs_Generate.Bike_Name = Bike_Name
        _Bike_Configs_Generate.Main()
        Configs_str_list.append(_Bike_Configs_Generate.Configs_str)

        BatchConfigs_dict[_nameof(config_dict_list)]\
            .append(_Bike_Configs_Generate.Configs_dict)

        print(f"end Operation {Index + 1} / {len(Bike_Names)}")

    print(f"end {_nameof(_BatchOperations_Perform)}")


def _File_BatchConfigs_Generate():
    with open(
        File_BatchConfigs_Name,
        "w+",
        encoding="utf-8"
    ) as File_BatchConfigs:
        _json_.dump(BatchConfigs_dict, File_BatchConfigs, indent=4)
    # end with


def Main():
    """
    Starts the main procedure.
    """
    def _Print_List(Name: str, List_: list):
        Info = f"begin list {Name}\n"

        for Index, Element in enumerate(List_):
            Info += f"begin element {Index + 1} / {len(List_)}\n"\
                + f"{Element:s}\n"\
                + f"end element {Index + 1} / {len(List_)}\n"
            # end info

        Info += f"end list {Name}"
        print(Info)

    print(f"begin {_Script_basename}")
    _Context_Create()
    _Arguments_Parse()
    _BatchOperations_Perform()
    _File_BatchConfigs_Generate()
    _Print_List(_nameof(Bike_Names), Bike_Names)
    _Print_List(_nameof(Configs_str_list), Configs_str_list)
    print(f"{File_BatchConfigs_Name = :s}")
    print(f"end {_Script_basename}")


if __name__ == "__main__":
    Main()
