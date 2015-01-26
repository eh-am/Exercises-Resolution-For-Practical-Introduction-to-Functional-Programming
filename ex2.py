# Non-funcional version:

# people = [{'name': 'Mary', 'height': 160},
#           {'name': 'Isla', 'height': 80},
#           {'name': 'Sam'}]

# height_total = 0
# height_count = 0
# for person in people:
#     if 'height' in person:
#         height_total += person['height']
#         height_count += 1

# if height_count > 0:
#     average_height = height_total / height_count

#     print average_height
#     # => 120

#     

# Funcional version:
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

people_with_height = filter(lambda x: 'height' in x, people)

heights_sum = reduce(lambda a, x: a + x['height'], people_with_height, 0)

average_height = heights_sum / len(people_with_height)

print average_height