import os
from dotenv import load_dotenv
import pyodbc

import SQL_Queries

load_dotenv()
DRIVER = os.getenv('MS_SQL_DRIVER')
SERVER = os.getenv('MS_SQL_SERVER')
DATABASE = os.getenv('MS_SQL_DATABASE')
PAD_DATABASE = os.getenv('MS_PAD_DATABASE')
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')

"""Simple Connection"""
# connection_string = f'''DRIVER{{SQL Server}};
#                         SERVER={SERVER}
#                         DATABASE={DATABASE}
#                         Trusted_Connection=yes'''

# """SecureConnection"""
connection_string = f'''DRIVER={DRIVER};
                        SERVER={SERVER};
                        DATABASE={PAD_DATABASE};
                        UID={USER};
                        PWD={PASSWORD}'''

created_db = 'Компания'
conn = pyodbc.connect(connection_string)
conn.autocommit = True

try:
    SQL_Query = SQL_Queries.create_data_default(created_db)
    conn.execute(SQL_Query)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    print(f"БД {created_db} создана")
finally:
    conn.close()


conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
table_name = 'Компания'
active_db_name = 'Компания'

try:
    SQL_Query = SQL_Queries.create_table(table_name)
    cursor.execute(fr"USE {active_db_name};")
    cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    print(f"Таблица {table_name} создана")
finally:
    conn.close()


conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = 'Компания'
table_name = 'Компания'
try:
    SQL_Query = SQL_Queries.insert_data(table_name)
    cursor.execute(fr"USE {active_db_name};")
    cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    print(f"Данные в {table_name} добавленны")
finally:
    conn.close()


conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = 'Компания'
table_name = 'Компания'
data_list = []
try:
    SQL_Query = SQL_Queries.get_data(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    # print(records)
    for record in records:
        data_dict = {'id': record.Id,
                     'Имя': record.Имя,
                     'Фамилия': record.Фамилия,
                     'Должность': record.Должность,
                     'Зарплата': record.Зарплата}
        data_list.append(data_dict)
finally:
    conn.close()

print(data_list)
for data in data_list:
    print(data)