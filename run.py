import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('employee-bonus')

# List of all employees
employees = {
        "3029557": "Diana Jordan",
        "5029737": "Amal Phan",
        "6500875": "Olivier Delarosa",
        "1505669": "Cherise Mathis",
        "3721969": "Amrit Wagner",
        "5429547": "Cristina Dickens",
        "8971943": "Amara Pitts"
    }

def get_employee_id():
    """
    Get the employee who data the user will be inputting to the sheet,
    A list of employee names with there ID will be displayed for options#
    """
    
    while True:
        print("-----------"*7)
        print('Please enter ID of the employee you wish to update:\n')
        print('''Diana Jordan - 3029557\nAmal Phan - 5029737\nOlivier Delarosa - 6500875\nCherise Mathis - 1505669\nAmrit Wagner - 3721969\nCristina Dickens - 5429547\nAmara Pitts - 8971943
        ''')
        employee_selected = input("Employee ID:\n")
        print("-----------"*7)
        if validate_input(employee_selected):
            if employee_selected not in employees:
                print("\nThere is no employee with that ID please try again")
                return get_employee_id()
            else:
                print("You have selected - "+ employees.get(employee_selected))
                break
    
    return employee_selected



def validate_input(selected):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if string cannot be converted into int,
    or if there aren't exactly 6 values
    """
    
    try:
        [int(id) for id in selected]
        if len(selected) != 7:
            raise ValueError(
                f"\nExactly 6 values required, you provided {len(selected)}"
            )
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again.\n")
        return False
    return True


def input_hours():
    '''
    Gets employee hours they worked that week
    '''
    while True:
        hours_worked = float(input("\nPlease Enter the Hours Worked:\n"))
        if valid_values(hours_worked):
            print("Data is valid!")
            break
    return hours_worked


def input_tickets():
    '''
    Gets employee number of solved tickets for that week
    '''
    while True: 
        solved_tickets = float(input("\nPlease enter the number of tickets solved by the employee:\n"))
        if valid_values(solved_tickets):
            print("Data is valid!")
            break
    return solved_tickets

def valid_values(value):
    '''
    Validates users inputs are int or floats
    '''
    try:
        input = int(value)
    except ValueError:
        try:
            input = float(value)
        except ValueError as e:
            print(f"\nInvalid data: {e}, please try again.\n")
            return False
    return True

"""
maths for hourly and bonus rates
12.30 hourly wage and 4.50 per solved ticket
"""
def cal_hourly(hours):
    hourly_pay_total = float(hours)*12.30
    hourly_pay_total = round(hourly_pay_total, 2)
    print(f"There Total hourly wages is €{hourly_pay_total}")
    return hourly_pay_total

def cal_bonus(tickets):
    bonus_total = float(tickets)*4.5
    bonus_total = round(bonus_total, 2)
    print(f"There Bonus Total is €{bonus_total}")
    return bonus_total

def update_sheet_data(data, id_sheet):
    print("updating employee records...")
    bonus_worksheet = SHEET.worksheet(id_sheet)
    bonus_worksheet.append_row(data)


def main():
    '''
    Runs all code
    '''
    append_list = []
    get_id = get_employee_id()
    employee_hours = input_hours()
    append_list.append(employee_hours)
    employee_tickets = input_tickets()
    append_list.append(employee_tickets)
    total_hours = cal_hourly(employee_hours)
    append_list.append(total_hours)
    total_tickets = cal_bonus(employee_tickets)
    append_list.append(total_tickets)
    total_pay = total_hours+total_tickets
    print(f"There total pay is €{total_pay}")
    append_list.append(total_pay)
    print(append_list)
    update_sheet_data(append_list, get_id)

main()