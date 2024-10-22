# Retroverse-Bike-Utils

- A utility toolset for the Retroverse Bike project.

# Preparation

- Install (Python)[https://www.python.org/downloads/]
- Make sure `python` and `pip` are available on your terminal command line.
- Open the repository directory in your terminal.
- Run `pip install -r ./requirements.txt` to install the python dependencies.

# Usage

## [`Bike_Configs_Generate.py`](./Bike_Configs_Generate.py)

- Generates configurations for a bike name.
- Uses cryptographic technologies to ensure information confidentiality.
- `python Bike_Configs_Generate.py [--help] <Bike_Name>`

## [`Batch_Bike_Configs_Generate.py`](./Batch_Bike_Configs_Generate.py)

- Performs a batch of "Bike_Configs_Generate.py" operations.
- `python Batch_Bike_Configs_Generate.py [--help] <Bike_Name1> [Bike_Name2] ...[Bike_Names]`

## [`Batch_RetroverseBike_Configs_Generate.py`](./Batch_RetroverseBike_Configs_Generate.py)

- Performs a "Batch_Bike_Configs_Generate.py" operation with a "Retroverse-Bike_" prefix for each bike name.
- `python Batch_RetroverseBike_Configs_Generate.py [--help] <Bike_Name1> [Bike_Name2] ...[Bike_Names]`

# Copyright

```
Copyright (C) 2024 Yucheng Liu. Under the GNU AGPL 3.0 License.
GNU AGPL 3.0 License available at: https://www.gnu.org/licenses/agpl-3.0.txt
```
