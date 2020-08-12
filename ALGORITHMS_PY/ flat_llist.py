

# returns a flat list from a nested list


def flatten(in_list):
    result =[]
    for i in in_list:
        if  isinstance (i,list):
          flat_List = flatten(i)
          result += flat_List
        else:
          result.append(i)
    return result

    #test case
planets = ['mercury', 'venus', ['earth'],
    'mars', [['jupiter', 'saturn']], 'uranus]'
    ]
print(flatten(planets))
