#
# Recipe.py
#
# This object serves as a container for an imported recipe.
#

class Recipe(object):

    def __init__(self):
        # metadata
        self.__title = None
        # recipe contents
        self.__ingredients = None
        self.__steps = None
