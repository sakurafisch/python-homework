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
    
class TeachingStaff(Employee):
    def __init__(self, employee_id: int, first_name: str, last_name: str, position: str, phone: str, subject: str) -> None:
        super().__init__(employee_id, first_name, last_name, position, phone)
        self.subject: str = subject
    
    def get_subject(self) -> str:
        return f'{self.first_name} {self.last_name} is teaching the subject of {self.subject}.'
    
    def get_course(self) -> str:
        return f'{self.first_name} {self.last_name} is teaching the subject of {self.subject}.'

	
teaching_staffObj1 = TeachingStaff("100004", "Alice", "Wang", "Teacher", "0004", "c++")
print(str(teaching_staffObj1))
print(repr(teaching_staffObj1))
print(teaching_staffObj1.get_course())