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

heights = map(lambda x: x['height'], 
  filter(lambda x: 'height' in x, people))

if (len(heights) > 0):
  from operator import add
  heights_sum = reduce(operator.add, heights)
  average_height = heights_sum / len(heights)
  print average_height