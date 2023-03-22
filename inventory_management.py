"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list."""
    inventory_count = {}
    for item in items:
        inventory_count[item] = inventory_count.get(item, 0) + 1
    return inventory_count
    
 
def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`."""
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory
    

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list."""
    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string."""
    inventory.pop(item, None)
    return inventory
    

def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory."""
    inventory_list = []
    for key in inventory:
        if inventory[key] > 0:
            inventory_list.append((key, inventory[key]))
    return inventory_list
