from utility_functions import create_tables

# Setup the sourceSystem table:
with open('./src/sql/setupSourceSystem.sql', 'r') as file:
    query = file.read()
    try:
        create_tables(query)
        print('sourceSystem table successfully created.')
    except Exception as e:
        print(f'Error: {e}')

# Setup the sourceEntity table:
with open('./src/sql/setupSourceEntity.sql', 'r') as file:
    query = file.read()
    try:
        create_tables(query)
        print('sourceEntity table successfully created.')
    except Exception as e:
        print(f'Error: {e}')