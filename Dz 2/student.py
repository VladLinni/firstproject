import datetime
class Student:
    name = ""
    year_of_birth = 2000
    group = ""
    average_score = 10
    age = 1

    def __init__(self, name="", year_of_birth = 2000, group = "", average_score = 10, age = 1):
        self.name = name
        self.year_of_birth = year_of_birth
        self.group = group
        self.average_score = average_score
        self.age = age

    def __str__(self):
        return self.get_stats()

    def get_age(self, year_of_birth):
        age = datetime.date.today() - year_of_birth
        return age

    def get_stats(self):
        return \
            f'Имя: {self.name}\n' \
            f'Год рождения: {self.year_of_birth}\n' \
            f'Группа: {self.group}\n' \
            f'Средний балл: {self.average_score}\n' \
            f'Возраст: {self.age}\n'