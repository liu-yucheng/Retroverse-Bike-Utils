# Retroverse-Bike-Utils

- A utility toolset for the Retroverse Bike project.

# Preparation

- Install (Python)[https://www.python.org/downloads/]
- Make sure `python` and `pip` are available on your terminal command line.
- Open the repository directory in your terminal.
- Run `pip install -r ./requirements.txt` to install the python dependencies.

# Usage

## [`./retroverse_bike_configs__batch_generate.py`](./retroverse_bike_configs__batch_generate.py)

- Performs a "./bike_configs__batch_generate.py" operation with a "Retroverse-Bike_" prefix for each bike name.
- `python ./retroverse_bike_configs__batch_generate.py [--help] <bike_name_1> [bike_name_2] ...[bike_names]`

## [`./bike_configs__batch_generate.py`](./bike_configs__batch_generate.py)

- Performs a batch of "./bike_configs__generate.py" operations.
- `python ./bike_configs__batch_generate.py [--help] <bike_name_1> [bike_name_2] ...[bike_names]`

## [./bike_configs__generate.py](./bike_configs__generate.py)

- Generates configurations for a bike name.
- Uses cryptographic technologies to ensure information confidentiality.
- `python ./bike_configs__generate.py [--help] <bike_name>`

# Copyright

```
Copyright (C) 2024-2025 Yucheng Liu. Under the GNU AGPL 3.0 License.
GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt
```
