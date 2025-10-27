"""
Inventory Management System Module

This module provides functions to manage inventory items, including adding,
removing, saving, and loading items. It demonstrates secure and PEP8-compliant
Python practices by handling exceptions safely and avoiding insecure functions.
"""

import json
from datetime import datetime


def add_item(stock_data, item=None, qty=0, logs=None):
    """
    Add a specified quantity of an item to the inventory.

    Args:
        stock_data (dict): The current inventory data.
        item (str): The name of the item.
        qty (int): The quantity to add.
        logs (list): Optional list to store log messages.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        print("Error: Invalid input types for add_item.")
        return stock_data

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    print(f"Added {qty} of {item}")
    return stock_data


def remove_item(stock_data, item, qty):
    """
    Remove a specified quantity of an item from the inventory.

    Args:
        stock_data (dict): The current inventory data.
        item (str): The name of the item.
        qty (int): The quantity to remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            print(f"Removed '{item}' completely from stock.")
        else:
            print(f"Removed {qty} of {item}. Remaining: {stock_data[item]}")
    except KeyError:
        print(f"Warning: Tried to remove non-existent item '{item}'.")
    except TypeError:
        print("Error: Quantity must be a number.")
    return stock_data


def get_qty(stock_data, item):
    """Return the quantity of a specific item."""
    try:
        return stock_data[item]
    except KeyError:
        print(f"Error: Item '{item}' not found in inventory.")
        return 0


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        print(f"Data loaded from {file}")
    except FileNotFoundError:
        print(f"{file} not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
        stock_data = {}
    return stock_data


def save_data(stock_data, file="inventory.json"):
    """Save current inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        print(f"Data saved to {file}")
    except OSError:
        print(f"Failed to write data to {file}.")


def print_data(stock_data):
    """Print all items and quantities in the inventory."""
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """
    Return a list of items with quantity below the given threshold.

    Args:
        stock_data (dict): The current inventory data.
        threshold (int): Minimum quantity threshold.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    stock_data = {}

    stock_data = add_item(stock_data, "apple", 10)
    stock_data = add_item(stock_data, "banana", -2)
    stock_data = add_item(stock_data, "orange", 5)
    stock_data = remove_item(stock_data, "apple", 3)
    stock_data = remove_item(stock_data, "mango", 2)

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")

    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)


if __name__ == "__main__":
    main()
