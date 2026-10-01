import os

#print spaces so column alligns
def print_space(column_width, info_length ):
    spaces = column_width - info_length
    print(' ' * spaces, end='')

#displays the main menu
def print_display_main_menu():
    print('=' * 40)
    print('      SALES RECORD MANAGEMENT SYSTEM  ')
    print('=' * 40)
    print('1. Add Sale Record')
    print('2. View All Records & Summary Statistics')
    print('3. Clear All Sales Data')
    print('4. Exit System')

#asks for user input from the main menu and validates it
def get_user_selection():
    print_display_main_menu()
    user_selection = input('Select an option 1-4:')

    #Validates user input
    try:
        selected_input = int(user_selection)
    except ValueError:
        print('Please enter a valid input like numbers 1 to 4')
        return

    if selected_input > 4 or selected_input < 1:
        print('Please enter a valid input like numbers 1 to 4')
    elif selected_input >= 1 and selected_input <= 4:
        return selected_input

#add record to file
def add_sales_record():
    #gets the input to add to the record
    item_name = input('Item Name: ')
    quantity_sold_input = input('Quantity Sold: ')
    price_per_unit_input = input('Price Per Unit: ')

    #validates the input before recording
    try:
        quantity_sold = int(quantity_sold_input)
        price_per_unit = float(price_per_unit_input)
    except ValueError:
        print('Inputs are Invalid Please Try Again.')
        add_sales_record()
    if not item_name.strip():
        print('Item Name cannot be blank')
        add_sales_record()

    #opens the file to append the information
    try:
        fhand = open('sales_log.txt', 'a')
    except FileNotFoundError:
        # if file not found then create
        print('Not found')
        fhand = open('sales_log.txt' 'x')
        #fhand.write('Name|Quantity|Price Per Unit|Total Amount')

    # calculates then inserts it to the files
    total_amount = quantity_sold * price_per_unit
    fhand.write(f'{item_name},{quantity_sold},{price_per_unit},{total_amount}\n')
    print('Sales record saved successfully')
    fhand.close()
    get_user_selection()

# Views the entire files and displays it to the user
def view_all_records(total_units_sold = 0,
        grand_total_revenue = 0):
    try:
        fhand = open('sales_log.txt', 'r')
    except FileNotFoundError:
        print('No records found')
        print_display_main_menu()
        get_user_selection()

    print('Name|Quantity|Price Per Unit|Total Amount')
    for lines in fhand:
        lines_info = lines.split(',')


        if len(lines_info) >1:
            total_units_sold += int(lines_info[1])
            grand_total_revenue += float(lines_info[3])
            print(lines_info[0], end=' ')
            print_space(9, len(lines_info[0]))
            print(lines_info[1], end=' ')
            print_space(8, len(lines_info[1]))
            print(lines_info[2], end=' ')
            print_space(15, len(lines_info[2]))
            print(lines_info[3])

        else:
            print(lines.strip())

    print(f'Total Units Sold: {total_units_sold}')
    print(f'Grand Total Revenue: {grand_total_revenue}')
    fhand.close()

#deletes the entire file
def clear_all_record():
    os.remove('sales_log.txt')
    print('All records cleared. No records remaining.')
    get_user_selection()





#checks for user input and directs to proper process

while True:
    user_option_selected = get_user_selection()
    if user_option_selected == 1:
        add_sales_record()
    elif user_option_selected == 2:
        view_all_records()
    elif user_option_selected == 3:
        clear_all_record()
    elif user_option_selected == 4:
        exit('Thank you for using the Sales Record Management System.')





