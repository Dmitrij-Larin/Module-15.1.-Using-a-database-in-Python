def create_data_default(name):
    COMMAND = fr"CREATE DATABASE {name};"
    return COMMAND


def create_table(name):
    COMMAND = fr"""CREATE TABLE {name}
                   (Id int PRIMARY KEY,
                    Имя nvarchar(50),
                    Фамилия nvarchar(50),
                    Должность nvarchar(50),
                    Зарплата money);"""
    return COMMAND


def insert_data(name):
    COMMAND = fr"""INSERT INTO {name} (Id, Имя, Фамилия, Должность, Зарплата)
                   VALUES
                   (1, 'Сергей', 'Иванов', 'Менеджер', 75000),
                   (2, 'Анна', 'Петрова', 'Аналитик', 68000),
                   (3, 'Алексей', 'Сидоров', 'Программист', 90000),
                   (4, 'Мария', 'Васильева', 'Дизайнер', 72000),
                   (5, 'Дмитрий', 'Смирнов', 'Инженер', 85000),
                   (6, 'Екатерина', 'Кузнецова', 'Маркетолог', 65000)"""
    return COMMAND


def get_data(name):
    COMMAND = fr"""SELECT Id, Имя, Фамилия, Должность, Зарплата
                   FROM {name}"""
    return COMMAND
