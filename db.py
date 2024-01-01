# import module name
import sqlite3 #sqlite3 is a built-in module in python 

#return= module.method(actual argument)
conn  =  sqlite3.connect('./mydatabase.sqlite') # every function return something
cursor = conn.cursor() 

query = '''
            create table if not exists employees(
                id integer primary key autoincrement,
                name text not null,
                position text not null,
                salary real not null
            );
        '''

cursor.execute(query) # query is an actual  argument
conn.commit()

query = "delete from employees;"
cursor.execute(query)

# ceo = method(actual argument1, actual argument2)
# ceo.method(string,tuple)
query = "insert into employees (name, position, salary) values (?, ?, ?);"
cursor.execute(query, ('ranu', "manager", 50000.00))
cursor.execute(query, ('tannu', "director", 55000))
cursor.execute(query, ('tanvi', "MD", 40000))
conn.commit()