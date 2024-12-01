# list -> array, mengakses dengan menggunakan index

data_list = ['ucup', 'otong', 'dudung']
print(data_list[0])

print(10 * '=')

# Dictionary (dict) -> associative array
# Identifier -> key

data_dict = {
    'key': 'value',
    'pr': 'piring',
    'gl': 'gelas',
    'sn': 'sendok',
    'nmbr': 5,
    'list': data_list,
}

# bisa memanggil value dengan menggunakan key
print(data_dict['pr'], data_dict['nmbr'], data_dict['list'])
