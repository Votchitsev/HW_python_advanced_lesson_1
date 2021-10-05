from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())

    today = datetime.today()
    print(today.date())
