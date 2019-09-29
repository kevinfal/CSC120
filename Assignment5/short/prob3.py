"""
    File: prob3.py
    Author: Kevin Falconett
    Purpose: Provides prob3() which is like a
             "shape" or something
"""


def prob3():
    """
        creates shape
        
        Returns:
        epic shape that has lots of references
        and stuff going all over the place
    """
    layer3_0 = [11, 22]
    layer3_1 = [33, 44]
    layer2_0 = [layer3_0, layer3_1]
    layer2_1 = [layer3_0, layer3_1]
    layer1 = [layer2_0, layer2_1, layer2_0, layer2_1]

    return layer1
