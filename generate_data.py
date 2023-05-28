from random import random

from factory import Factory
import pandas as pd
import factory


class CompanyFactory(Factory):
    class Meta:
        model = dict

    first_name = factory.Faker("first_name")
    last_name = factory.Faker('last_name')
    age = factory.Faker('random_int', min=20, max=45)
    position = factory.Faker('random_element', elements=(
        'junior', 'middle', 'senior', 'team_lead', 'tech_lead'))
    salary = factory.Faker('random_int', min=20000, max=45000)
    work_experience = factory.Faker('random_int', min=1, max=15)


num_rows = 50

employees = CompanyFactory.create_batch(num_rows)

for employee in employees:
    if random() < 0.1:
        employee['first_name'] = None
    if random() < 0.1:
        employee['position'] = None
    if random() < 0.1:
        employee['salary'] = -1 * employee['salary']


df = pd.DataFrame(employees)
df.to_csv('employees.csv', index=False)

print(df)