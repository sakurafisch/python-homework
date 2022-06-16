class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, position: str, phone: str) -> None:
        self.employee_id: int = employee_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.position: str = position
        self.phone: str = phone
    
    def __str__(self) -> str:
        return f'{self.employee_id} {self.first_name} {self.last_name}'
    
    def __repr__(self) -> str:
        # return f"{type(self).__name__}('{self.employee_id}', '{self.first_name}', '{self.last_name}', '{self.position}', '{self.phone}')"
        return f"Employee('{self.employee_id}', '{self.first_name}', '{self.last_name}', '{self.position}', '{self.phone}')"
    
employeeObj1: Employee = Employee(100001, 'John', 'Lee', 'Accountant', '0001')
employeeObj2: Employee = Employee(100002, 'Mary', 'Zheng', 'Programmer', '0002')
employeeObj3: Employee = Employee(100003, 'Cindy', 'Wilson', 'DBA', '0001')

	
print(str(employeeObj1))
print(repr(employeeObj1))
print(str(employeeObj2))
print(repr(employeeObj2))