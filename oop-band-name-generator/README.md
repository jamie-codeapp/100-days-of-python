# Band Name Generator

A simple Python program that generates a band name based on the user's input of their hometown and pet's name.

## Overview

The Band Name Generator is a fun and interactive command-line application that prompts users for their city of origin and their pet's name, then combines these inputs to create a unique band name. This project is designed for educational purposes and to demonstrate basic object-oriented programming concepts in Python.

## Features

-   Prompts users for input.
-   Generates a band name using the provided city and pet name.
-   Displays the generated band name in a user-friendly format.

## Requirements

-   Python 3.x
-   No external libraries are required.

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Download or clone this repository to your local machine.
3. Navigate to the directory containing `main.py`.

## Usage

To run the Band Name Generator, execute the following command in your terminal:

```
python main.py
```

## Code Structure

The code consists of a single class, BandNameGenerator, which contains the following methods:

-   `__init__`: Initializes the class with empty attributes for city and pet.
-   `get_user_input`: Prompts the user for their city and pet's name, storing them as attributes.
-   `generate_band_name`: Combines the city and pet name to create a band name.
-   `display_band_name`: Prints the generated band name to the console.

## Example

```
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
> New York
What's your pet's name?
> Fluffy
Your band name could be New York Fluffy
```
