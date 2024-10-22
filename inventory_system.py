# inventory_system.py
import copy

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    electronics = {'Laptop': {'name': 'Laptop', 'price': 1000, 'quantity': 5},
                   'Smartphone': {'name': 'Smartphone', 'price': 500, 'quantity': 10}}
    
    groceries = dict(
        Apples={'name': 'Apples', 'price': 1.5, 'quantity': 100},
        Bread={'name': 'Bread', 'price': 2, 'quantity': 50}
    )
    
    inventory = {
        'Electronics': electronics,
        'Groceries': groceries,
        **{'Clothing': {item: {'name': item, 'price': price, 'quantity': 20} 
                        for item, price in [('T-shirt', 15), ('Jeans', 50)]}}
    }
    
    return inventory

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    if category in inventory and item_name in inventory[category]:
        inventory[category][item_name].update(update_info)
    else:
        inventory.setdefault(category, {})[item_name] = {'name': item_name, **update_info}

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    merged = copy.deepcopy(inv1)
    for category, items in inv2.items():
        if category not in merged:
            merged[category] = items
        else:
            for item_name, item_info in items.items():
                if item_name not in merged[category]:
                    merged[category][item_name] = item_info
                else:
                    for key, value in item_info.items():
                        if key == 'quantity':
                            merged[category][item_name][key] += value
                        else:
                            merged[category][item_name][key] = max(merged[category][item_name].get(key, 0), value)
    return merged

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    return inventory.get(category, {})

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    return max((item for category in inventory.values() for item in category.values()),
               key=lambda x: x['price'])

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for category in inventory.values():
        if item_name in category and category[item_name]['quantity'] > 0:
            return category[item_name]
    return None

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return list(inventory.keys())

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    return [item for category in inventory.values() for item in category.values()]

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    return [(category, item) for category, items in inventory.items() for item in items]

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    return copy.deepcopy(inventory) if deep else copy.copy(inventory)