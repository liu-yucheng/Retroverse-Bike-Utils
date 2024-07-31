# Retroverse-Bike-Utils

- A utility toolset for the Retroverse Bike project.

# Preparation

- Install (Python)[https://www.python.org/downloads/]
- Make sure `python` and `pip` are available on your terminal command line.
- Open the repository directory in your terminal.
- Run `pip install -r ./requirements.txt` to install the python dependencies.

# Usage
## `gen_bike_config_info.py`

- Generates configuration information for the specified bike name.
- Uses "block chain" technologies to ensure information confidentiality.
- `python gen_bike_config_info.py [--help] <bike-name>`

## `batch_gen_bike_config_info.py`

- Performs a batch of `gen_bike_config_info.py` operations.
- `python batch_gen_bike_config_info.py [--help] <bike-name-1> [bike-name-2] ...[bike-names]`

## `batch_gen_retroverse_bike_config_info.py`

- Performs a batch of `gen_bike_config_info.py` operations with the `Retroverse-Bike--` bike name prefix.
- `python batch_gen_retroverse_bike_config_info.py [--help] <bike-name-1> [bike-name-2] ...[bike-names]`

# Copyright

```
Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt
```
