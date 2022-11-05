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

def get_employee_id():
    """
    Get the employee who data the user will be inputting to the sheet,
    A list of employee names with there ID will be displayed for options"""

    print('Please enter ID of the employee you wish to update:\n')
    print('''
Diana Jordan - 3029557\nAmal Phan - 5029737\nOlivier Delarosa - 6500875\nCherise Mathis - 1505669\nAmrit Wagner - 3721969\nCristina Dickens - 5429547\nAmara Pitts - 8971943
    ''')
    employee_selected = input("Empolyee ID: ")
    print(f"You have selected - {employee_selected}")


get_employee_id()