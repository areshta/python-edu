# Given following data structure:
# [
# {'first_name': 'John', 'last_name': 'Cornwell', 'net_worth': 2632.345},
# {'first_name': 'Emily', 'last_name': 'Alton', 'net_worth': -4578.234},
# {'first_name': 'James', 'last_name': 'Bond', 'net_worth': 1000.07},
# ]
# Generate an output formatted like:
# ------------------------------------
# | Cornwell J. | +2632.34 |
# | Alton E. | -4578.23 |
# | Bond J. | +1000.07 |
# ------------------------------------
# - Last names are left aligned with padding to 15 chars
# - From first name display only first letter right aligned with padding, total width 2 chars, followed by ‘.’
# - Net worth column width is 10 chars, we display only first two decimals, and also sign for both positive and negative numbers
# - Data is wrapped up between ‘|’ and ‘-’ ASCII chars to print similar to a table

data = [
          {'first_name': 'John', 'last_name': 'Cornwell', 'net_worth': 2632.345},
          {'first_name': 'Emily', 'last_name': 'Alton', 'net_worth': -4578.234},
          {'first_name': 'James', 'last_name': 'Bond', 'net_worth': 1000.07},
      ]

print('-'*35)
for line in data:
    print('| {:<15} | {}. | {:+.2f} |'.format(line['first_name'], line['last_name'][0], line['net_worth']))
print('-'*35)
  
