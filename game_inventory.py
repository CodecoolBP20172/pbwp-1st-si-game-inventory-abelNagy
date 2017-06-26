inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory:")
    number_of_items = 0
    for k, v in inventory.items():
        print(v, k)
        number_of_items += v
    print("Total number of items: %g" % number_of_items)


display_inventory(inv)
print("")


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        elif item not in inventory:
            inventory[item] = 1
    return inventory


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

'''
def print_table(inventory, order=None):
'''
