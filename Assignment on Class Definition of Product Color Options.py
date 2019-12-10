#Devon Keen
#CS 100-017
#11/30/18
#Assignment on Class Definition of Product Color Options

#1

class ColorOptionsClass:
    '''it contains entries of key value pairs from a special dictionary'''
    def __init__(self):
        self.products = {}

    def add_product(self, product, color_options):
        self.products[product] = color_options

    def get_matching_products(self, color):
        productList = []
        for product in self.products:
            if color in self.products[product]:
                productList.append[product]
            else:
                return productList

#2

import color_options_catalog
appliances = color_options_catalog.ColorOptionsClass()
appliances.add_product("microwave", ["black", "white"])
appliances.add_product("stove",["stainless", "white"])
print(appliances.get_matching_products("stainless"))
