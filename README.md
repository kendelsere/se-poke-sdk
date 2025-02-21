# se-poke-sdk

A Python SDK for interacting with the PokéAPI (pokeapi.co), providing easy access to Pokémon data.

## Installation

### From Source

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Clone the repository:
```bash
git clone https://github.com/yourusername/se-poke-sdk.git
cd se-poke-sdk
```

3. Install the package in editable mode:
```bash
pip install .
```

## Basic Usage

See basic_usage.py for examples

## Features

- Fetch Pokemon by ID or name
- Paginated listing of Pokemon
- Access to detailed Pokemon information including:
  - Base stats
  - Types
  - Abilities
  - Moves
  - Game indices
  - Held items
  - Sprites
  - And more!

## Requirements

- Python 3.11+
- requests

## Design Considerations

My primary concern with this SDK was to make it as easy to use as possible. To this end, I've decided to add model classes that wrap the JSON responses from the API. This allows me to use type hints and make it easier to access the data.

The main exception to this is the Fetchable class. This class is used to represent URLs that can be fetched from the API. I chose to not every model from the API in this version and instead allow the user to define their own models as needed or retrieve the JSON data directly for models that are not available in the SDK

This should make the SDK both useable for cases outside the initial scope, but also allows future updates to the SDK to be made without breaking changes.

## Tools used

- Cursor IDE to generate the initial project structure and tertiary files like the README and tests
- Pytest for testing
- Pip for dependency management



