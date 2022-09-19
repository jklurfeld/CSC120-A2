# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

from computer import Computer
from oo_resale_shop import ResaleShop

# Import the functions we wrote in procedural_computer_shop.py
# from procedural_computer_shop import buy, update_price, sell, print_inventory

# # Import the functions we wrote in procedural_resale_shop.py, renaming them with an 'r' prefix
from procedural_resale_shop import buy as rbuy, update_price as rupdate_price, sell as rsell, print_inventory as rprint_inventory, refurbish


""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }

def main():


    inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}

    # create a computer
    mac = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    print(mac.description)

    # make a resale shop
    shop = ResaleShop(inventory)

    print(shop.buy(mac))
    shop.print_inventory()

    shop.update_price(1, 1000)
    print("updated price:", mac.price)

    shop.refurbish(1, "macOS monterey")
    print("price after refurbish:", mac.price, "and OS after refurbish:", mac.operating_system)

    shop.sell(1)
    shop.print_inventory()

    shop.refurbish(3)

# Calls the main() function when this file is run
if __name__ == "__main__": main()
