from crud_operations import insert_row, read_rows, update_row, delete_row

# Insert a new row
insert_row('John Doe', 30, 'john@example.com', 55000.50, 1, '2024-09-16', '2024-09-16', '123-456-7890', b'Some notes')

# Read all rows
rows = read_rows()
print('Rows after insertion:')
for row in rows:
    print(row)

# Update the row
update_row(1, name='Jane Doe', email='jane@example.com')

# Read all rows after update
rows = read_rows()
print('\nRows after update:')
for row in rows:
    print(row)

# Delete the row
delete_row(1)

# Read all rows after deletion
rows = read_rows()
print('\nRows after deletion:')
for row in rows:
    print(row)
