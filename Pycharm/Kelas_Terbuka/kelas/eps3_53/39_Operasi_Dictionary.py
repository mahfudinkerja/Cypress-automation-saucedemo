# Operator dictionary

data_dict = {
    'cup': 'ucup surucup',
    'tong': 'otong surotong',
    'dung': 'dudung surudung',
}

# Panjang dictionary
lendict = len(data_dict)
print(f"panjang dictionary : {lendict}")

# mengecek key exist atau tidak
key = "cup"
checkkey = key in data_dict
print(f"apakah {key} ada didalam data_dict : {checkkey}")

# mengakses value (read) dengan get
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get('kis', 'data key tidak ditemukan'))  # check key dengan mesaage tidak ditemukan

# update data
print(data_dict)
data_dict.update({'cup': 'ucup imut', 'par': 'gompar'})
print(data_dict)

# mendelete data dari dictionary
del data_dict['cup']
print(data_dict)
