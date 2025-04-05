my_dict = {
    'tuple': (11, 12, 13, 14, 15),
    'list': [21, 22, 23, 24, 25],
    'dict': {'one': '31', 'two': '32','three': '33', 'four': '34', 'five': '35'},
    'set': {41, 42, 43, 44, 45, 44, 43, 42, 41}
}


print(my_dict['tuple'][-1])

my_dict['list'].append(26)
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 'yes'
del my_dict['dict']['three']

my_dict['set'].add(46)
my_dict['set'].remove(44)

print(my_dict)