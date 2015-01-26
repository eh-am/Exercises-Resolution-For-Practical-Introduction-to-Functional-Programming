#Non-functional:

# names = ['Mary', 'Isla', 'Sam']

# for i in range(len(names)):
#     names[i] = hash(names[i])

# print names
# => [6306819796133686941, 8135353348168144921, -1228887169324443034]

names = ['Mary', 'Isla', 'Sam']

hashed_names = map(hash, names)

print hashed_names