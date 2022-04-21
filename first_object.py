"""
Author: Carlos Barona
"""

class My_Obj():
    """
    Title: My_Object
    Description:
    Arguments:
    Returns:
    """
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance

    def show(self):
        print(self.name, self.importance)

    def mod_name(self, name):
        self.name = name
