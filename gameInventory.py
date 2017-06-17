from collections import OrderedDict
import csv


def display_inventory(inventory):
    for val, key in sorted(inventory.items()):
        print(key, val)
    print('Total number of items:', sum(inv.values()))


def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        inventory.setdefault(added_items[i], 0)
        inventory[added_items[i]] = inventory[added_items[i]] + 1

    return inventory


def max_length(list_of_elements):
    x = 0
    for item in list_of_elements:
        if len(str((item))) > x:
                x = len(str(item))
    return(x)


def print_table(inventory, order=None):

    value_inv = list(inv.values())
    key_inv = list(inv.keys())

    print("Inventory:")
    print()
    spacelength_count=max_length(value_inv)-len("count")
    spacelength_item_name = max_length(key_inv)-len("Item name")
    print(spacelength_count*' '," count", spacelength_item_name*' ',  " Item name")

    list_line = ['_']*20
    print(*(list_line))
    print()
    max_key_inv = max_length(key_inv)
    if max_key_inv <9:
        max_key_inv =9
    max_value_inv = max_length(value_inv)
    if max_value_inv <5:
        max_value_inv =5

    if order == "count,desc":
        sortedinv = OrderedDict(sorted(inventory.items(), key=lambda t: t[1], reverse=True))
        for key, valeu in sortedinv.items():
            spacelength_key = max_key_inv-len(str(key))
            spacelength_val = max_value_inv-len(str(value))
            print (spacelength_val*' ', value, ' ', spacelength_key*' ', key)

    elif order == "count,asc":
        sortedinv = OrderedDict(sorted(inventory.items(), key=lambda t: t[1], ))
        for key, value in sortedinv.items():
            spacelength_key = max_key_inv-len(str(key))
            spacelength_val = max_value_inv-len(str(value))
            print (spacelength_val*' ', value, ' ', spacelength_key*' ', key)

    else:
        for key, value in inventory.items():
            spacelength_key = max_key_inv-len(str(key))
            spacelength_val = max_value_inv-len(str(value))
            print (spacelength_val*' ', value, ' ', spacelength_key*' ', key)
    print(*(list_line))
    print('Total number of items:', sum(inv.values()))


def import_inventory(inventory, filename="test_inv.csv"):
    reader = csv.reader(open(filename, 'r', newline=''),quoting=csv.QUOTE_NONE, escapechar="|")

    for row in reader:
        add_to_inventory(inventory, row)


def export_inventory(inventory, filename="test_inventory_export.csv"):
    export_items = []
    writer = csv.writer(open(filename, 'w', newline=''),quoting=csv.QUOTE_NONE, escapechar="|")
    for key, value in inventory.items():
        for i in range(value):
            export_items.append(key)
    writer.writerow(export_items)

# >>>main<<<


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
display_inventory(inv)
inv = add_to_inventory(inv, dragonLoot)
print_table(inv, order="count,asc")
import_inventory(inv, "specialcharacter.csv")
print_table(inv, order="count,asc")
export_inventory(inv, "test1.csv")
