import employee_and_project
import copy
from typing import List

class Company:
    def __init__(self) -> None:
        self._employees = []
        self._projects = []

    def __str__(self):
        str_employees = [f" {item} " for item in self._employees]
        str_projects = [f" {item} " for item in self._projects]
        str_employees = ''.join(str_employees)
        str_projects = ''.join(str_projects)

        return f"projects:\n   {str_projects},\nemplyees:\n    {str_employees}"

    @property
    def employees(self) -> List[employee_and_project.Employee]:
        return copy.deepcopy(self._employees)

    @property
    def project(self) -> List[employee_and_project.Project]:
        return copy.deepcopy(self._projects)

    def add_project(self, project: employee_and_project.Project) -> None:
        for item in self._projects:
            if item.id == project.id:
                raise ValueError("Error: project already exists")
        self._projects.append(project)

    def add_employees(self, employee: employee_and_project.Employee) -> None:
        for item in self._employees:
            if item.id == employee.id:
                raise ValueError("Error: employee already exists")
        self._employees.append(employee)

    def del_employee(self, employee: employee_and_project.Employee) -> None:
        flag = False
        for item in self._employees:
            if item.id == employee.id:
                del item
                flag = True
        if not flag:
            raise ValueError("Error: employee does not exist")

    def del_project(self, project: employee_and_project.Project) -> None:
        flag = False
        for item in self._projects:
            if item.id == project.id:
                del item
                flag = True
        if not flag:
            raise ValueError("Error: project does not exist")

def main() -> None:
    print("!company run!")

if __name__ == "__main__":
    main()
