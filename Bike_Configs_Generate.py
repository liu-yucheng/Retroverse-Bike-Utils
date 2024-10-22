"""
Generates configurations for a bike name.
"""

# Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
# GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt


from argparse import ArgumentParser as _ArgumentParser
import os as _os
import re as _re
import hashlib as _hashlib_
import json as _json_
import varname as _varname
import _Utils_DateTime


_os_path = _os.path
_nameof = _varname.core.nameof
_Script_basename = _os_path.basename(__file__)
_Parser = None
_Arguments = None

Script_NoExt, _ = _os_path.splitext(_Script_basename)
Folder_Data_Name = None
Timestamp = None
File_Configs_Name = None
Arguments_Overridden = False
Bike_Name = None
Configs_str = None
Configs_dict = None


def _Context_Create():
    global Folder_Data_Name
    global Timestamp
    global File_Configs_Name

    if Folder_Data_Name is None:
        Folder_Data_Name = _os_path.dirname(__file__)

        Folder_Data_Name = \
            _os_path.join(Folder_Data_Name, f".{Script_NoExt}_Data")
        # end statement

    _os.makedirs(Folder_Data_Name, exist_ok=True)

    if Timestamp is None:
        Timestamp = _Utils_DateTime.DateTime_Custom_FindStringFor_Now()

    if File_Configs_Name is None:
        File_Configs_Name = f"Bike-Configs_{Timestamp}.json"
        File_Configs_Name = _os_path.join(Folder_Data_Name, File_Configs_Name)
    # end if


def _Arguments_Parse():
    global _Parser
    global _Arguments
    global Bike_Name

    _Parser = _ArgumentParser(
        prog=_Script_basename,
        usage=f"python {_Script_basename} [--help] <{_nameof(Bike_Name)}>",
        description="Generates configurations for a bike name.",

        epilog=\
            "Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License."
    )

    _Parser.add_argument(
        f"{_nameof(Bike_Name)}",
        type=str,
        help="Bike name.",
        metavar=f"{_nameof(Bike_Name)}"
    )

    if not Arguments_Overridden:
        _Arguments = _Parser.parse_args()

        if Bike_Name is None:
            Bike_Name = _Arguments.Bike_Name

        Bike_Name = str(Bike_Name)


def _Configs_Generate():
    def _HashHexStr_Find(Info: str, Digit_Count: int) -> str:
        Info_Encoded = Info.encode(encoding="utf-8")
        Hash_ = _hashlib_.sha512(Info_Encoded, usedforsecurity=True)
        Result = Hash_.hexdigest()
        Result = Result[-Digit_Count:]
        return Result

    global Configs_str
    global Configs_dict

    Configs_str = f"begin bike configs\n"\
        + f"timestamp: {Timestamp}\n"\
        + f"bike_name: {Bike_Name}\n"

    Configs_dict = {
        "timestamp": Timestamp,
        "bike_name": Bike_Name
    }

    Secret = _HashHexStr_Find(Configs_str, 8)
    Configs_str += f"secret: {Secret}\n"
    Configs_dict["secret"] = Secret

    WiFi_SSID = _HashHexStr_Find(Configs_str, 4)
    Bike_Name_Prefix = _re.split("_+", Bike_Name)[0]
    WiFi_SSID = f"{Bike_Name_Prefix}_{WiFi_SSID}"
    Configs_str += f"wifi_ssid: {WiFi_SSID}\n"
    Configs_dict["wifi_ssid"] = WiFi_SSID

    WiFi_Password = _HashHexStr_Find(Configs_str, 4)
    WiFi_Password = f"0000{WiFi_Password}"

    Configs_str += \
        f"wifi_password: {WiFi_Password}\n"\
        + f"end bike configs"

    Configs_dict["wifi_password"] = WiFi_Password


def _File_Configs_Generate():
    with open(File_Configs_Name, "w+", encoding="utf-8") as File_Configs:
        _json_.dump(Configs_dict, File_Configs, indent=4)
    # end with


def Main():
    """
    Starts the main procedure.
    """
    print(f"begin {_Script_basename}")
    _Context_Create()
    _Arguments_Parse()
    _Configs_Generate()
    _File_Configs_Generate()

    print(
        f"{Bike_Name = :s}\n"
        + f"{Configs_str = :s}\n"
        + f"{File_Configs_Name = :s}"
    )

    print(f"end {_Script_basename}")


if __name__ == "__main__":
    Main()
