'''
    File: shapes.py
    Author: Kevin Falconett
    Purpose: functions that create
             "shapes" (lists)
    Meta: If you want a
          binary tree, just
          ask
'''

def shape_alpha():
    '''
        Function for shape alpha
    '''

    layer2_0 = [1.1,-17]
    layer2_1 = [123,456]

    layer1_0 = [10,'abc','jkl',40]
    layer1_1 = [layer2_0,layer2_1]

    returned = [layer1_0,layer1_1]
    return returned

def shape_bravo():
    '''
        Function for shape bravo
    '''
    layer2_0 = ['whoa','excellent']
    layer2_1 = ['bogus','righteous']
    layer2_2 = 'rufus'

    layer1_0 = [layer2_0,layer2_1]
    layer1_1 = [layer2_1,layer2_2]

    returned = [layer1_0,layer1_1]

    return returned

def shape_charlie(arg1):
    '''
        Function for shape charlie
    '''
    layer3 = [None,arg1]
    layer2 = [layer3,arg1]
    layer1 = [layer2,arg1]
    returned = [layer1,arg1]
    return returned

def shape_delta(arg1,arg2):
    '''
        Function for shape delta
    '''
    layer3 = [arg1,arg2]
    layer2 = [arg1,arg2,layer3,[30]]
    layer1 = [arg1,layer2,[20],arg2]
    returned = [arg1,arg2,layer1,[10]]
    return returned

def shape_echo(arg1,arg2,arg3):
    '''
        Function for shape echo
    '''
    returned = []
    
    layer2 = [returned,arg3]
    layer1 = [layer2,arg2]

    returned.append(layer1)
    returned.append(arg1)

    return returned
