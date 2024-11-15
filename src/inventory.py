import os
import json

# Path to the inventory file
INVENTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/inventory.json")

def load_inventory():
    """
    Load ingredients inventory from a JSON file.

    Returns:
        set: A set of ingredients in the inventory.
    """
    if not os.path.exists(INVENTORY_FILE):
        return set()

    with open(INVENTORY_FILE, "r") as file:
        return set(json.load(file))

def save_inventory(inventory):
    """
    Save the ingredients inventory to a JSON file.

    Args:
        inventory (set): A set of ingredients to save.
    """
    with open(INVENTORY_FILE, "w") as file:
        json.dump(list(inventory), file)

def add_to_inventory(ingredients):
    """
    Add ingredients to the inventory.

    Args:
        ingredients (list): List of ingredients to add.
    """
    inventory = load_inventory()
    inventory.update(ingredients)
    save_inventory(inventory)
    print(f"Added ingredients to inventory: {ingredients}")

def remove_from_inventory(ingredients):
    """
    Remove ingredients from the inventory.

    Args:
        ingredients (list): List of ingredients to remove.
    """
    inventory = load_inventory()
    inventory.difference_update(ingredients)
    save_inventory(inventory)
    print(f"Removed ingredients from inventory: {ingredients}")

def view_inventory():
    """
    Display the current ingredients inventory.
    """
    inventory = load_inventory()
    print("\nCurrent Inventory:")
    for ingredient in sorted(inventory):
        print(f"- {ingredient}")
