# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import csv
# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print(v, k)
    print("Total number of items: %g" % sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        elif item not in inventory:
            inventory[item] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    longest_item = max(len(k) for k in inventory)
    longest_count = max(len(str(v)) for v in inventory.values())
    space_between = longest_item - len("inventory")
    dashes = longest_item + space_between + len("count ")
    print("Inventory:")
    print("count ".rjust(longest_count) + "item name".rjust(longest_item))
    print("-" * dashes)
    keys_inventory = list(inventory)
    if order == "count,desc":
        values_inventory = list(reversed(sorted(inventory.values())))
        #inventory_local = sorted([(v, k) for k, v in inventory.items()], reverse = True)
        #print(inventory_local)
        print(values_inventory)
    elif order == "count,asc":
        values_inventory = sorted(inventory.values())
        #inventory_local = sorted([(v, k) for k, v in inventory.items()])
        #print(inventory_local)

    else:
        for k, v in inventory.items():
            print(v, k)
    print("-" * dashes)
    print("Total number of items: %g" % sum(inventory.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    if filename is None:
        filename = "import_inventory.csv"
    with open(filename, "r") as csvfile:
        for i in csv.reader(csvfile):
            add_to_inventory(inventory, i)
        return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    to_export = []
    if filename is None:
        filename = "export_inventory.csv"
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile)
        for k, v in inventory.items():
            to_export.append(k)
