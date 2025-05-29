class Employee:
    def __init__(self, name, employee_id, hourly_wage, shift_hours):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.shift_hours = shift_hours
        self.hours_worked = 0

    def clock_in(self):

        print(f"{self.name} has clocked in.")

    def clock_out(self):
        print(f"{self.name} has clocked out.")

    def get_pay(self):
        pay = self.hours_worked * self.hourly_wage
        print(f"{self.name} has been paid {pay}")
class Cashier(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, meal):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.meal = meal
    def handle_transaction(self):
        print(f"{self.name} prepared {self.meal}, specializing in {self.specialty}.")


class Cleaner(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, cleaning_area):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.cleaning_area = cleaning_area

    def sanitize_area(self):
        print(f"{self.name} sanitized the {self.cleaning_area}.")

class DriveThruCashier(Cashier):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, register_id, headset_id):
        super().__init__(name, employee_id, hourly_wage, shift_hours, register_id)
        self.headset_id = headset_id

    def take_order(self, customer_name, order):
        print(f"{self.name} (headset {self.headset_id}) took an order from {customer_name}: {order}.")

class Cook(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, specialty):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.specialty = specialty

    def prepare_meal(self, meal):
        print(f"{self.name} prepared {meal}, specializing in {self.specialty}.")


class SousChef(Cook):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, specialty, certification):
        super().__init__(name, employee_id, hourly_wage, shift_hours, specialty)
        self.certification = certification

    def oversee_kitchen(self):
        print(f"{self.name}, a certified {self.certification}, is overseeing the kitchen operations.")
