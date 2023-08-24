import copy
from typing import List

class Project:
    pass

class Employee:
    _id: int = 0

    def __init__(self, employee_name: str) -> None:
        self._current_id = Employee._id
        self._employee_name = employee_name
        self._projects_list = []
        Employee._id += 1

    def __str__(self):
        str_projects = [f" {item.name} " for item in self._projects_list]
        str_projects = ''.join(str_projects)
        return f"projects: {str_projects}, \nid: {self.id}, name: {self.name}"


    def _join(self, project: Project) -> None:
        self._projects_list.append(project)

    @property
    def id(self) -> int:
        return self._current_id

    @property
    def name(self) -> str:
        return self._employee_name

    @name.setter
    def name(self, set_employee_name: str) -> None:
        self._employee_name = set_employee_name

    @property
    def projects(self) -> List[Project]:
        return copy.deepcopy(self._projects_list)

class Project:
    _id: int = 0

    def __init__(self, project_name: str, description: str) -> None:
        self._current_id = Project._id
        self._project_name = project_name
        self._description = description
        self._employees_list = []
        Project._id += 1

    def __str__(self):
        str_employees = [f" {item.name} " for item in self._employees_list]
        str_employees = ''.join(str_employees)
        return f"employee: {str_employees}, \nid: {self.id}, name: {self.name},\
 description: {self.description}"

    def add_employees(self, employee: Employee) -> None:
        for item in self._employees_list:
            if item.id == employee.id:
                raise ValueError("Error: employee already exists")
        employee._join(self)
        self._employees_list.append(employee)

    @property
    def id(self):
        return self._current_id

    @property
    def name(self) -> str:
        return self._project_name

    @name.setter
    def name(self, set_name: str) -> None:
        self._project_name = set_name

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def employees(self) -> List[Employee]:
        return copy.deepcopy(self._employees_list)

__all__ = ["Employee", "Project"]

def main() -> None:
    print("!project_emplayee run!")

if __name__ == "__main__":
    main()

